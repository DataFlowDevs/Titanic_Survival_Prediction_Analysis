from utils import *


def extract(kaggle_url, raw_data_dir):
    print("Extracting data...")
    csv_file = download_data(kaggle_url, raw_data_dir)
    if csv_file:
        return read_csv_file(csv_file)
    return None

def transform(df):
    print("Transforming data...")
    df = rename_column(df)
    df = remove_duplactes(df)
    df = fill_null_values(df)
    df = encode_categories(df)
    return df

def load(df, processed_file_path):
    print("Loading data...")
    create_directory(os.path.dirname(processed_file_path))
    store_preprocessed_data(df, processed_file_path)
if __name__ == "__main__":
    KAGGLE_DATASET_URL = "your_kaggle_dataset_url_here"
    RAW_DATA_DIR = "./datasets/raw_data"
    PROCESSED_FILE_PATH = "./datasets/preprocessed/titanic_preprocessed.csv"

    df_extracted = extract(KAGGLE_DATASET_URL, RAW_DATA_DIR)

    if df_extracted is not None:
        df_transformed = transform(df_extracted)
        load(df_transformed, PROCESSED_FILE_PATH)
        print("ETL Pipeline executed successfully.")
    else:
        print("ETL Pipeline failed due to extraction error.")