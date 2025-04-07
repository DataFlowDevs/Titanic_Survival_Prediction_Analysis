from utils import *


def preprocess_data(df):
    print("Cleaning and preprocessing data...")
    df = rename_column(df)
    df = remove_duplicates(df)
    df = fill_null_values(df)
    df = encode_categories(df)
    return df

if __name__ =="__main__":
    RAW_DATA_FILE = '../datasets/raw_data/The Titanic dataset.csv'
    df = read_csv_file(RAW_DATA_FILE)
    preprocess_data(df)
    print(df.head(10))
