import argparse
from collections import defaultdict
import csv



def find_neighbors(file_path):

    neighbors = defaultdict(list)

    with open(file_path, 'r', newline='', encoding='UTF-8') as csv_file:
        reader = csv.reader(csv_file)

        for cur, node_list in enumerate(reader, 1):
            neighbors[cur] = [i for i, node in enumerate(node_list, 1) if node]

        return neighbors

def parse_args():
    parser = argparse.ArgumentParser(description='find neighbors')
    parser.add_argument('file_path', type=str, help='absolute path')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    ans = find_neighbors(args.file_path)
    for node, neighbors in ans.items():
        print(f"{node}: {', '.join(map(str, neighbors))}")
