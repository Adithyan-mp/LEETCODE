# Syntax: pandas.melt(frame, id_vars=None, value_vars=None,
# var_name=None, value_name=’value’, col_level=None)
import pandas as pd

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    return pd.melt(report,id_vars=['product'],value_vars=['quarter_1','quarter_2','quarter_3','quarter_4'],var_name='quarter',value_name='sales')
