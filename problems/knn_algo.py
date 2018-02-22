from sklearn.datasets import load_iris  #load iris is a func
from sklearn.neighbors import KNeighborsClassifier
iris=load_iris()

print (iris.data)

x=iris.data #matrix
y=iris.target #vector
knn=KNeighborsClassifier(n_neighbors=1) # n_neighbors tells values of k, knn is object
knn.fit(x,y)
x_new=[[3,5,4,2],[1,2,1,3]]
print(knn.predict(x_new))  #here 0,1,2 are targets, they have target_names associated with them
