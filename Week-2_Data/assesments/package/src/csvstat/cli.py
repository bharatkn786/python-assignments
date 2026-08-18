from .main import (
    read_csv,
    get_shape,
    get_column_type,
    get_missing_count,
    get_missing_percentage,
    get_numeric_statistics,
    get_top_values,
)

def main():

    parser = argparse.ArgumentParser(
        description="Analyze CSV files"
    )

    parser.add_argument(
        "file",
        nargs="?",
        help="CSV file to analyze"
    )

    parser.add_argument(
        "--top",
        type=int,
        default=5
    )

    args = parser.parse_args()

    if args.file is None:
        print("Error: Please provide a CSV file.")
        return

    try:
        df = read_csv(args.file)

    except FileNotFoundError:
        print(f"Error: File {args.file} was not found.")
        return

    rows, columns = get_shape(df)

    print(f"Rows: {rows}")
    print(f"Columns: {columns}")

    for column in df.columns:

        column_type = get_column_type(df, column)

        missing = get_missing_count(df, column)

        missing_percentage = get_missing_percentage(
            df,
            column
        )

        print(f"\nColumn: {column}")
        print(f"Type: {column_type}")
        print(f"Missing: {missing}")
        print(
            f"Missing Percentage: "
            f"{missing_percentage:.2f}%"
        )

        if column_type == "numeric":

            stats = get_numeric_statistics(
                df,
                column
            )

            print(f"Min: {stats['min']}")
            print(f"Mean: {stats['mean']:.2f}")
            print(f"Max: {stats['max']}")

        elif column_type == "text":

            print("Top values:")

            top_values = get_top_values(
                df,
                column,
                args.top
            )

            for value, count in top_values.items():
                print(f"  {value}: {count}")


if __name__ == "__main__":
    main()