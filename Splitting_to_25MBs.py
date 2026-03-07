def split_large_file(file_path, max_chunk_size=25 * 1024 * 1024):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = []
        size = 0
        part = 1

        for line in f:
            lines.append(line)
            size += len(line.encode('utf-8'))
            if size >= max_chunk_size:
                with open(f"part_{part}.txt", 'w', encoding='utf-8') as out:
                    out.writelines(lines)
                print(f"Saved part_{part}.txt")
                lines, size = [], 0
                part += 1

        # Save any remaining lines
        if lines:
            with open(f"part_{part}.txt", 'w', encoding='utf-8') as out:
                out.writelines(lines)
            print(f"Saved part_{part}.txt")

# Example usage
split_large_file("clean_dataset.txt")
