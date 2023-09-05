# Student Records Management System

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [Contributing](#contributing)
- [Acknowledgement](#acknowledgement)

## Overview

The Student Records Management System is a simple Python program that allows users to manage student records. It provides functionality to input, view, delete, and search for student data. This system is designed to help educational institutions maintain student information efficiently.

## Features

- Input new student records, including name, class, section, and admission number.
- View existing student records in a tabular format.
- Delete student records based on name and admission number.
- Search for student records by admission number or name and class.

## Getting Started

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/jayadityadev/StudentRecordsManagementSystem.git
   ```

2. Install the required dependencies:

    ```bash
   pip install -r requirements.txt
   ```

## Usage

`A sample 'student.txt' is provided in the repository with prefilled data. You can use the given text file, or else the program will itself create a new 'student.txt' if the same is not found in the working directory.`

#### Run the program

```bash
python main.py
```

#### Adding New Student Records

1. Run the program and select the "Input New Data" option.
2. Enter the number of students you want to add.
3. Fill in the details for each student (Name, Class, Section).
4. The system will automatically generate an admission number.

#### Viewing Student Records

1. Run the program and select the "Read Existing Data" option.
2. Existing student records will be displayed in a tabular format.

#### Deleting Student Records

1. Run the program and select the "Delete Old Data" option.
2. Enter the name and admission number of the student you want to delete.
3. Confirm the deletion when prompted.

#### Searching for Student Records

1. Run the program and select the "Search Data" option.
2. Choose the search method (by admission number or name and class).
3. Enter the required details to search for a student.

## Contributing

Contributions are welcome! If you would like to improve this program, please follow these steps:

1. Fork the repository.
   
3. Create a new branch for your feature or bugfix:
   
   ```bash
   git checkout -b new-feature.
   ```
   
4. Make your changes and commit them (ensure they are well documented):
   
    ```bash
    git commit -m 'Add new feature'.
   ```
    
6. Push to the branch:
   
    ```bash
    git push origin new-feature
   ```
    
8. Create a pull request from your fork's branch to the main repository's main branch.

## Acknowledgement

Thank you for using Student Records Management System! If you have any feedback or suggestions, feel free to open an issue on this repository.
