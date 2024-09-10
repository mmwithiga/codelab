from spyder_kernels.utils.lazymodules import pandas


import pandas as pd
from functions import generate_email_unique, has_special_characters, save_as_csv_and_tsv, shuffle_and_save
import logging

# Main program logic

# Load File_A and File_B from the Excel sheet
file_path = 'input_files/Test Files.xlsx'
df_a = pd.read_excel(file_path, sheet_name='File_A')
df_b = pd.read_excel(file_path, sheet_name='File_B')

# Initialize dictionary for unique email storage
emails = {}

# Step 1: Generate email addresses and ensure they are unique
df_a['Email Address'] = df_a['Student Name'].apply(lambda x: generate_email_unique(x, emails))
df_b['Email Address'] = df_b['Student Name'].apply(lambda x: generate_email_unique(x, emails))

# Step 2: Save DataFrames as CSV and TSV
save_as_csv_and_tsv(df_a, 'students_a')
save_as_csv_and_tsv(df_b, 'students_b')

# Step 3: Separate male and female students
male_students_a = df_a[df_a['Gender'] == 'M']
female_students_a = df_a[df_a['Gender'] == 'F']

male_students_b = df_b[df_b['Gender'] == 'M']
female_students_b = df_b[df_b['Gender'] == 'F']

# Log the counts of male and female students
logging.info(f"Number of male students in File_A: {len(male_students_a)}")
logging.info(f"Number of female students in File_A: {len(female_students_a)}")
logging.info(f"Number of male students in File_B: {len(male_students_b)}")
logging.info(f"Number of female students in File_B: {len(female_students_b)}")

# Step 4: Detect and log names with special characters
special_char_names_a = df_a[df_a['Student Name'].apply(has_special_characters)]
special_char_names_b = df_b[df_b['Student Name'].apply(has_special_characters)]

logging.info(f"Students with special characters in File_A: {special_char_names_a['Student Name'].tolist()}")
logging.info(f"Students with special characters in File_B: {special_char_names_b['Student Name'].tolist()}")

# Step 5: Shuffle and save the data
shuffle_and_save(df_a, 'shuffled_students_a')
shuffle_and_save(df_b, 'shuffled_students_b')
