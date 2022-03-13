import numpy as np
import pandas as pd


def get_rank(country_code: str, df: pd.DataFrame):
    """
    returns the rank of the country_code passed in parameters,
     if it contains the country code, returns a np.nan if not.
    """
    rank = df.index[(df['Country Code'] == country_code)]
    if len(rank) == 0:
        return np.nan
    elif len(rank) == 1:
        return int(rank[0])


def rate_col(dataframe: pd.DataFrame, column_label: str):
    """changes rank to a grade / 100, applied on Dataframe"""
    total_ranks = len(dataframe[~dataframe[column_label].isna()])
    for index, series in dataframe.iterrows():
        dataframe.at[index, column_label] = ((dataframe.loc[index, column_label]) / total_ranks) * 100


def final_rating(dataframe: pd.DataFrame, k_per_col: dict) -> pd.DataFrame:
    """
    applies coefficients and assigns correct combined ratings to dataframe,
     returns dataframe ordered by combined rating, descending. + index reset
    """
    col_labels = k_per_col.keys()

    def combine_rating(series: pd.Series):
        """returns the combined rating of a series with k"""
        total = 0
        for label in col_labels:
            total += k_per_col[label] * series[label]

        return total / sum(k_per_col.values())

    for index, series in dataframe.iterrows():
        final_score = combine_rating(series)
        dataframe.loc[index, "combined_rating"] = final_score

    return dataframe.sort_values(by="combined_rating", ascending=False).reset_index(drop=True)
