import numpy as np
import pandas as pd

# Add a placeholder (like 'Index') to the first row so all rows have 3 elements
data = np.array([
    ['Index', 'Col1', 'Col2'], 
    ['Row1', '1', '2'], 
    ['Row2', '3', '4']
])

# Slicing shifts perfectly now:
# Data = row 1 onwards, col 1 onwards
# Index = row 1 onwards, col 0
# Columns = row 0, col 1 onwards
df1 = pd.DataFrame(
    data=data[1:, 1:], 
    index=data[1:, 0], 
    columns=data[0, 1:]
)

print(df1)
