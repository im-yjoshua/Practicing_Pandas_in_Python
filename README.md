# Function Documentation

## func1()

This function reads a CSV file and returns the first 5 rows in the dataset.

```python
import pandas as pd

def func1():
    """
    This function will read the csv, and return the first 5 rows in the dataset.
    """
    dataFrame = pd.read_csv('./dataset.csv')
    return dataFrame.head(5)
```