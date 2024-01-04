import pandas as pd
#DataFrame.iloc[source]
#Purely integer-location based indexing for selection by position
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.iloc[:3]
    
