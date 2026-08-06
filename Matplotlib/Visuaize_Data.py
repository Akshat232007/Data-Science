import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales_2023 = [150, 200, 250, 300, 280, 350]
sales_2024 = [180, 220, 270, 320, 300, 400]

plt.plot(months, sales_2023, color='blue', linestyle='--', marker='o', label='2023')
plt.plot(months, sales_2024, color='green', linestyle='-', marker='s', label='2024')

plt.title("Monthly Sales Comparison (2023 vs 2024)")
plt.xlabel("Months")
plt.ylabel("Sales")
plt.legend()

max_sales_2024 = max(sales_2024)
max_month = months[sales_2024.index(max_sales_2024)]

plt.annotate(
    f'Highest Sales ({max_sales_2024})',
    xy=(max_month, max_sales_2024),
    xytext=('May', max_sales_2024 - 20),
    arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=6)
)

plt.tight_layout()
plt.savefig("sales_comparison.png")
plt.show()