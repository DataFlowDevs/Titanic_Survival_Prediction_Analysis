
from utils import *

raw_data_dest = './datasets/raw_data/'
staged_processed_data_file = './datasets/preprocessed_dataset/stage_data.csv' 

if __name__ =="__main__":
    download_data("sakshisatre/titanic-dataset", raw_data_dest)
    df = read_csv_file('./datasets/raw_data/The Titanic dataset.csv')
    df = rename_column(df)
    df = remove_duplactes(df)
    df = fill_null_values(df)
    df = encode_categories(df)
    store_preprocessed_data(df, staged_processed_data_file)

    # print(df.head(10))