import pandas as pd

def load_data(file_path):
    """
    Load CSV file and display basic info
    """
    df = pd.read_csv(file_path)
    print("Dataset Loaded Successfully")
    print("Shape:", df.shape)
    print("Columns:", df.columns.tolist())
    print("\nMissing Values:\n", df.isnull().sum())
    return df


def clean_data(df):
    """
    Remove duplicates and missing values
    """
    df = df.drop_duplicates()
    df = df.dropna()
    return df


# -------- TEST BLOCK --------
if __name__ == "__main__":
    print("Testing data_utils module...")
