#pandas is a powerful data manipulation library in Python, widely used for data analysis and handling structured data.
import pandas as pd
#series is a one-dimensional array-like object that can hold various data types.
if __name__ == "__main__": # Ensure this code runs only when the script is executed directly because pandas is imported above and we want to avoid conflicts.
    data = [100, 102, 104]
    series = pd.Series(data, index=['a', 'b', 'c'])
    print(series)