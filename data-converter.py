#!/usr/bin/python3
import sys
import json

"""The puropse of this is to convert data that is in vertical tabular format and convert it to a JSON format.  With the json format you can then use the csv.DictWriter to make a table that way."""
    
def convert(text):
    text = text.strip()
    blocks  = text.split('\n\n')
    entries = []
    for block in blocks:
        entry = {}
        key = None
        line = block.split('\n')
        for item in line:
            if ":" in item:
                key, value = item.split(':', 1)
                entry[key.strip()] = value.strip()
            else:
                value = item.strip()
                entry[key.strip()] =  entry[key] + ', ' + value.strip()

        entries.append(entry)

    return entries

if __name__ == "__main__":
    if len(sys.argv) == 2:
        fn = sys.argv[1]
    else:
        print(f"Missing Filename!\n{sys.argv[0]} filename")
        sys.exit(1)

    out_fn = fn.replace('txt', 'json')

    print(f"Processing: {fn}")
    print()

    with open(fn, 'r') as f:
        data = convert(f.read())

    with open(out_fn, 'w') as f:
        json.dump(data, f, indent=2)

    print(f"Process complete\nOut file is {out_fn}")
