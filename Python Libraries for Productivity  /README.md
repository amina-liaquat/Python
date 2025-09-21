# Python Libraries for Productivity  

Python has a bunch of libraries that make our life easier as developers. Instead of writing everything from scratch, we can use these libraries to **analyze data, visualize results, work with APIs, or even scrape websites**.  

---

## Pandas (Data Analysis)  

Think of Pandas as **Excel inside Python**. It helps us organize, clean, and analyze data.  

Best for: working with tables, spreadsheets, and CSV files.  

**Example:**
```python
import pandas as pd

data = {"Task": ["Coding", "Meeting", "Email"], "Hours": [3, 2, 1]}
df = pd.DataFrame(data)

print(df)          # Shows the table
print(df.describe())  # Quick stats like mean, min, max
```

---

## NumPy (Numerical Computing)

NumPy is all about numbers and math. It gives us fast arrays and functions to do calculations quickly.

Best for: big calculations, statistics, and scientific computing.

## Example:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print("Array:", arr)
print("Mean:", np.mean(arr))
print("Square Root:", np.sqrt(arr))
```

---


















