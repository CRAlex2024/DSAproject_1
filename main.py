import pandas as pd
import numpy as np
import re
import json
import tensorflow_hub as hub
from function import generate_email, separate_gender_lists, special_character_names, calculate_similarity, \
    shuffle_and_save


def main():
    # Read data
    df = pd.read_excel('Test files.xlsx')

    # Split student names into first and last names
    df[['First Name', 'Last Name']] = df['Student Name'].str.split(',', expand=True)
    df['First Name'] = df['First Name'].str.strip()
    df['Last Name'] = df['Last Name'].str.strip()

    # Generate email addresses
    df['Email'] = df.apply(lambda row: generate_email(row['First Name'], row['Last Name']), axis=1)

    # Separate gender lists
    separate_gender_lists(df)

    # Identify special character names
    special_character_names(df)

    # Calculate similarity
    males = df[df['Gender'] == 'Male']['First Name'].tolist()
    females = df[df['Gender'] == 'Female']['First Name'].tolist()
    calculate_similarity(males, females)

    # Shuffle and save
    shuffle_and_save(df)

    # Save email addresses to CSV and TSV
    df.to_csv('students_with_emails.csv', index=False)
    df.to_csv('students_with_emails.tsv', sep='\t', index=False)

    print("Email addresses generated and files saved.")


if __name__ == '__main__':
    main()
