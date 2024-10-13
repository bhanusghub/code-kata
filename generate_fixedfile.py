import json
import random
import string


def gen_string(length):
    """To generate a random string"""
    useletters = string.ascii_letters  # a-zA-Z
    return ''.join(random.choice(useletters) for _ in range(length))

def gen_number(length):
    """To generate a random number"""
    return ''.join(random.choice(string.digits) for _ in range(length))
def generate_file(spec_file, output_file):
    # get information from the spec file
    with open(spec_file, 'r') as f:
        spec = json.load(f)
    
    column_names = spec["ColumnNames"]
    offsets = list(map(int, spec["Offsets"]))
    
    # header
    lines = []
    if spec.get("IncludeHeader", "False") == "True":
        header = ''.join(name.ljust(offset) for name, offset in zip(column_names, offsets))
        lines.append(header)

    # Generate random data based on the offsets
    data = []
    for i in range(10):  # Adjust the range for the number of rows you want
        row = []
        for offset in offsets:
            if random.choice([True, False]):
                # String or number
                row.append(gen_string(offset) if random.random() > 0.5 else gen_number(offset))
            else:
                row.append(" " * offset)  
        data.append(row)

    #  formatting lines
    for row in data:
        line = ''.join(value.ljust(offset) for value, offset in zip(row, offsets))
        lines.append(line)

    # Write to the output file
    with open(output_file, 'w', encoding=spec["FixedWidthEncoding"]) as f:
        for line in lines:
            f.write(line + '\n')

if __name__ == "__main__":
    generate_file('spec.json', 'fixed_width.txt')
