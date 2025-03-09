#!/usr/bin/env python3
import sys
import pandas as pd

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 datareader.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        df = pd.read_csv(filename)
        print(df)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
