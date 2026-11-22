
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [12, 18, 15, 22]
subjects = ["Math", "Science", "English"]
marks = [85, 90, 78]

figure, axes = plt.subplots(2, 2, figsize=(9, 7))

axes[0, 0].plot(months, sales, marker="o")
axes[0, 0].set_title("Line Chart")

axes[0, 1].bar(months, sales)
axes[0, 1].set_title("Bar Chart")

axes[1, 0].hist(sales, bins=4)
axes[1, 0].set_title("Histogram")

axes[1, 1].pie(marks, labels=subjects, autopct="%1.1f%%")
axes[1, 1].set_title("Pie Chart")

figure.tight_layout()
plt.show()
