
#Program 1
import pandas as pd
ufo=pd.read_csv('http://bit.ly/uforeports')
print(ufo.head)
print(ufo.shape)

'''
#Program2- shows all the attributes
import pandas as pd
ufo=pd.read_csv('http://bit.ly/uforeports')
print(ufo.columns) #shows all the attributes
'''

'''
#Program3- display value of attributes
import pandas as pd
ufo=pd.read_csv('http://bit.ly/uforeports')
print(ufo['City'])
print(ufo['Colors Reported'])

'''

'''
 #Program4- rename columns
import pandas as pd
ufo=pd.read_csv('http://bit.ly/uforeports')
print(ufo.columns)
ufo.rename(columns={'Colors Reported':'Colors_Reported','Shape Reported':'Shape_Reported'},inplace=True)
print(ufo.columns)
'''


'''
http://bit.ly/imdbratings
'''
