# Q. Distinguish between stack() and unstack() in a DataFrame
import pandas as pd

df = pd.DataFrame(
    {"Maths": [90, 80, 70], "Science": [85, 75, 65]},
    index=["Amit", "Rhea", "Raju"],
)
print("Original (wide) DataFrame:")
print(df)

# stack(): columns -> inner row index   (wide -> long, returns Series)
stacked = df.stack()
print("\nAfter stack():")
print(stacked)

# unstack(): inner row index -> columns (long -> wide, returns DataFrame)
unstacked = stacked.unstack()
print("\nAfter unstack():")
print(unstacked)

print("""
Difference:
+-------------+------------------------------------+------------------------------------+
| Point       | stack()                            | unstack()                          |
+-------------+------------------------------------+------------------------------------+
| Direction   | Columns -> rows                    | Rows (inner index) -> columns      |
| Shape       | Makes data taller (long format)    | Makes data wider (wide format)     |
| Result      | Series with MultiIndex             | DataFrame                          |
| Relation    | Inverse of unstack()               | Inverse of stack()                 |
+-------------+------------------------------------+------------------------------------+
""")
