#Create a DataFrame from List
import pandas as pd

#DataFrame(data=None, index=None, columns=None, dtype=None, copy=None)
def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    data_frame=pd.DataFrame(student_data,columns=['student_id','age'])
    return data_frame
    
