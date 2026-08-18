import pandas as pd
import boto3
from datetime import datetime

BUCKET = "bharat-csvstat"   # your S3 bucket
TOP = 5                      # how many top values to show for text columns


def get_first_csv_key(s3, bucket):
    # looks inside input/ and returns the one CSV file sitting there
    # (list_objects_v2 gives back everything under that prefix/folder)
    response = s3.list_objects_v2(Bucket=bucket, Prefix="input/")
    for obj in response.get("Contents", []):
        key = obj["Key"]
        if key.endswith(".csv"):     # only care about actual csv files
            return key
    return None    # no csv found in input/


def main():
    s3 = boto3.client("s3")   # uses the EC2 instance's IAM role automatically, no keys needed

    input_key = get_first_csv_key(s3, BUCKET)
    if input_key is None:
        print("Error: No CSV file found in input/ folder.")
        return

    # s3fs lets pandas read this s3:// path directly, same as a normal file path
    s3_input_path = f"s3://{BUCKET}/{input_key}"
    print(f"Reading file: {s3_input_path}")

    report_lines = []   # every printed line also gets stored here, to upload as the report later

    df = pd.read_csv(s3_input_path)
    print(df)
    report_lines.append(str(df))

    rows, columns = df.shape
    print(f"rows:{rows}")
    print(f"columns:{columns}")
    report_lines.append(f"rows:{rows}")
    report_lines.append(f"columns:{columns}")

    # profile every column
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            column_type = "numeric"
        elif "date" in column.lower():
            column_type = "date"
        else:
            column_type = "text"

        # .isna(): checks each value and asks "is this value missing?"
        # .sum() adds up all the Trues (missing) since True=1, False=0
        missing = df[column].isna().sum()
        missing_percent = (missing / rows) * 100
        print("")
        print(f" Missing: {missing},Missing in which Column: {column},")
        print(f"  Missing Percentage: {missing_percent:}%")
        report_lines.append("")
        report_lines.append(f" Missing: {missing},Missing in which Column: {column},")
        report_lines.append(f"  Missing Percentage: {missing_percent:}%")
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
            report_lines.append(f"  Min: {df[column].min()}")
            report_lines.append(f"  Mean: {df[column].mean():.2f}")
            report_lines.append(f"  Max: {df[column].max()}")

        # top values for text
        if column_type == "text":
            print("  Top values:")
            report_lines.append("  Top values:")
            top_values = df[column].value_counts().head(TOP)
            for value, count in top_values.items():
                print(f"{value}: {count}")
                report_lines.append(f"{value}: {count}")

        # date wala
        if column_type == "date":
            print("  Date column")
            report_lines.append("  Date column")

    # build a unique filename using the current timestamp, so old reports never get overwritten
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename_only = input_key.split("/")[-1]
    output_key = f"output/report_{filename_only}_{timestamp}.txt"

    # join every collected line into one text block and upload it as the report
    s3.put_object(Bucket=BUCKET, Key=output_key, Body="\n".join(report_lines))
    print(f"\nReport uploaded to s3://{BUCKET}/{output_key}")


if __name__ == "__main__":
    main()