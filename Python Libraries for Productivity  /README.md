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


