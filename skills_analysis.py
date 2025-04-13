import pandas as pd

skills = ["SQL", "Python", "Power BI", "Excel", "Tableau", "R", "Azure", "AWS"]

df = pd.read_csv("data/job_posts.csv")
results = {}

for skill in skills:
    count = df["summary"].str.contains(skill, case=False).sum()
    results[skill] = count

skills_df = pd.DataFrame.from_dict(results, orient='index', columns=["Count"])
skills_df.sort_values(by="Count", ascending=False).to_csv("data/skills_frequency.csv")
print(skills_df)
