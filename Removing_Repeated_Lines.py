def remove_repeated_lines_from_file():
    input_file = "clean_dataset.txt"
    output_file = "Repeated_Lines_Removed.txt"

    seen_lines = set()
    cleaned_lines = []

    try:
        with open(input_file, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                line = line.strip()
                if line and line not in seen_lines:
                    seen_lines.add(line)
                    cleaned_lines.append(line)
    except Exception as e:
        print(f"Error reading {input_file}: {e}")
        return

    with open(output_file, 'w', encoding='utf-8') as out:
        for line in cleaned_lines:
            out.write(line + '\n')

    print(f"\n✅ Cleaned file saved as {output_file} with {len(cleaned_lines)} unique lines.")

# Run the function
remove_repeated_lines_from_file()
