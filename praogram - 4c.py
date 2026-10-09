
import pandas as pd
df1 = pd.DataFrame(
    {
        'Name': ['Ravi', 'Sita', 'Arun'],
        'Marks': [85, None, 78],
        'Grade': ['A', 'B', None]
    },
    index=[101, 102, 103]
)
df2 = pd.DataFrame(
    {
        'Name': ['Ravi', 'Sita', 'Kiran'],
        'Marks': [90, 88, 82],
        'Grade': [None, 'A', 'B']
    },
    index=[101, 102, 104]
)
print("First DataFrame:")
print(df1)
print("\nSecond DataFrame:")
print(df2)
merged = pd.merge(
    df1,
    df2,
    left_index=True,
    right_index=True,
    how='outer',
    suffixes=('_DF1', '_DF2')
)
print("\nMerged DataFrame:")
print(merged)
combined = df1.combine_first(df2)
print("\nDataFrame after combine_first():")
print(combined)




First DataFrame:
     Name  Marks Grade
101  Ravi   85.0     A
102  Sita    NaN     B
103  Arun   78.0  None

Second DataFrame:
      Name  Marks Grade
101   Ravi     90  None
102   Sita     88     A
104  Kiran     82     B

Merged DataFrame:
    Name_DF1  Marks_DF1 Grade_DF1 Name_DF2  Marks_DF2 Grade_DF2
101     Ravi       85.0         A     Ravi       90.0      None
102     Sita        NaN         B     Sita       88.0         A
103     Arun       78.0      None      NaN        NaN       NaN
104      NaN        NaN       NaN    Kiran       82.0         B

DataFrame after combine_first():
      Name  Marks Grade
101   Ravi   85.0     A
102   Sita   88.0     B
103   Arun   78.0   NaN
104  Kiran   82.0     B
