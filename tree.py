import os
import sys

def generate_tree(directory=".", indent=""):
    """Generates a tree-like representation of a directory, handling Unicode."""
    try:
        items = os.listdir(directory)
        items.sort()

        for index, item in enumerate(items):
            path = os.path.join(directory, item)
            is_last = index == len(items) - 1

            try:
                # Force UTF-8 encoding for the item name
                item_str = item.encode('utf-8', errors='replace').decode('utf-8')
            except UnicodeEncodeError:
                item_str = item.encode('utf-8', errors='replace').decode('utf-8')

            if os.path.isdir(path):
                print(indent + ("└── " if is_last else "├── ") + item_str + "/")
                new_indent = indent + ("    " if is_last else "│   ")
                generate_tree(path, new_indent)
            else:
                print(indent + ("└── " if is_last else "├── ") + item_str)

    except PermissionError:
        print(indent + "└── (Permission denied)")
    except FileNotFoundError:
        print(indent + "└── (Directory not found)")
    except Exception as e:
        print(indent + f"└── (An error occurred: {e})")

if __name__ == "__main__":
    # Set the standard output to use UTF-8 encoding
    if sys.stdout.encoding != 'UTF-8':
        sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)

    generate_tree()
