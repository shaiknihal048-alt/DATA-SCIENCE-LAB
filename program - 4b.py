
import pandas as pd
index = pd.MultiIndex.from_tuples(
    [
        ('Engineering', 'CSE'),
        ('Engineering', 'ECE'),
        ('Science', 'Physics'),
        ('Science', 'Chemistry')
    ],
    names=['Department', 'Branch']
)
data = pd.DataFrame(
    {
        '2025': [85, 78, 92, 88],
        '2026': [90, 82, 95, 91]
    },
    index=index
)
print("Original Tabular Data:")
print(data)
unstacked_data = data.unstack()
print("\nData after Unstack():")
print(unstacked_data)
stacked_data = unstacked_data.stack()
print("\nData after Stack():")
print(stacked_data)



Original Tabular Data:
                       2025  2026
Department  Branch               
Engineering CSE          85    90
            ECE          78    82
Science     Physics      92    95
            Chemistry    88    91

Data after Unstack():
             2025                          2026                        
Branch        CSE Chemistry   ECE Physics   CSE Chemistry   ECE Physics
Department                                                             
Engineering  85.0       NaN  78.0     NaN  90.0       NaN  82.0     NaN
Science       NaN      88.0   NaN    92.0   NaN      91.0   NaN    95.0

Data after Stack():
                       2025  2026
Department  Branch               
Engineering CSE        85.0  90.0
            ECE        78.0  82.0
Science     Chemistry  88.0  91.0
            Physics    92.0  95.0
