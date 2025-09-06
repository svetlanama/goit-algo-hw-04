
import argparse
import shutil
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Recursively copies files from a source directory to a destination directory, sorting them into subdirectories based on their file extensions.")
    parser.add_argument("source", type=Path, help="Path to the source directory.")
    parser.add_argument("--destination", type=Path, default=Path("dist"), help="Path to the destination directory (defaults to 'dist').")

    args = parser.parse_args()

    source_dir = args.source
    destination_dir = args.destination

    if not source_dir.exists():
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return

    if not source_dir.is_dir():
        print(f"Error: Source path '{source_dir}' is not a directory.")
        return

    # Ensure destination directory exists
    destination_dir.mkdir(parents=True, exist_ok=True)

    print(f"Copying files from '{source_dir}' to '{destination_dir}'...")

    copy_files_recursively(source_dir, destination_dir)

def copy_files_recursively(source_path: Path, destination_path: Path):
    for item in source_path.iterdir():
        if item.is_dir():
            copy_files_recursively(item, destination_path)
        elif item.is_file():
            try:
                extension = item.suffix.lower().lstrip('.')  # Get file extension without dot
                if not extension:  # Handle files without extension
                    extension = "no_extension"

                target_dir = destination_path / extension
                target_dir.mkdir(parents=True, exist_ok=True)
                shutil.copy2(item, target_dir / item.name)
                print(f"Copied '{item}' to '{target_dir / item.name}'")
            except shutil.Error as e:
                print(f"Error copying file '{item}': {e}")
            except OSError as e:
                print(f"OS Error with file '{item}': {e}")


if __name__ == "__main__":
    main() 