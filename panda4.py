
 #Program4- rename columns
import pandas as pd
ufo=pd.read_csv('http://bit.ly/uforeports')
print(ufo.columns)
ufo.rename(columns={'Colors Reported':'Colors_Reported','Shape Reported':'Shape_Reported'},inplace=True)
print(ufo.columns)

