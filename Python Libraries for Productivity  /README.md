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

## Matplotlib (Data Visualization)

Data is more fun when we can see it. Matplotlib helps us turn numbers into graphs and charts.

Best for: line plots, bar charts, scatter plots, and more.

---

## Example:

```python
import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y, marker='o', color='purple')
plt.title("Simple Line Chart")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
```

---

## Requests (APIs & HTTP Requests)

Requests is like the postman of Python. It helps us talk to websites and APIs.

Best for: fetching data from the web or APIs.

---

## Example:

```pyhon
import requests

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print("Status Code:", response.status_code)
print("JSON Response:", response.json())
```

---












