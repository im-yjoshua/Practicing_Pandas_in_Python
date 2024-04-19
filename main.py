import pandas as pd

def func1():
    """
    This function will read the csv, and return the first 5 rows in the dataset.
    """
    dataFrame = pd.read_csv('./dataset.csv')
    return dataFrame.head(5)


# print(func1())


# ===================================

def func2():
    """
    This function will the read the dataset, and return the data types of each column.
    """
    dataFrame = pd.read_csv("./dataset.csv")
    DataTypes_list = []
    for i in range(len(dataFrame.dtypes)):
        DataTypes_list.append(dataFrame.dtypes[i])
    return f"Column Types:\n{DataTypes_list}\nDescription:\n{dataFrame.describe()}"


# print(func2())


# ====================================

def func3():
    """
    This function will read the dataset, select the {name, & age} columns,
    and will only return the entries whose age is greater than 30.
    """
    dataFrame = pd.read_csv("./dataset.csv")
    # Selecting the columns 'Name' and 'Age'
    selecting_cols = dataFrame[["Name", "Age"]]
    # Applying boolean indexing to select rows where age is greater than 30
    filtered_data = selecting_cols[selecting_cols["Age"] > 30]
    return filtered_data

# print(func3())

# ====================================

def func4():
    """
    This function will read the dataset, and find the missing values, in it, and will replace the missing values with the mean of the respective columns
    """
    dataFrame = pd.read_csv("./dataset.csv")
    # Finding the missing values
    missing_values = dataFrame.isnull().sum()
    # Finding the mean of Age column (as it has integer values)
    mean_values = dataFrame["Age"].mean()
    # Replacing the missing values with the mean of each column
    dataFrame = dataFrame.fillna(mean_values)
    return dataFrame

# print(func4()) 

# ====================================

def func5():
    """
    This function will read to datasets in csv format, and merge both of them on the basis of ["Name"] column.
    """
    dataFrame1 = pd.read_csv("./dataset.csv")
    dataFrame2 = pd.read_csv("./dataset2.csv")
    merged_data = pd.merge(dataFrame1, dataFrame2, on=["Name"])
    return merged_data

# print(func5())
