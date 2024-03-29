# The rename() method allows you to change the row indexes, and the columns labels.
# Syntax
# dataframe.rename(mapper, index, columns, axis, copy, inplace, level, errors)

import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    return students.rename(columns={'id':"student_id","first":"first_name","last":"last_name","age":"age_in_years"})
