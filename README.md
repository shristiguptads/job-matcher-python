# Job Matcher using Python

I made this project as part of my internship task to learn how data and logic work together in Python.

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

## What I Learned
This project isn't perfect, but it taught me a lot about data cleaning, condition logic, and how to make code actually work.

## Future Improvements

- Add a Streamlit web interface so users can enter their details easily, instead of using the terminal.  
- Use a more advanced matching logic that weights skill importance and considers partial matches.  
- Expand the job dataset — recommendations improve when more job options are available.  
- Add proper error handling to manage missing or invalid data in the CSV file.  
- Include more visualizations (like pie or scatter plots) for deeper insights.
