import argparse
import os
import json

# From https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python/51991554#51991554
def fs_tree_to_dict(path_):
    file_token = ''
    for root, dirs, files in os.walk(path_):
        tree = {d: fs_tree_to_dict(os.path.join(root, d)) for d in dirs}
        tree.update({f: file_token for f in files})
        return tree  # note we discontinue iteration trough os.walk

def argumentParserBuilder():
    parser = argparse.ArgumentParser(
        description='directoryScan - A tool to scan directories'
    )
    parser.add_argument(
        'path',
        help='The root path to scan.',
    )
    return parser

if __name__ == "__main__":
    parser = argumentParserBuilder()
    args = parser.parse_args()
    print(json.dumps(fs_tree_to_dict(args.path)))
