
import pandas as pd
index = [
    ['Engineering', 'Engineering', 'Science', 'Science'],
    ['CSE', 'ECE', 'Physics', 'Chemistry']
]

multi_index = pd.MultiIndex.from_arrays(
    index,
    names=['Department', 'Branch']
)
marks = pd.Series(
    [85, 78, 92, 88],
    index=multi_index
)

print("Original Series:")
print(marks)
print("\nData for Engineering:")
print(marks.loc['Engineering'])
print("\nData for CSE:")
print(marks.loc[('Engineering', 'CSE')])
print("\nData for Science:")
print(marks.loc['Science'])





Original Series:
Department   Branch   
Engineering  CSE          85
             ECE          78
Science      Physics      92
             Chemistry    88
dtype: int64

Data for Engineering:
Branch
CSE    85
ECE    78
dtype: int64

Data for CSE:
85

Data for Science:
Branch
Physics      92
Chemistry    88
dtype: int64
