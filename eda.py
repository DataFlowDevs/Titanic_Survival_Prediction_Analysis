import pandas as pd

# Load the preprocessed Titanic dataset
the_titanic_df = pd.read_csv("./datasets/preprocessed_dataset/stage_data.csv")

# Grouping by passenger class to get total, survived and survival rate
survivor_counts_per_pclass = the_titanic_df.groupby('pclass').agg(
    survivor_count=('survived', 'count'),
    survivor_sum=('survived', 'sum'),
    survivor_rate=('survived', 'mean')
)
survivor_counts_per_pclass.to_csv("./datasets/results/survivor_counts_per_pclass.csv")

# Aggregating survival statistics by gender
gender_survival_agg = the_titanic_df.groupby(['gender'], as_index=False)['survived'].agg(['count', 'sum','mean'])
gender_survival_agg.to_csv("./datasets/results/gender_survival_agg.csv")

# Aggregating survival statistics by class and gender
gender_class_survival_agg = the_titanic_df.groupby(['pclass', 'gender'])['survived'].agg(['count', 'sum','mean'])
gender_class_survival_agg.to_csv("./datasets/results/gender_class_survival_agg.csv")

# Calculating average fare per passenger class
pclass_mean_fare = the_titanic_df.groupby(['pclass'], as_index=False)['fare'].mean()
pclass_mean_fare.to_csv("./datasets/results/pclass_mean_fare.csv", index=False)

# Analyzing survival by family size
family_class_survival = the_titanic_df.groupby(['family'])['survived'].agg(['count', 'sum', 'mean'])
family_class_survival.to_csv("./datasets/results/family_class_survival.csv")

# Analyzing survival rate based on fare paid
survival_by_fare = the_titanic_df.groupby(['fare'], as_index=False)['survived'].mean()
survival_by_fare.to_csv("./datasets/results/survival_by_fare.csv", index=False)

# Embarkation analysis: passenger count, survival count, and survival rate
embarked_stats = the_titanic_df.groupby('embarked').agg(
    stotal_passengers=('survived', 'count'),
    survivors=('survived', 'sum'),
    survivor_rate=('survived', 'mean')
)
embarked_stats.to_csv("./datasets/results/embarked_stats.csv")

# Distribution of passenger classes per embarkation point
embarked_pclass = the_titanic_df.groupby(['embarked', 'pclass']).size().unstack()
embarked_pclass.to_csv("./datasets/results/embarked_pclass.csv")

# Mean fare paid by embarkation point
mean_fare_by_embark = the_titanic_df.groupby('embarked')['fare'].mean()
mean_fare_by_embark.to_csv("./datasets/results/mean_fare_by_embark.csv")
