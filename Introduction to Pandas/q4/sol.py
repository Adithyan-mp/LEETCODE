import pandas as pd
#data_frame.loc[row_label, column_label]
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students['student_id']==101,['name','age']]
