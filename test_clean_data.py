import pandas as pd
from clean_data import cleanse_data

def test_cleanse_data():
    # Cleanse the data
    cleanse_data("raw_data.csv", "cleaned_data.csv")
    
    # Read the cleansed data
    df = pd.read_csv("cleaned_data.csv")
    
    # Example test cases
    # Check if there are any missing values
    assert df.isnull().sum().sum() == 0, "There are missing values"
    # Check if all column names are lowercase
    assert all(col.islower() for col in df.columns), "Not all column names are lowercase"
    # Check if there are no duplicate rows
    assert df.duplicated().sum() == 0, "There are duplicate rows"

    print("All tests passed!")

if __name__ == "__main__":
    test_cleanse_data()
