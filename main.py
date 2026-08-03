import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel("Dataset/Startup_Financial_KPI_Dataset.xlsx")

total = [
    data["Revenue"].sum(),
    data["Marketing Cost"].sum(),
    data["Expenses"].sum()
]

labels = ["Revenue", "Marketing Cost", "Expenses"]

plt.pie(total, labels=labels, autopct="%1.1f%%")
plt.title("Revenue, Marketing Cost and Expenses")
plt.show()