import argparse
from entry import quick_add


def main():
    parser = argparse.ArgumentParser(
        description="Quickly add an entry to Omnifocus")
    parser.add_argument('raw_entry', type=str)
    args = parser.parse_args()
    quick_add(args.raw_entry)


if __name__ == '__main__':
    main()
