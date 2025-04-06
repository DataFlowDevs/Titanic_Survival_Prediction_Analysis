import os
import kagglehub
import shutil
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def is_path_exist(path: str) -> bool:
    return os.path.exists(path)

def create_directory(path: str) -> None:
    #check if path exist
    if is_path_exist(path):
        print(f"The path {path} already exist")
        return "skip"
    os.mkdir(path)


def download_data(url: str, dest_path: str) -> None:
    """
    Download the data from kaggle store is the destination path dir
    """
    if not is_path_exist(dest_path):
        print(f"The path {dest_path} does not exist")
    try:
        # Download latest version
        
        path = kagglehub.dataset_download(url)
        print("Dataset downloaded succesfully")
        print("Path to dataset files:", dest_path)
        file_names = os.listdir(path)
            
        for file_name in file_names:
            shutil.move(os.path.join(path, file_name), dest_path)
        shutil.rmtree(path)
        return "success"
    
    except Exception as e:
        print(f"{e}")


def read_csv_file(csv_file: str):
    df = pd.read_csv(csv_file, header = 1)
    return df

def remove_duplicates(df):
    df = df.drop_duplicates()
    df.drop_duplicates('name', inplace=True)
    return df

def rename_column(df):
    df = df.rename(columns={df.columns[3]: 'name'})
    return df


def fill_null_values(df):

    non_numeric_values = pd.to_numeric(df['age'], errors='coerce')
    df['age'] = non_numeric_values

    mean_age = int(df['age'].mean())
    df['age'] = df['age'].fillna(mean_age)
    
    df['fare'] = pd.to_numeric(df['fare'], errors='coerce')
    mean_fare = int(df['fare'].mean())

    df['fare'] = df['fare'].fillna(mean_fare)
    df['gender'] = df['gender'].fillna("male")

    mode_embark = df['embarked'].mode().iloc[0]
    df['embarked'] = df['embarked'].fillna(mode_embark)


    df['family'] = pd.to_numeric(df['family'], errors='coerce')

    mode_family = df['family'].mode().iloc[0]
    df['family'] = df['family'].fillna(mode_family)
    return df
    
def encode_categories(df):
    labelEconder = LabelEncoder()
    df['encoded_gender'] = labelEconder.fit_transform(df[['gender']])
    df['encoded_embarked'] = labelEconder.fit_transform(df[['embarked']])
    return df


def store_preprocessed_data(df, dest_path):
    df.to_csv(dest_path)

    