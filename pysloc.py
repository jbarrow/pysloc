import argparse
import os
from tabulate import tabulate

def count_sloc(filename):
    with open(filename, "r") as file:
        lines = [line.rstrip() for line in file]
        lines = [line for line in lines if line]
        return len(lines)

def traverse(directory, exts):
    f = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            for ext in exts:
                if file.endswith("."+ext):
                    if file == "pysloc.py":
                        continue
                    f.append((root + "/" + file, count_sloc(root + "/" + file)))
    return f

def tabulate_files(files):
    total = sum(list(zip(*files))[1])
    files.extend([("\n", ""), ("Total: ", total)])
    print("\n",tabulate(files, headers=["Filename", "SLOC"]), "\n")

if __name__ == '__main__':
    # Register the argument parser
    parser = argparse.ArgumentParser(description='Count the source lines\
        of code in a given project')
    parser.add_argument('--dir', dest='dir', required=True,
        help='The top level directory for your project')
    parser.add_argument('--exts', dest='exts', required=True,
        help='A comma-separated list of file extensions to use.')
    args = parser.parse_args()

    if args.exts != None:
        exts = args.exts.strip().strip(",")
        exts = [ext.strip(".") for ext in exts.split(",")]
    else:
        exts = None

    files = traverse(args.dir, exts)
    tabulate_files(files)
