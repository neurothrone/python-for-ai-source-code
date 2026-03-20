# %%
import matplotlib.pyplot as plt
import seaborn as sns

tips = sns.load_dataset("tips")

print(tips.head())

# %%
sns.scatterplot(data=tips, x="total_bill", y="tip")
plt.title("Total Bill vs Tip")
plt.show()

# %%
sns.boxplot(data=tips, x="day", y="total_bill")
plt.title("Total Bill by Day")
plt.show()