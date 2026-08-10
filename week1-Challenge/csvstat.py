import argparse
import pandas as pd


import sys

parser=argparse.ArgumentParser()

# Path to the CSV file"
parser.add_argument("file",nargs="?")       # here nargs means the file is optional  (if file is not provided thn it will give NONE)  
parser.add_argument("--top",type=int,default=5)

args=parser.parse_args()


# if the csv file is not provided
if args.file is None:
    print("Error: Please provide a CSV file.")
    sys.exit(1)

try:
    df = pd.read_csv(args.file)
    print(df)
except FileNotFoundError:
    print(f"Error: File {args.file} was not found.")
    sys.exit(1)
    

rows, columns = df.shape
print(f"rows:{rows}")
print(f"columns:{columns}")



#profile every column
for column in df.columns:
    if pd.api.types.is_numeric_dtype(df[column]):
        column_type = "numeric"
        
    elif "date" in column.lower():
        column_type = "date"
    else:
        column_type = "text"
    # print(f"{column}:{column_type}")
        

#missing columns
# .isna():checks each value and asks:   # Is this value missing?
# .sum() adds all the output from the .isna
#  (it gives true or false and it takes it as the binary so true:1 and false=0)


    missing=df[column].isna().sum()         
    missing_percent=(missing/rows)*100

    print("\n")
    print(f" Missing: {missing},Missing in which Column: {column},")
    print(f"  Missing Percentage: {missing_percent:}%")


    # Take the current column
    #         ↓
    # Find empty/missing values
    #         ↓
    # Count them
    #         ↓
    # Store the count in `missing`

    # Numeric statistics
    if column_type == "numeric":
        print(f"  Min: {df[column].min()}")
        print(f"  Mean: {df[column].mean():.2f}")
        print(f"  Max: {df[column].max()}")


        #top values for text
    if column_type == "text":
        print("  Top values:")

        top_values = df[column].value_counts().head(args.top)

        for value, count in top_values.items():
            print(f"{value}: {count}")



    # date wala
    if column_type == "date":
        print("  Date column")