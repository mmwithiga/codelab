import re
import pandas as pd
import logging

# Initialize logging configuration
logging.basicConfig(filename='student_logs.log', level=logging.INFO)

# Function to generate an email address from a student name
def generate_email(name):
    parts = name.split()
    if len(parts) == 2:
        email = f"{parts[0][0]}{parts[1]}@gmail.com".lower()
    else:
        email = f"{parts[0][0]}{parts[-1]}@gmail.com".lower()
    return email

# Ensure email addresses are unique
def generate_email_unique(name, emails):
    base_email = generate_email(name)
    if base_email not in emails:
        emails[base_email] = 1
        return base_email
    else:
        count = emails[base_email] + 1
        emails[base_email] = count
        return f"{base_email.split('@')[0]}{count}@gmail.com"

# Special character detection in names
def has_special_characters(name):
    return bool(re.search(r"[^\w\s]", name))

# Function to save DataFrame as CSV and TSV
def save_as_csv_and_tsv(df, file_name):
    df.to_csv(f'output_files/{file_name}.csv', index=False)
    df.to_csv(f'output_files/{file_name}.tsv', sep='\t', index=False)

# Shuffle DataFrame and save it as JSON
def shuffle_and_save(df, file_name):
    shuffled_df = df.sample(frac=1).reset_index(drop=True)
    shuffled_df.to_json(f'output_files/{file_name}.json', orient='records', lines=True)
