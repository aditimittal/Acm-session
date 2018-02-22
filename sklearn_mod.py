from sklearn.datasets import load_iris #load iris is a func
iris=load_iris()

print (iris.data)
print (iris.feature_names) # headers of the columns

print (iris.target ) # 0,1,2 corresponds to target_names

print (iris.target_names )#is the classification say 0,1,2 has some value
print (iris.data.shape)

print (iris.target.shape)
