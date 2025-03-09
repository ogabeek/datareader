#!/usr/bin/env python3
import sys
import pandas as pd
from ydata_profiling import ProfileReport
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 datareader.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        df = pd.read_csv(filename)
        print(df)
        profile = ProfileReport(df, title="Data Analysis Report", explorative=True)

        # Save the report to an HTML file
        output_file = "report.html"
        profile.to_file(output_file)

        # Generate repor message 
        abs_path = os.path.abspath(output_file)
        print(f"Profile report generated! Open file://{abs_path} in your browser to view it.")
        
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        sys.exit(1)
        
    

if __name__ == "__main__":
    main()
