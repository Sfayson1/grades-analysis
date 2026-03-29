# Grades Analysis Project

This project is a Python assignment demonstrating how to work with Pandas DataFrames, MultiIndex, grouped statistics, and Matplotlib visualizations.

The program stores a classroom roster, assigns grades for two subjects, calculates the average grade per subject, and displays both the numerical output and a bar chart.

## Features

| Feature | Description |
|---|---|
| **Student ID Printout** | Prints the student ID at program start |
| **Roster** | Stores a classroom roster of 10 students |
| **MultiIndex** | Uses Pandas MultiIndex to organize students and subjects |
| **DataFrame** | Creates a DataFrame containing Math and Science grades |
| **Grouping** | Groups grades by subject and calculates the mean |
| **Visualization** | Displays a vertical bar chart of average grades |
| **Comments** | Code is fully commented for clarity |

## Technologies Used

- Python 3
- Pandas
- Matplotlib

## File Structure

```
grades-analysis/
│
├── grades_analysis.py     # Main Python script
└── README.md              # Project documentation
```

## How to Run the Program

1. Install required libraries:
   ```bash
   pip install pandas matplotlib
   ```

2. Run the script:
   ```bash
   python grades_analysis.py
   ```

3. View results:
   - Terminal output (average grades)
   - Bar chart window (visualization)

## Example Output

**Student ID:** Lisa1234

| Subject | Grade |
|---|---|
| Math | 92.25 |
| Science | 87.00 |
