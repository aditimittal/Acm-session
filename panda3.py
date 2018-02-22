
#Program3- display value of attributes
import pandas as pd
ufo=pd.read_csv('http://bit.ly/uforeports')
print(ufo['City'])
print(ufo['Colors Reported'])
