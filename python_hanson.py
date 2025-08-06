import os

# Step 1: Check and create folders
input_dir = "data_input"
output_dir = "data_output"

if not os.path.exists(input_dir):
    os.makedirs(input_dir)
    print(f"Created '{input_dir}' folder.")
    print("Please add .txt files to this folder and re-run the script.")
    exit()

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Step 2: List .txt files in data_input
txt_files = [f for f in os.listdir(input_dir) if f.endswith(".txt")]

if not txt_files:
    print("⚠ No .txt files found in the 'data_input' folder.")
    exit()

# Step 3: Process each file
summary_lines = []

print("\n📄 Processing .txt files...\n")

for file_name in txt_files:
    input_path = os.path.join(input_dir, file_name)
    output_path = os.path.join(output_dir, file_name)

    line_count = 0
    word_count = 0
    processed_lines = []

    with open(input_path, "r") as infile:
        for line in infile:
            if line.strip().startswith("#"):
                continue  # Ignore comment lines
            line_count += 1
            words = line.split()
            word_count += len(words)
            modified_line = line.replace("temp", "permanent")
            processed_lines.append(modified_line)

    with open(output_path, "w") as outfile:
        outfile.writelines(processed_lines)

    # Print to screen
    print(f"{file_name}:")
    print(f"   - Lines (excluding comments): {line_count}")
    print(f"   - Words (excluding comments): {word_count}\n")

    # Save summary data
    summary_lines.append(f"{file_name}\tLines: {line_count}\tWords: {word_count}")

# Step 4: Write summary.txt
summary_path = os.path.join(output_dir, "summary.txt")
with open(summary_path, "w") as summary_file:
    summary_file.write("Summary Report\n")
    summary_file.write("====================\n")
    for line in summary_lines:
        summary_file.write(line + "\n")

print("All files processed.")
print(f"Summary saved to '{summary_path}'\n")
