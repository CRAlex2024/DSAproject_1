# Code Labs Project

This Code lab processes student data to generate email addresses, separate gender lists, identify names with special characters, calculate name similarities, and shuffle the student list.

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setting Up the Virtual Environment

1. **Create a Virtual Environment**:
    ```bash
    python -m venv myenv
    ```

2. **Activate the Virtual Environment**:
    - On Windows:
      ```bash
      myenv\Scripts\activate
      ```
    - On macOS and Linux:
      ```bash
      source myenv/bin/activate
      ```

3. **Install the Required Libraries**:
    ```bash
    pip install numpy pandas openpyxl tensorflow tensorflow-hub
    ```

## Usage

1. **Place the Excel File**:
   Ensure the `Test files.xlsx` file is in the project root directory.

2. **Run the Main Script**:
    ```bash
    python main.py
    ```

   This will read the data from the Excel file, process it, and generate the required outputs.

## Project Structure

- **main.py**: The main script that orchestrates the data processing.
- **function.py**: Contains helper functions used in the main script.
- **logs.txt**: Log file where the counts of male and female students and names with special characters are recorded.

## Functions Overview

### main.py

- **Import Libraries**: 
  ```python
  import pandas as pd
  import numpy as np
  import re
  import json
  import tensorflow_hub as hub
  from function import generate_email, separate_gender_lists, special_character_names, calculate_similarity, shuffle_and_save
  
- **Load the Tools**:

First, we bring in some tools that will help us with the job. It's like getting your pencils, erasers, and rulers ready before you start working on a project.
 
- ```python

    import pandas as pd
    import numpy as np
    import re
    import json
    import tensorflow_hub as hub
    from function import generate_email, separate_gender_lists, special_character_names, calculate_similarity, shuffle_and_save
- **Read the Student List**:

We read the student list from an Excel file called 'Test files.xlsx'. Think of it like opening your notebook to see all the names written down.
   
-   ```python

    def main():
        df = pd.read_excel('Test files.xlsx')
  
- **Split Names**:

- We split the full names into first names and last names. It's like taking "John, Doe" and turning it into "John" and "Doe".
    
  ```python

    df[['First Name', 'Last Name']] = df['Student Name'].str.split(',', expand=True)
    df['First Name'] = df['First Name'].str.strip()
    df['Last Name'] = df['Last Name'].str.strip()

- **Make Email Addresses**:

- We create email addresses for each student. If we have a student named "John Doe", his email will be something like "jdoe@gmail.com".
    
  ```python

    df['Email'] = df.apply(lambda row: generate_email(row['First Name'], row['Last Name']), axis=1)
  
- **Separate Boys and Girls**:

- We put all the boys in one list and all the girls in another. This is like making two different teams from your class.
    
  ```python
    separate_gender_lists(df)
  
- **Find Special Names**:

- We look for names with special characters (like "Ng'wono") and make a separate list for those. This helps us know which names are a bit unusual.
    
  ```python

    special_character_names(df)
  
- **Check Name Similarities**:

- We check how similar boys' names are to girls' names. This is like seeing if "John" and "Joan" sound alike.
    
  ```python

    males = df[df['Gender'] == 'Male']['First Name'].tolist()
    females = df[df['Gender'] == 'Female']['First Name'].tolist()
    calculate_similarity(males, females)
  
- **Mix Up the List**:

- We shuffle the student list to mix up the order. It’s like shuffling a deck of cards.
    
  ```python
  
    shuffle_and_save(df)
  
- **Save Everything**:

- Finally, we save all the information (including the new email addresses) back into files, so we don't lose any of our work. We save it in two formats, CSV and TSV, which are just ways to organize data in a file.
    
  ```python
  
    df.to_csv('students_with_emails.csv', index=False)
    df.to_csv('students_with_emails.tsv', sep='\t', index=False)

- **Print a Confirmation**:

- We print a message saying "Email addresses generated and files saved." to let us know everything is done.

    ```python
    print("Email addresses generated and files saved.")




- **Main Function**:

  The `main` function is the entry point of the script. It performs the following tasks:
  - Reads the student data from an Excel file.
  - Splits student names into first and last names.
  - Generates email addresses for each student.
  - Separates the students into gender-based lists and logs the counts.
  - Identifies names with special characters and logs them.
  - Prepares lists of male and female names for similarity calculation.
  - Shuffles the student list and saves it in JSON and JSONL formats.
  - Saves the generated email addresses to CSV and TSV files.
  
  ```python
  if __name__ == '__main__':
      main()


  
## function.py

- **Import Libraries**:
    ```python
    import re
    import pandas as pd
    import numpy as np
  
This imports the necessary libraries for regular expressions and data processing.

- **Generate Email**:
    ```python
    def generate_email(first_name, last_name):
        clean_last_name = re.sub(r'\W+', '', last_name).lower()
        return f"{first_name[0].lower()}{clean_last_name}@gmail.com"
  
This function generates a unique email address for each student by taking the first letter of the first name and the entire last name, cleaning it of any non-word characters, and appending @gmail.com.

- **Separate Gender Lists**:
    ```python
    def separate_gender_lists(df):
        males = df[df['Gender'] == 'Male']
        females = df[df['Gender'] == 'Female']
        males.to_csv('male_students.csv', index=False)
        females.to_csv('female_students.csv', index=False)

        with open('logs.txt', 'a') as log_file:
            log_file.write(f"Number of male students: {len(males)}\n")
            log_file.write(f"Number of female students: {len(females)}\n")
This function separates students into male and female lists, saves them to separate CSV files, and logs the counts to logs.txt.

- **Special Character Names**:
    ```python
    def special_character_names(df):
        pattern = re.compile(r"[^\w\s]")
        special_char_names = df[df['Last Name'].apply(lambda x: bool(pattern.search(x)))]
        special_char_names.to_csv('special_char_names.csv', index=False)

        with open('logs.txt', 'a') as log_file:
            log_file.write(f"Special character names:\n{special_char_names.to_string(index=False)}\n")
This function identifies names with special characters, saves them to a CSV file, and logs them to logs.txt.

- **Calculate Similarity**:
    ```python
    def calculate_similarity(male_names, female_names):
        # Placeholder for your similarity calculation logic
        pass
This function is a placeholder for the logic to calculate similarity between male and female names.

- **Shuffle and Save**:
    ```python
    def shuffle_and_save(df):
        shuffled_df = df.sample(frac=1).reset_index(drop=True)
        shuffled_df.to_json('shuffled_students.json', orient='records', lines=False)
        shuffled_df.to_json('shuffled_students.jsonl', orient='records', lines=True)
This function shuffles the DataFrame randomly and saves it in both JSON and JSONL formats.
