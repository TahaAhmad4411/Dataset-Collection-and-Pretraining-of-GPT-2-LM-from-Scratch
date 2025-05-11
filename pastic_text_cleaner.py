import os
import re

def is_binary_file(filepath):
    try:
        with open(filepath, 'rb') as f:
            chunk = f.read(1024)
            if b'\x00' in chunk:
                return True
            return False
    except:
        return True

def clean_text(text):
    # Remove non-ASCII characters
    text = text.encode("ascii", "ignore").decode()
    
    # Remove extra spaces and empty lines
    text = re.sub(r'\s+', ' ', text)
    
    # Replace multiple line breaks with one
    text = re.sub(r'\n{2,}', '\n', text)
    
    return text.strip()

def extract_clean_paragraphs(directory_path, output_file):
    all_paragraphs = []

    for filename in sorted(os.listdir(directory_path)):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory_path, filename)
            if is_binary_file(filepath):
                print(f"Skipping binary/corrupted file: {filename}")
                continue
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
                    text = file.read()
                    cleaned = clean_text(text)
                    # Filter out navigation/menu-like lines
                    if len(cleaned) > 50:  # Skip very short lines
                        all_paragraphs.append(cleaned)
            except Exception as e:
                print(f"Error reading {filename}: {e}")

    # Save all cleaned text into one file
    with open(output_file, 'w', encoding='utf-8') as out:
        for para in all_paragraphs:
            out.write(para + '\n')

# Set your folder path here
source_folder = "pastic_texts"  # Replace with your actual directory path
output_file = "pastic_basic_filter.txt"

extract_clean_paragraphs(source_folder, output_file)
print(f"\n✅ Cleaning complete. Output saved to: {output_file}")
