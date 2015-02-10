import argparse

if __name__ == '__main__':
    # Register the argument parser
    parser = argparse.ArgumentParser(description='Count the source lines\
        of code in a given project')
    parser.add_argument('--dir', dest='dir', required=True,
        help='The top level directory for your project')
    parser.add_argument('--exts', dest='exts', help='A comma-separated \
        list of file extensions to use.')
