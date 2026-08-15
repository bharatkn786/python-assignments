# CSV Stat Profiler — S3 + EC2

A CSV profiling tool that runs on an EC2 instance, reads its input CSV directly from an S3 bucket, and writes a profiling report back to S3 — using an IAM instance profile for authentication (no access keys stored on the instance).


## Overview

`csvstat.py` runs with no arguments and automatically takes its input straight from the S3 bucket — you don't pass a filename or path. On each run, it:

1. Automatically finds the CSV file sitting in `s3://<bucket>/input/`
2. Reads it directly from S3 using `pandas` + `s3fs`
3. Profiles every column — row/column counts, missing values, min/mean/max for numeric columns, top values for text columns, and flags date columns
4. Prints the report to the terminal
5. Uploads the same report as a timestamped `.txt` file to `s3://<bucket>/output/`

> **Note:** No manual input is required — the script automatically pulls the CSV from `s3://<bucket>/input/` on every run. Just keep one CSV file in that folder and run `python csvstat.py`.

## Architecture

```
S3 bucket (input/)  --reads CSV-->  EC2 instance (IAM instance profile attached)  --writes report-->  S3 bucket (output/)
```

## Prerequisites

- An EC2 instance (Amazon Linux 2023 or similar) with SSH access
- An S3 bucket with `input/` and `output/` folders
- An IAM role with scoped S3 permissions, attached to the EC2 instance as an instance profile
- Git installed on the instance
- Python 3.9+ available on the instance



S## 1. Clone the Repository

SSH into your EC2 instance:

<img width="1189" height="243" alt="Screenshot 2026-08-15 111759" src="https://github.com/user-attachments/assets/b0ef84eb-7b33-41b4-94ab-364484c44fc6" />


Then clone the repository:

```bash
git clone https://github.com/bharatkn786/python-assignments.git
cd python-assignments
```

## 2. Create a Virtual Environment and Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

`requirements.txt` contains:

```
pandas
boto3
s3fs
```

> **Note:** Install all dependencies in a single `pip install` command (or from `requirements.txt`) rather than separate commands. Installing `boto3` and `s3fs` separately can cause `botocore` version conflicts, since `s3fs` depends on `aiobotocore`, which pins a different `botocore` range than `boto3` does. A single combined install lets pip's resolver pick compatible versions for everything at once.

## 3. Create the S3 Bucket and Folders

From your local machine or the EC2 instance (using credentials with sufficient permissions):

```bash
aws s3 mb s3://bharat-csvstat --region ap-south-1
aws s3api put-object --bucket bharat-csvstat --key input/
aws s3api put-object --bucket bharat-csvstat --key output/
```
<img width="1916" height="678" alt="Screenshot 2026-08-15 111927" src="https://github.com/user-attachments/assets/c91c1beb-2e70-4a01-a336-a4cc88604f19" />

Upload a sample CSV to the `input/` folder:

```bash
aws s3 cp sample_data.csv s3://bharat-csvstat/input/
```

> Keep only **one** CSV file in `input/` at a time — the script automatically picks up the first `.csv` file it finds there.

## 4. Set Up the IAM Instance Profile

### Create a scoped IAM policy

In the IAM console, create a policy that grants only the permissions needed — no broader access:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "s3:ListBucket",
      "Resource": "arn:aws:s3:::bharat-csvstat"
    },
    {
      "Effect": "Allow",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::bharat-csvstat/input/*"
    },
    {
      "Effect": "Allow",
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::bharat-csvstat/output/*"
    }
  ]
}
```
<img width="1908" height="672" alt="Screenshot 2026-08-15 112429" src="https://github.com/user-attachments/assets/e654d09c-2387-4c15-ba0c-86eb17936795" />


### Create the IAM role

1. IAM → Roles → Create Role
2. Trusted entity: **EC2**
3. Attach the policy created above
4. Name the role (e.g. `CSVStatEC2Role`)

### Attach the role to the EC2 instance

1. EC2 Console → select the instance
2. Actions → Security → Modify IAM role
3. Select `CSVStatEC2Role` and save

No access keys are ever entered on the instance. Verify the role is active:

```bash
aws sts get-caller-identity
```


Expected output shows an **assumed-role** ARN, not an IAM user:

<img width="746" height="112" alt="Screenshot 2026-08-15 112540" src="https://github.com/user-attachments/assets/32979fb3-7913-4348-8dbd-c4c78ac43255" />



> If any `~/.aws/credentials` file exists on the instance with hardcoded keys, remove or rename it so the SDK falls back to the instance role:
> ```bash
> mv ~/.aws/credentials ~/.aws/credentials.backup
> ```

## 5. Configure the Bucket Name in the Script

Open `csvstat.py` and set the bucket name at the top:

```python
BUCKET = "bharat-csvstat"   # your S3 bucket name
TOP = 5                      # number of top values shown for text columns
```

## 6. Run the Script

```bash
source venv/bin/activate
python csvstat.py
```

The script requires no arguments — it automatically finds the CSV in `input/`, profiles it, prints the report, and uploads it to `output/`.

Example output:

<img width="490" height="884" alt="image" src="https://github.com/user-attachments/assets/5071231a-32ed-41d4-9c31-1924b8b0ca1a" />

Report uploaded to s3://bharat-csvstat/output/report_sample_data.csv_20260814_205807.txt
```

## 7. Verify the Report

```bash
aws s3 ls s3://bharat-csvstat/output/
```

You should see a new `report_<filename>_<timestamp>.txt` file for each run.

## What the Script Does — Column by Column

For every column in the CSV:

| Column type | Detection | Stats reported |
|---|---|---|
| Numeric | `pandas` numeric dtype | Min, Mean, Max |
| Date | Column name contains `"date"` | Flagged as a date column |
| Text | Anything else | Top 5 most frequent values (configurable via `TOP`) |

Every column also reports its missing-value count and missing-value percentage.

## Troubleshooting

### `AccessDenied` on `s3:ListAllMyBuckets` or `s3:DeleteObject`

This is expected behavior, not a bug. The IAM policy above only grants `GetObject`, `PutObject`, and `ListBucket` — nothing broader. If you need to delete an object from `input/` or `output/`, do it from a machine using a full-permission identity (e.g. your local AWS CLI with an IAM user), not from the EC2 instance itself.

### `No CSV file found in input/ folder`

Confirm exactly one `.csv` file is present:

```bash
aws s3 ls s3://bharat-csvstat/input/
```

### `pip` dependency conflicts between `boto3`, `botocore`, and `s3fs`

Always install `pandas`, `boto3`, and `s3fs` together in one command (or via `requirements.txt`), never in separate `pip install` calls. If a conflict already occurred, rebuild the virtual environment from scratch:

```bash
deactivate
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip check
```

`pip check` should print no output if all dependencies are compatible.

## Project Structure

```
week1-Challenge/
│
├── venv/
├── csvstat.py
├── requirements.txt
├── data.csv
├── sql/
└── README.md
```

## Security Notes

- No AWS access keys are stored on the EC2 instance; all access is via the IAM instance profile.
- The IAM policy is scoped to a single bucket and only the three actions required (`GetObject`, `PutObject`, `ListBucket`).
- Never commit AWS access keys or secret keys to this repository.
