import pandas as pd


def write_parquet_file():
    df = pd.read_csv('//recursion/cousera/clients.csv')
    df.to_parquet('/Users/christopher/PycharmProjects/PersonalProjects/recursion/cousera/clients3.parquet')

write_parquet_file()