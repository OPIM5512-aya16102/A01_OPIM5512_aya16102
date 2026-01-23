from sklearn.datasets import fetch_california_housing
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import os

from sklearn.datasets import fetch_california_housing
import pandas as pd

# Update this line to include your working directory !
os.chdir(r"C:\Users\admin\Desktop\Grad_School\OPIM5512\Repository_Clones\A01\A01_OPIM5512_aya16102")

# Load California Housing dataset
housing = fetch_california_housing(as_frame=True)

# Features + target as a single DataFrame
df = housing.frame

# Quick check
print(df.head())
print(df.shape)

# you can save the boxplot...
plt.figure(figsize=(8, 6))
plt.boxplot(df["MedHouseVal"])
plt.title("Boxplot of MedHouseValue")
plt.ylabel("Value")
plt.xlabel("MedHouseValue")

# Save the plot
plt.savefig("figs/MedHouseVal.png", dpi=300, bbox_inches="tight")
plt.close()

