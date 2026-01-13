import pandas as pd
import re

def process_sports_data(input_file, output_file):
    # Load dataset without forcing dtype initially (avoids conversion errors)
    df = pd.read_csv(input_file, keep_default_na=False)

    # Convert birthyear and hpi to numeric (handle errors safely)
    df["birthyear"] = pd.to_numeric(df["birthyear"], errors="coerce").fillna(1600).astype(int)
    df["hpi"] = pd.to_numeric(df["hpi"], errors="coerce").fillna(1.0)  # Set missing hpi to 1.0

    # Remove rows where birthyear is below 1700
    df = df[df["birthyear"] >= 1900]

    # Normalize hpi (divide by 100)
    df["hpi"] = df["hpi"] / 100

    # Clean names (replace "_" and "-" with space)
    df["name"] = df["name"].astype(str).apply(lambda x: re.sub(r"[_-]", " ", x))

    # Save processed data
    df.to_csv(output_file, index=False, encoding="utf-8")

    print(f"✅ Processed file saved as {output_file}")

# Usage
input_file = "persons.csv"
output_file = "processed_persons.csv"
process_sports_data(input_file, output_file)
