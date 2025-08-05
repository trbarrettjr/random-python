#!/usr/bin/python3
import sys
import json

def convert(text):
    text = text.strip()
    blocks  = text.split('\n\n')
    entries = []
    for block in blocks:
        entry = {}
        key = None
        for item in block.split('\n'):
            if ":" in item:
                key, value = item.split(':', 1)
                if key not in entry:
                    entry[key.strip()] = value.strip()
                else:
                    if not isinstance(entry[key], list):
                        entry[key] = [entry[key]]
                    if value == '':
                        continue
                    entry[key].append(value.strip())
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
