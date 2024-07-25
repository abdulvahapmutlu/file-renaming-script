# File Renaming Script

This repository contains a simple Python script to rename files in a specified directory. It can be particularly useful for organizing datasets for machine learning and deep learning projects.

## Overview

This script is designed to rename all files within a specified directory in a sequential order. It is particularly useful for organizing and standardizing file names in a directory, such as a collection of images or documents.

## Features

- Renames all files in a specified directory.
- Maintains the original file extensions.
- Provides clear logging of old and new file names.
- Handles errors gracefully.

## Requirements

- Python 3.x

## Usage

1. **Clone the repository** (if applicable):

    ```
    git clone https://github.com/abdulvahapmutlu/file-renaming-script.git
    cd filerenamer
    ```

2. **Install necessary dependencies** (if any):

    This script does not require any external dependencies beyond the Python standard library.

3. **Modify the script to specify the directory path**:

    Open the `rename_files.py` file and update the `directory_path` variable to the path of the directory you want to rename files in.

    ```python
    directory_path = "path/to/your/directory"
    ```

4. **Run the script**:

    ```
    python rename_files.py
    ```

## Example

Assuming your directory contains the following files:

```
/path/to/your/directory/
├── image1.png
├── image2.png
├── doc1.txt
├── doc2.txt
```

After running the script, the directory will contain:

```
/path/to/your/directory/
├── images_1.png
├── images_2.png
├── images_3.txt
├── images_4.txt
```

## Error Handling

The script includes basic error handling to catch and display any issues that arise during execution, such as invalid directory paths or permission errors.

## Contributions

Contributions are welcome! If you have suggestions for improvements or encounter any issues, please feel free to create a pull request or open an issue in the repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
