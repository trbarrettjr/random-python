#!/usr/bin/python3
import os
import json
import hashlib

def main():
    # files = os.listdir()
    # for file in files:
    #     if not os.path.isfile(file): # Removes directories
    #         files.remove(file)
    #     if file.startswith('.'): # Removes hidden files
    #         files.remove(file)

    files = [f for f in os.listdir() if os.path.isfile(f) and not f.startswith('.')]

    # Pick either function above.  I like the second one as it is an anonymous function that is
    # easy to read.  But the first one is easier for newer programmers to follow as each line will
    # do something.

    # They could also do something like this below.
    # for file in files:
    #     if not os.path.isfile(file) and file.startswith('.'):
    #         files.remove(file)

    table_of_contents = []

    for file in files:
        print(f'Processing ... {file}')
        with open(file, 'rb') as f:
            data = f.read() # need to get the contents of the file to read.

        contents = {
            "filename": f"{file}",
            "md5": f"{hashlib.md5(data).hexdigest()}",
            "sha1": f"{hashlib.sha1(data).hexdigest()}",
            "sha256": f"{hashlib.sha256(data).hexdigest()}"
        }

        table_of_contents.append(contents)

    sorted_toc = sorted(table_of_contents, key=lambda f: f['filename']) # sort the table of contents by 'filename' in the JSON file.

    with open("contents.json", "w") as f:
        json.dump(sorted_toc, f)

    print(f"Done with processing directory.\nOutput: contents.json")        

if __name__ == "__main__":
    main()
