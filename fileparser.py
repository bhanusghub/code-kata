import json

def parse_fixed_width_file(input_filename, output_filename, offsets):
    with open(input_filename, 'r', encoding='windows-1252') as infile, open(output_filename, 'w', encoding='utf-8') as outfile:
        for line in infile:
            parsed_data = []
            start = 0  # Start index for each field
            for width in offsets:
                end = start + int(width)
                # Extract the substring for each field and strip trailing spaces
                parsed_data.append(line[start:end].strip())
                start = end  # Move start to the end of the current field
            
            # Join parsed fields with a comma for CSV format
            outfile.write(",".join(parsed_data) + "\n")

if __name__ == "__main__":
    # Read the specifications from the JSON file
    with open('code-kata/spec.json') as f:
        spec = json.load(f)
    
    offsets = list(map(int, spec["Offsets"]))  # Convert offsets to integers
    parse_fixed_width_file("fixed_width.txt", "output.csv", offsets)