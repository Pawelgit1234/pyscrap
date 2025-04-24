from argparse import ArgumentParser

def main():
    parser = ArgumentParser(description='Pyscrap - tool for website data extraction')
    subparsers = parser.add_subparsers(dest='command', required=True, help='Available commands')

    # === TREE command ===
    tree_parser = subparsers.add_parser('tree', help='Prints a tree structure')
    tree_parser.add_argument('-r', '--recursion', type=int, default=1_000_000,
                             help='Recursion depth (0 = infinite), by default infinite')
    tree_parser.add_argument('-j', '--javascript', action='store_true',
                             help='Enable dynamic JavaScript rendering (e.g. for SPAs)')

    # === GET command ===
    get_parser = subparsers.add_parser('get', help='Fetch data and save to file')
    get_parser.add_argument('-e', action='store_true', help='Extract emails')
    get_parser.add_argument('-p', action='store_true', help='Extract phone numbers')
    get_parser.add_argument('-l', action='store_true', help='Extract other site links (e.g. social media)')
    get_parser.add_argument('-f', action='store_true', help='Download files (PDFs, images, etc.)')
    get_parser.add_argument('-a', action='store_true', help='Extract IP (v4, v6) addresses')
    get_parser.add_argument('-d', action='store_true', help='Extract dates')
    get_parser.add_argument('--json', action='store_true', help='Save output as JSON (data.json)')
    get_parser.add_argument('--csv', action='store_true', help='Save output as CSV (data.csv)')
    get_parser.add_argument('--line', action='store_true', help='Line format for email clients')
    get_parser.add_argument('-r', '--recursion', type=int, default=0,
                             help='Recursion depth (0 = infinite)')
    get_parser.add_argument('-j', '--javascript', action='store_true',
                             help='Enable dynamic JavaScript rendering (e.g. for SPAs)')
    get_parser.add_argument('-o', '--out', type=str,
                             help='Custom output filename')

    # === CLEAN command ===
    clean_parser = subparsers.add_parser('clean', help='Clean and separate extracted data')
    clean_parser.add_argument('-d', action='store_true', help='Split emails by domain')
    clean_parser.add_argument('-c', action='store_true', help='Split phone numbers by country')
    clean_parser.add_argument('-p', action='store_true', help='Split platforms by subdomain')
    clean_parser.add_argument('-r', '--regex', type=str, help='Split by regular expression')

    args = parser.parse_args()

if __name__ == '__main__':
    main()