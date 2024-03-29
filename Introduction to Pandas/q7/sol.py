import pandas as pd


    # Syntax: DataFrameName.dropna(axis=0, how=’any’, thresh=None, subset=None, inplace=False)

    # Parameters:

    #     axis: axis takes int or string value for rows/columns. Input can be 0 or 1 for Integer and ‘index’ or ‘columns’ for String. 
    #     how: how takes string value of two kinds only (‘any’ or ‘all’). ‘any’ drops the row/column if ANY value is Null and ‘all’ drops only if ALL values are null.
    #     thresh: thresh takes integer value which tells minimum amount of na values to drop. 
    #     subset: It’s an array which limits the dropping process to passed rows/columns through list. inplace: It is a boolean which makes the changes in data frame itself if True.


def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(axis=0,how='any',subset=['name'])
    
