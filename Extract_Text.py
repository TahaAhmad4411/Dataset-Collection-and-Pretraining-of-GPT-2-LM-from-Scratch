import requests
import gzip
import json
import os
from io import BytesIO
from warcio.recordloader import ArcWarcRecordLoader
from bs4 import BeautifulSoup

# Create output folder
os.makedirs("extracted_texts", exist_ok=True)

# Read the list of WARC records from CommonCrawl_List.txt
with open("CommonCrawl_List.txt", "r", encoding='utf-8') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    try:
        data = json.loads(line)

        warc_filename = data.get('filename')
        try:
            offset = int(data.get('offset'))  # Convert to integer
            length = int(data.get('length'))  # Convert to integer
        except (ValueError, TypeError):
            print(f"Skipping invalid offset/length at line {idx + 1}")
            continue

        url = data.get('url')

        if not (warc_filename and offset and length):
            print(f"Skipping invalid entry at line {idx + 1}")
            continue

        # Build WARC URL
        warc_url = f"https://data.commoncrawl.org/{warc_filename}"

        # Download the partial WARC record
        headers = {'Range': f'bytes={offset}-{offset + length - 1}'}
        response = requests.get(warc_url, headers=headers, timeout=30)

        if response.status_code == 206:  # 206 = Partial Content
            print(f"Downloaded WARC record for {url}")

            # Decompress the gzip content
            compressed_stream = BytesIO(response.content)
            decompressed_stream = gzip.GzipFile(fileobj=compressed_stream)

            # Parse the decompressed WARC record
            loader = ArcWarcRecordLoader()
            record = loader.parse_record_stream(decompressed_stream)

            if record.rec_type == 'response':
                payload = record.content_stream().read()
                html_content = payload.decode('utf-8', errors='replace')

                # Extract clean text from HTML
                soup = BeautifulSoup(html_content, 'html.parser')
                clean_text = soup.get_text(separator='\n', strip=True)

                # Save to .txt file using domain name or url path
                domain_part = url.split('//')[-1].split('/')[0].replace(':', '_')
                file_name = f"extracted_texts/{idx+1}_{domain_part}.txt"
                
                with open(file_name, 'w', encoding='utf-8') as f_out:
                    f_out.write(clean_text)

                print(f"✅ Extracted and saved to {file_name}")
            else:
                print(f"Record is not a response at {url}")

        else:
            print(f"Failed to download: {url}, Status code {response.status_code}")

    except Exception as e:
        print(f"Error processing line {idx + 1}: {e}")
