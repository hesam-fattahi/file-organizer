# File Organizer

## Overview

The **File Organizer** is a Python script that organizes files in a specified directory into categorized folders based on their file extensions. This helps keep your directories tidy and makes it easier to find files.

## Features

- Categorizes files into predefined categories such as Documents, Pictures, Music, Videos, etc.
- Creates category folders if they do not exist.
- Moves files to the appropriate category folders.
- Handles files with spaces in their names.
- Provides error handling for common issues.

## Categories

The script categorizes files into the following categories:

- **Compressed**: `.zip`, `.rar`, `.7z`, `.tar`, `.gz`, `.bz2`
- **Documents**: `.pdf`, `.doc`, `.docx`, `.txt`, `.xls`, `.xlsx`, `.ppt`, `.pptx`, `.odt`, `.ods`, `.odp`, `.rtf`
- **Music**: `.mp3`, `.wav`, `.flac`, `.aac`, `.ogg`, `.wma`, `.m4a`
- **Programs**: `.exe`, `.msi`, `.bat`, `.sh`, `.deb`, `.rpm`, `.pkg`, `.dmg`
- **Videos**: `.mp4`, `.avi`, `.mkv`, `.mov`, `.wmv`, `.flv`, `.webm`
- **Pictures**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.svg`, `.webp`
- **Others**: Any file that does not match the above categories

## Installation

No additional dependencies are required as the script uses Python's standard libraries. Ensure you have Python installed on your system.

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/file-organizer.git
   cd file-organizer
   ```

2. **Create a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

## Usage

To organize files in a specified directory, run the script with the directory path as an argument:

```bash
python file_organizer.py "/path/to/directory"
```

To organize files in the current directory, simply run:

```bash
python file_organizer.py
```

## Example

Organize files in the Downloads folder (replace `<username>` with your actual username)::

```bash
python file_organizer.py "C:/Users/<username>/Downloads"

```

## Error Handling

The script includes error handling for common issues such as permission errors and file conflicts. If an error occurs while moving a file, the script will print an error message and continue processing the remaining files.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
