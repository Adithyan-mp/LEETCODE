# DataFrame.drop_duplicates(subset=None, *, keep='first', inplace=False, ignore_index=False
# Return DataFrame with duplicate rows removed.
#to find duplicate om column use subset['column name']
import pandas as pd
def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset=['email'])
