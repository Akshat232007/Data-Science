import matplotlib.pyplot as plt

subjects = ['Python for DS', 'Data Structures', 'Database Systems', 'Machine Learning', 'Web Development']
scores = [85, 70, 75, 90, 65]
explode = [0.1, 0, 0, 0, 0]

plt.pie(scores, labels=subjects, autopct='%1.1f%%', explode=explode)
plt.title('Subject Scores Breakdown')
plt.show()