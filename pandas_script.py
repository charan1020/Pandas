# pandas is a powerful data manipulation library in Python, widely used for data analysis and handling structured data.
# NOTE: This file is named `pandas.py` which will shadow the real `pandas` package from site-packages.
# To avoid import errors, rename this file (for example to `pandas_example.py`) and delete any
# `pandas.pyc` or `__pycache__` related to this file.

try:
    import pandas as pd
except Exception as e:
    raise ImportError(
        "Failed to import the real 'pandas' package. If this file is named 'pandas.py' it may be shadowing the package. "
        "Rename this file (for example to 'pandas_example.py') and remove any '__pycache__' or '*.pyc' files, then try again.") from e

# If import succeeded but looks like our local file, give a clear message:
if not hasattr(pd, 'Series'):
    raise ImportError(
        "Imported a module named 'pandas' that doesn't look like the pandas package (it has no 'Series'). "
        "This usually happens when your script is named 'pandas.py'. Please rename this file (e.g., to 'pandas_example.py') and delete 'pandas.pyc' and '__pycache__'.")

# series is a one-dimensional array-like object that can hold various data types.
if __name__ == '__main__':
    data = [100, 102, 104]
    series = pd.Series(data)
    print(series)

