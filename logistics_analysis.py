import pandas as pd

# Load the logistics dataset
df = pd.read_csv("data.csv")

# Calculate extra travel time
df["extra_time"] = df["actual_time"] - df["osrm_time"]

# Calculate key performance indicators
average_extra_time = df["extra_time"].mean()
average_actual_time = df["actual_time"].mean()

print("Average extra time:", average_extra_time)
print("Average actual time:", average_actual_time)

# Compare average extra time by route type
route_analysis = df.groupby("route_type")["extra_time"].mean()

print("\nAverage extra time by route type:")
print(route_analysis)
