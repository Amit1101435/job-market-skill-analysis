import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data/skills_frequency.csv")
sns.barplot(x=df.index, y="Count", data=df)
plt.title("Skill Frequency in Job Descriptions")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("data/skill_trends.png")
