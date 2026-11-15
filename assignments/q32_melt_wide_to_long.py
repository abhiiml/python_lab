# Q. Employee DataFrame (wide format) -> long format using melt()
# An employee may have more than 1 contact no. and more than 1 project location.
# Wide format: one column per project location, holding the contact number
# used for that location.
import pandas as pd

wide = pd.DataFrame({
    "emp_id":   ["E01", "E02", "E03", "E04", "E05"],
    "emp_name": ["Amit", "Suraj", "Alia", "Sonal", "Ira"],
    "Kolkata":  ["9830011111", "9830022222", None,         "9830044444", "9830055555"],
    "Delhi":    ["9811011111", None,         "9811033333", "9811044444", None],
    "Mumbai":   [None,         "9820022222", "9820033333", None,         "9820055555"],
})

print("Wide format:")
print(wide)

long = wide.melt(
    id_vars=["emp_id", "emp_name"],
    value_vars=["Kolkata", "Delhi", "Mumbai"],
    var_name="project_location",
    value_name="contact_no",
)

# drop rows where the employee has no project in that location
long = long.dropna(subset=["contact_no"]).sort_values("emp_id").reset_index(drop=True)

print("\nLong format (using melt):")
print(long)
