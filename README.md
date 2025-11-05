# Job Matcher using Python

This project matches users to the most relevant jobs based on their skills, location, and experience.

## How it works
1. User inputs their details.
2. The program compares them with jobs.csv.
3. Matches are ranked using a custom score.
4. Top 3 matches are displayed and saved in matched_results.csv.

## Files
- main.py — source code
- jobs.csv — job database
- matched_results.csv — results generated after running the program

## Requirements
pandas, matplotlib

## How to run
1. Install dependencies:
   pip install -r requirements.txt
2. Run the script:
   python main.py

## Output Example
Displays top job matches and a bar graph of match scores.