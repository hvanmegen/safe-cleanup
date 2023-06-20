# Safe Cleanup

This Python script helps you delete a limited number of files and directories from a specified directory. It is designed to handle various conditions such as slow file deletions and errors during the deletion process.

## Features

- Specify the directory and the number of files/directories to delete.
- Optional verbose mode to display detailed output with a progress bar.
- Handles slow file deletions by waiting and doubling the wait time if necessary.
- Quits if a single file deletion takes more than 30 seconds.
- Gracefully handles KeyboardInterrupt (CTRL-C) to stop the process.
- Exits with an error message if the maximum number of errors is reached.

## Requirements

- Python 3.x
- Python 'tqdm' module

## Installation

1. Ensure you have Python 3.x installed on your system. You can check this by running `python --version` or `python3 --version`.
2. Install the `tqdm` module using pip:

```
pip install tqdm
```

## Usage

Run the script from the command line with the following syntax:

```
python cleanup.py [-v] <directory> <number_of_items>
```

- `-v` or `--verbose`: (Optional) Enable verbose mode for detailed output.
- `<directory>`: The directory path from which you want to delete files and directories.
- `<number_of_items>`: The number of files and directories to delete.


Example:

```
python cleanup.py -v /path/to/directory 10000
```

This command will delete 10000 files/directories from `/path/to/directory` and display detailed output with a progress bar.

## Contributing

To contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push them to your fork.
4. Create a pull request, and it will be reviewed as soon as possible.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
