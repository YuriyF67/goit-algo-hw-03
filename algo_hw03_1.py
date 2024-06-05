import os
import shutil
import argparse


def sort_files(src_dir, dest_dir):
    try:
        os.makedirs(dest_dir, exist_ok=True)
        for item in os.listdir(src_dir):
            src_path = os.path.join(src_dir, item)
            if os.path.isdir(src_path):
                sort_files(src_path, os.path.join(dest_dir, item))
            else:
                ext = os.path.splitext(item)[1][1:].lower()
                dest_ext_dir = os.path.join(dest_dir, ext)
                os.makedirs(dest_ext_dir, exist_ok=True)
                shutil.copy2(src_path, dest_ext_dir)
    except Exception as e:
        print(f"Error: {e}")


def main():
    parser = argparse.ArgumentParser(
        description="Recursive copy files and sorting by extension."
    )
    parser.add_argument("src_dir", help="Path to source dir")
    parser.add_argument(
        "dest_dir",
        nargs="?",
        default="dst",
        help="Path to destination dir (default: 'dst')",
    )
    args = parser.parse_args()
    sort_files(args.src_dir, args.dest_dir)


if __name__ == "__main__":
    main()
