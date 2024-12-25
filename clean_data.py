import pandas as pd

def cleanse_data(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)
    
    # Example cleansing steps
    # Remove rows with missing values
    df.dropna(inplace=True)
    # Convert all column names to lowercase
    df.columns = [col.lower() for col in df.columns]
    # Remove duplicate rows
    df.drop_duplicates(inplace=True)
    
    # Save the cleaned data to a new CSV file
    df.to_csv(output_file, index=False)
    print("Data cleansed and saved to", output_file)

if __name__ == "__main__":
    cleanse_data("raw_data.csv", "cleaned_data.csv")
