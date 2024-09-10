import os
import shutil
import argparse

# Define file categories and their corresponding extensions
FILE_CATEGORIES = {
    "Compressed": [".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".ods", ".odp", ".rtf"],
    "Music": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".wma", ".m4a"],
    "Programs": [".exe", ".msi", ".bat", ".sh", ".deb", ".rpm", ".pkg", ".dmg"],
    "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"],
    "Pictures": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],
    "Others": []
}

# Create a reverse lookup dictionary for file extensions
EXTENSION_TO_CATEGORY = {ext: category for category, extensions in FILE_CATEGORIES.items() for ext in extensions}

def create_category_folder(directory_path, category):
    """Create category folder if it doesn't exist."""
    category_folder_path = os.path.join(directory_path, category)
    if not os.path.exists(category_folder_path):
        os.makedirs(category_folder_path)
    return category_folder_path

def move_file_to_category(file_path, category_folder_path):
    """Move file to the appropriate category folder."""
    try:
        shutil.move(file_path, os.path.join(category_folder_path, os.path.basename(file_path)))
    except shutil.Error as e:
        print(f"Error moving file {os.path.basename(file_path)}: {e}")

def organize_files(directory_path):
    """Organize files in the specified directory into categories."""
    try:
        items_in_directory = os.listdir(directory_path)
        
        for item in items_in_directory:
            item_path = os.path.join(directory_path, item)

            if os.path.isfile(item_path):
                file_extension = os.path.splitext(item)[1].lower()
                category = EXTENSION_TO_CATEGORY.get(file_extension, "Others")
                category_folder_path = create_category_folder(directory_path, category)
                move_file_to_category(item_path, category_folder_path)

            else:
                print(f"Skipping directory: {item}")

        print("Your files have been successfully organized.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organize files in a specified directory.")
    parser.add_argument("directory", nargs='?', default=os.getcwd(), help="The directory to organize (default: current directory)")
    args = parser.parse_args()

    organize_files(args.directory)
