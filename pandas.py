import numpy as np
import pandas as pd
arr=np.array([1,2,3,4,np.nan,6,7])
print(arr)
s=pd.Series(arr)
print(s)
print('-'*30)
dates=pd.date_range(start='20191202',periods=5)
print(dates)
print('-'*30)
datesDF=pd.DataFrame(np.random.randn(5,5),index=dates,columns=list('ABCDE'))
print(datesDF)
print('-'*30)
dict1={
       'Name':['gagan','naman','tushar','luv','anil'],
       'Age':[20,21,19,21,22],
       'Gender':['Male','Male','Female','Male','Male'],
       'Job':['Student','Student','Student','Student','Student']
       }
df2=pd.DataFrame(dict1,index=list('ABCDE'))
print(df2)
print('-'*30)
print(df2.dtypes)
print('-'*30)
print(df2.head(2))
print('-'*30)
print(df2.tail(2))
print('-'*30)
print(df2.index)
print(df2.columns)
print(datesDF.describe())
print(df2.T)
print(df2['Name'])
print(df2.loc[:, ['Name', 'Job']])
print(df2.iloc[3])
s1 = pd.Series(np.random.randint(0, 7, size=10))
print(s1)
s2 = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
print(s2.str.lower())




#OUTPUT

[ 1.  2.  3.  4. nan  6.  7.]
0    1.0
1    2.0
2    3.0
3    4.0
4    NaN
5    6.0
6    7.0
dtype: float64
------------------------------
DatetimeIndex(['2019-12-02', '2019-12-03', '2019-12-04', '2019-12-05',
               '2019-12-06'],
              dtype='datetime64[ns]', freq='D')
------------------------------
                   A         B         C         D         E
2019-12-02 -0.614694  0.111971 -1.057846  0.609306  0.098268
2019-12-03  1.764978  0.675623 -0.858314  0.220436 -0.963655
2019-12-04 -0.090642 -0.515079  0.671625 -0.786618 -0.789599
2019-12-05 -0.679139 -1.071400  1.369087  0.137551  0.788542
2019-12-06 -1.529695 -1.029883  0.470204  0.276035  0.835666
------------------------------
     Name  Age  Gender      Job
A   gagan   20    Male  Student
B   naman   21    Male  Student
C  tushar   19  Female  Student
D     luv   21    Male  Student
E    anil   22    Male  Student
------------------------------
Name      object
Age        int64
Gender    object
Job       object
dtype: object
------------------------------
    Name  Age Gender      Job
A  gagan   20   Male  Student
B  naman   21   Male  Student
------------------------------
   Name  Age Gender      Job
D   luv   21   Male  Student
E  anil   22   Male  Student
------------------------------
Index(['A', 'B', 'C', 'D', 'E'], dtype='object')
Index(['Name', 'Age', 'Gender', 'Job'], dtype='object')
              A         B         C         D         E
count  5.000000  5.000000  5.000000  5.000000  5.000000
mean  -0.229838 -0.365754  0.118951  0.091342 -0.006156
std    1.228646  0.753988  1.040621  0.522497  0.848779
min   -1.529695 -1.071400 -1.057846 -0.786618 -0.963655
25%   -0.679139 -1.029883 -0.858314  0.137551 -0.789599
50%   -0.614694 -0.515079  0.470204  0.220436  0.098268
75%   -0.090642  0.111971  0.671625  0.276035  0.788542
max    1.764978  0.675623  1.369087  0.609306  0.835666
              A        B        C        D        E
Name      gagan    naman   tushar      luv     anil
Age          20       21       19       21       22
Gender     Male     Male   Female     Male     Male
Job     Student  Student  Student  Student  Student
A     gagan
B     naman
C    tushar
D       luv
E      anil
Name: Name, dtype: object
     Name      Job
A   gagan  Student
B   naman  Student
C  tushar  Student
D     luv  Student
E    anil  Student
Name          luv
Age            21
Gender       Male
Job       Student
Name: D, dtype: object
0    1
1    3
2    2
3    1
4    4
5    4
6    3
7    3
8    5
9    2
dtype: int32
0       a
1       b
2       c
3    aaba
4    baca
5     NaN
6    caba
7     dog
8     cat
dtype: object