import numpy as np

arr1=np.array([1,2,3,4,5,6])
arr2=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr1)
print(arr2)
print(arr1.ndim)
print(arr2.ndim)
print(arr1.dtype)
print(arr1.size)
print(arr1.shape)
print(arr2.shape)
print(arr1.itemsize)
arr3=np.array([[1,2,3],[4,5,6]])
print(arr3.shape)
arr4=np.zeros(5)
print(arr4)
arr5=np.zeros((2,2))
print(arr5)
arr6=np.ones(3)
print(arr6)
arr7=np.eye(3)
print(arr7)
arr8=np.random.rand(4)
print(arr8)
arr9=np.random.rand(3,3)
print(arr9)
arr10=np.random.randint(10,211,6)
print(arr10)
arr11=np.full([3,4],0.11)
print(arr11)
arr12=np.arange(0,30,5)
print(arr12)
arr13=np.arange(1,10)
print(arr13)
arr14=np.arange(1,10).reshape(3,3)
print(arr14)
arr15=np.linspace(1,3,10)
print(arr15)
arr16=arr13.reshape(3,3)
print(arr16)
arr17=np.array([1,2,3,4,5,6,7])
print(arr17[5])
print(arr17[1:3])
print(arr17[-1:3])
print(arr17.max())
print(arr17.min())
print(arr17.argmax())
print(arr17.argmin())
print(arr17.sum())
print(arr2.sum(axis=0))
print(arr2.sum(axis=1))
print(arr2.cumsum(axis=0))
print(arr2.cumsum(axis=1))
print(arr2[1:-1,1:-1])


#OUTPUT

[1 2 3 4 5 6]
[[1 2 3]
 [4 5 6]
 [7 8 9]]
1
2
int32
6
(6,)
(3, 3)
4
(2, 3)
[0. 0. 0. 0. 0.]
[[0. 0.]
 [0. 0.]]
[1. 1. 1.]
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
[0.45001744 0.11582635 0.33494578 0.41164543]
[[0.81887157 0.39308087 0.92367274]
 [0.39101727 0.38606576 0.3742727 ]
 [0.47351761 0.73280706 0.40072962]]
[105  80  13 185 104  20]
[[0.11 0.11 0.11 0.11]
 [0.11 0.11 0.11 0.11]
 [0.11 0.11 0.11 0.11]]
[ 0  5 10 15 20 25]
[1 2 3 4 5 6 7 8 9]
[[1 2 3]
 [4 5 6]
 [7 8 9]]
[1.         1.22222222 1.44444444 1.66666667 1.88888889 2.11111111
 2.33333333 2.55555556 2.77777778 3.        ]
[[1 2 3]
 [4 5 6]
 [7 8 9]]
6
[2 3]
[]
7
1
6
0
28
[12 15 18]
[ 6 15 24]
[[ 1  2  3]
 [ 5  7  9]
 [12 15 18]]
[[ 1  3  6]
 [ 4  9 15]
 [ 7 15 24]]
[[5]]
