import argparse
import csv


def read_csv_value(file_path, n_row, n_col):
    if n_row < 0 or n_col < 0:
        raise Exception('Negative index')
    n_row -= 1
    n_col -= 1

    with open(file_path, 'r', newline='', encoding='UTF-8') as csv_file:
        reader = csv.reader(csv_file)

        for row, line in enumerate(reader):
            if n_row == row:

                if len(line) < n_col:
                    raise Exception("Column index out of range")
                return line[n_col]

        raise Exception("Row index out of range")


def parse_args():
    parser = argparse.ArgumentParser(description='find  csv cell')
    parser.add_argument('file_path', type=str, help='absolute path')
    parser.add_argument('n_row', type=int)
    parser.add_argument('n_col', type=int)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    ans = read_csv_value(args.file_path, args.n_row, args.n_col)
    print(ans)


