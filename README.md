# codelab 
## Student Email Generation and Logging the number of male and female students

This project generates unique email addresses for students based on their names and stores the results in various file formats. It also handles special character detection in names and shuffles the data for different purposes. It also logs the counts of all male students and female students.

### Libraries and tools used 
- Python 3.12
- Pandas
- Logging module
- Google API key

 ## Features
- Generate email addresses in the format: `first_initial_lastname@gmail.com`
- Ensure email uniqueness.
- Detect and log names containing special characters.
- Separate and log counts of male and female students.
- - Shuffle the data and save it in JSONL format.
- Compare name similarity using LaBSE and save results in a JSON file.
- Save results in multiple formats: CSV, TSV, JSON, JSONL.

  ## Files and Directories
- **`main.py`**: Main program logic to load data, generate email addresses, detect special characters, and shuffle data.
- **`functions.py`**: Contains helper functions for email generation, special character detection, and file saving.
- **`constraints.py`**: Holds project constraints, including the similarity threshold for LaBSE.
- **`student_logs.log`**: Log file that records computations and results.
- **`input_files/`**: Folder containing the input Excel files.
- **`output_files/`**: Folder where the output CSV, TSV, JSON, and JSONL files are stored.

   ## **Project Structure:**

```
 student-email-generator/
│
├── README.md
├── constraints.py
├── functions.py
├── main.py
├── student_logs.log
│
├── input_files/
│   └── Test Files.xlsx (place your Excel file here)
│
└── output_files/
    ├── students_a.csv
    ├── students_a.tsv
    ├── students_b.csv
    ├── students_b.tsv
    ├── shuffled_students_a.jsonl
    └── shuffled_students_b.jsonl
```
