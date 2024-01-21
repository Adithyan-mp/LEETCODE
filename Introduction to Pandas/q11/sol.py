    # Syntax: DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None, **kwargs)

    # Parameters: 

    #     value : Static, dictionary, array, series or dataframe to fill instead of NaN.
    #     method : Method is used if user doesn’t pass any value. Pandas have different methods like bfill, backfill, or ffill which fills the place with value in the Forward index or Previous/Back respectively.
    #     axis: axis takes int or string value for rows/columns. Input can be 0 or 1 for Integer and ‘index’ or ‘columns’ for String
    #     inplace: It is a boolean which makes the changes in data frame itself if True.
    #     limit : This is an integer value which specifies maximum number of consecutive forward/backward NaN value fills.
    #     downcast : It takes a dict which specifies what dtype to downcast to which one. Like Float64 to int64.
    #     **kwargs : Any other Keyword arguments


import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
   products.quantity=products.quantity.fillna(0)
   return products
