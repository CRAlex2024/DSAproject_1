import re
import pandas as pd
import numpy as np


def generate_email(first_name, last_name):
    clean_last_name = re.sub(r'\W+', '', last_name).lower()
    return f"{first_name[0].lower()}{clean_last_name}@gmail.com"


def separate_gender_lists(df):
    males = df[df['Gender'] == 'Male']
    females = df[df['Gender'] == 'Female']
    males.to_csv('male_students.csv', index=False)
    females.to_csv('female_students.csv', index=False)

    with open('logs.txt', 'a') as log_file:
        log_file.write(f"Number of male students: {len(males)}\n")
        log_file.write(f"Number of female students: {len(females)}\n")


def special_character_names(df):
    pattern = re.compile(r"[^\w\s]")
    special_char_names = df[df['Last Name'].apply(lambda x: bool(pattern.search(x)))]
    special_char_names.to_csv('special_char_names.csv', index=False)

    with open('logs.txt', 'a') as log_file:
        log_file.write(f"Special character names:\n{special_char_names.to_string(index=False)}\n")


def calculate_similarity(male_names, female_names):
    # Placeholder for your similarity calculation logic
    pass


def shuffle_and_save(df):
    shuffled_df = df.sample(frac=1).reset_index(drop=True)
    shuffled_df.to_json('shuffled_students.json', orient='records', lines=False)
    shuffled_df.to_json('shuffled_students.jsonl', orient='records', lines=True)
