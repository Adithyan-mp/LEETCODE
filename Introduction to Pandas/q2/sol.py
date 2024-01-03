#Get the Size of a DataFrame
import pandas as pd
#DataFrame.shape[source]
#Return a tuple representing the dimensionality of the DataFrame.
def getDataframeSize(players: pd.DataFrame) -> List[int]:
    row,column=players.shape
    return [row,column]
    
