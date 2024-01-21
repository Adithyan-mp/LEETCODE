# Syntax: concat(objs, axis, join, ignore_index, keys, levels, names, verify_integrity, sort, copy)
import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([df1,df2],join='outer',axis=0)
