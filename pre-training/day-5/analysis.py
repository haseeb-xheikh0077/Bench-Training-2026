import pandas as pd

df = pd.read_csv("titanic.csv")

# ── helper to print section headers 
def header(n, title):
    print(f"\n{'─' * 50}")
    print(f"  Q{n:02d}. {title}")
    print(f"{'─' * 50}")


# ── Q01. Survived vs. did not survive 
header(1, "Survived vs. Did Not Survive")

counts = df["Survived"].value_counts().rename({0: "Did not survive", 1: "Survived"})
pct = (counts / len(df) * 100).round(1)

for label in counts.index:
    print(f"  {label:<20} {counts[label]:>4}  ({pct[label]}%)")


# ── Q02. Survival rate by passenger class 
header(2, "Survival Rate by Passenger Class")

# groupby splits the dataframe into groups; mean() on Survived gives the rate (0/1 column)
class_survival = df.groupby("Pclass")["Survived"].mean().mul(100).round(1)
class_names = {1: "1st Class", 2: "2nd Class", 3: "3rd Class"}

for pclass, rate in class_survival.items():
    print(f"  {class_names[pclass]}: {rate}%")


# ── Q03. Average age: survivors vs. non-survivors 
header(3, "Average Age of Survivors vs. Non-Survivors")

avg_age = df.groupby("Survived")["Age"].mean().round(1)

print(f"  Survivors     : {avg_age[1]} years")
print(f"  Non-survivors : {avg_age[0]} years")


# ── Q04. Embarkation port with highest survival rate 
header(4, "Survival Rate by Embarkation Port")

port_names = {"C": "Cherbourg", "Q": "Queenstown", "S": "Southampton"}
port_survival = df.groupby("Embarked")["Survived"].mean().mul(100).round(1).sort_values(ascending=False)

for code, rate in port_survival.items():
    print(f"  {port_names.get(code, code):<15} {rate}%")

best_port = port_names.get(port_survival.idxmax(), port_survival.idxmax())
print(f"\n  Highest survival rate: {best_port}")


# ── Q05. Missing ages → fill with class median 
header(5, "Missing Age Values → Fill with Class Median")

missing_before = df["Age"].isna().sum()
print(f"  Missing age values before: {missing_before}")

# For each passenger, fill their missing age with the median age of their class
df["Age"] = df.groupby("Pclass")["Age"].transform(lambda x: x.fillna(x.median()))

missing_after = df["Age"].isna().sum()
print(f"  Missing age values after : {missing_after}")
print(f"  Filled {missing_before - missing_after} values using per-class medians")


# ── Q06. Oldest surviving passenger 
header(6, "Oldest Surviving Passenger")

# Filter to survivors only, then find the row with the max age
oldest = df[df["Survived"] == 1].loc[df[df["Survived"] == 1]["Age"].idxmax()]

print(f"  Name  : {oldest['Name']}")
print(f"  Age   : {int(oldest['Age'])}")
print(f"  Class : {class_names[oldest['Pclass']]}")


# ── Q07. Survival rate by gender 
header(7, "Survival Rate by Gender")

gender_survival = df.groupby("Sex")["Survived"].mean().mul(100).round(1)

print(f"  Women : {gender_survival['female']}%")
print(f"  Men   : {gender_survival['male']}%")


# ── Q08. AgeGroup column → survival rate per group 
header(8, "Survival Rate by Age Group")

# pd.cut bins a numeric column into labeled ranges
df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[0, 18, 60, 200],
    labels=["Child (<18)", "Adult (18-60)", "Senior (60+)"]
)

age_survival = df.groupby("AgeGroup", observed=True)["Survived"].mean().mul(100).round(1)

for group, rate in age_survival.items():
    print(f"  {group:<20} {rate}%")


# ── Q09. 3rd class: survival rate for men vs. women 
header(9, "3rd Class — Survival Rate by Gender")

third_class = df[df["Pclass"] == 3]
third_survival = third_class.groupby("Sex")["Survived"].mean().mul(100).round(1)

print(f"  Women : {third_survival['female']}%")
print(f"  Men   : {third_survival['male']}%")


# ── Q10. Drop rows with missing Cabin data 
header(10, "Rows Remaining After Dropping Missing Cabin Data")

original_count = len(df)
df_with_cabin  = df.dropna(subset=["Cabin"])
remaining = len(df_with_cabin)
kept_pct = round(remaining / original_count * 100, 1)

print(f"  Original rows : {original_count}")
print(f"  Rows remaining: {remaining}")
print(f"  Data kept     : {kept_pct}%")

print(f"\n{'─' * 50}\n")
