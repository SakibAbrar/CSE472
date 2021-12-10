import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.impute import SimpleImputer

from mapping import (
    MIN_MAX_ENCODING,
    ONE_HOT_ENCODING,

    DS1_MISSING_VALUE_FILL_MAPPING,
    DS1_ENCODER_MAPPING,
)


def remove_white_space_with_Nan(df):
    return df.replace(r'^\s*$', np.nan, regex=True)


def fill_null_data(df, mapping):
    encoded_df = pd.DataFrame()  # Final encoded df
    headers = df.columns.values  # Headers of the given df

    for column in headers:
        fill_method = mapping.get(column, None)

        if fill_method == None:
            encoded_df[column] = df[column]
        else:
            encoded_df[column] = SimpleImputer(
                strategy=fill_method).fit_transform(df[[column]])[:, 0]

    return encoded_df


def kill_null_data(df):
    pass


def encode_data(df, mapping):
    encoded_df = pd.DataFrame()  # Final encoded df
    headers = df.columns.values  # Headers of the given df

    for column in headers:
        # Get the current column encoding from the mapping
        encoding = mapping.get(column, None)

        if encoding == MIN_MAX_ENCODING:
            encoded_df[column] = preprocessing.MinMaxScaler(
            ).fit_transform(df[[column]].values)

        elif encoding == ONE_HOT_ENCODING:
            unique_data = len(pd.unique(df[column]))
            new_keys = [column + str(idx) for idx in range(1, unique_data)]
            encoded_df[new_keys] = preprocessing.OneHotEncoder(
                drop='first').fit_transform(df[[column]]).toarray()

        elif encoding == None:  # Keep the original
            encoded_df[column] = df[column]

        # Replace if none of the above holds
        else:
            replacement_mapping = encoding
            encoded_df[column] = df[column].replace(replacement_mapping)

    return encoded_df


raw_df = pd.read_csv(
    "./dataset/WA_Fn-UseC_-Telco-Customer-Churn.csv", sep=',')

print(raw_df)
processed_df = remove_white_space_with_Nan(raw_df)
processed_df = fill_null_data(
    processed_df, mapping=DS1_MISSING_VALUE_FILL_MAPPING)
processed_df = encode_data(processed_df, mapping=DS1_ENCODER_MAPPING)

print(processed_df.info())
processed_df.to_csv('result.csv')
