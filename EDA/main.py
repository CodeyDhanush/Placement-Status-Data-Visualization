import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("college_student_placement_dataset.csv")

# Count the number of 'Yes' and 'No' in the 'Placement' column
yes_count = (df["Placement"] == 'Yes').sum()
no_count = (df["Placement"] == 'No').sum()

print("Placed (Yes):", yes_count)
print("Not Placed (No):", no_count)

# Create the bar chart
labels = ['Placed (Yes)', 'Not Placed (No)']
values = [yes_count, no_count]

plt.bar(labels, values, color=['green', 'red'])
plt.title('Placement Status')
plt.xlabel('Placement')
plt.ylabel('Number of Students')
plt.show()

