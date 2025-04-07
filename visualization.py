import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


# Load the preprocessed Titanic dataset
stage_data = pd.read_csv("./datasets/preprocessed_dataset/stage_data.csv")
embarked_pclass = pd.read_csv("./datasets/results/embarked_pclass.csv", index_col=0)
embarked_stats = pd.read_csv("./datasets/results//embarked_stats.csv")
family_class_survival = pd.read_csv("./datasets/results//family_class_survival.csv")

output_dir = "./datasets/results/images"

def save_plot(filename):
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, filename))
    plt.close()

plt.figure(figsize=(8, 6))
sns.barplot(x='pclass', y='survived', data=stage_data, hue='pclass', palette='Set2')   
plt.title('Average Survival Rate by Passenger Class')
plt.ylabel('Survival Rate')
plt.xlabel('Passenger Class')
plt.ylim(0, 1)
save_plot("survival_rate_by_pclass.png")


plt.figure(figsize=(8, 6))
sns.barplot(x='gender', y='survived', data=stage_data, hue='gender', palette='Set2')
plt.title('Average Survival Rate by Gender')
plt.ylabel('Survival Rate')
plt.xlabel('Gender')
plt.ylim(0, 1)
save_plot("survival_rate_by_gender.png")


age_bins = np.arange(0, stage_data['age'].max() + 10, 10)  # Creating age bins of 10 years
stage_data['age_group'] = pd.cut(stage_data['age'], bins=age_bins)
age_survival = stage_data.groupby('age_group')['survived'].mean().reset_index()

age_survival['age_group'] = age_survival['age_group'].astype(str)

# Plot the survival rate by age group
plt.figure(figsize=(10, 6))
sns.lineplot(x='age_group', y='survived', data=age_survival, marker='o', color='b')

plt.title('Average Survival Rate by Age Group')
plt.ylabel('Survival Rate')
plt.xlabel('Age Group')
plt.xticks(rotation=45)
plt.ylim(0, 1)
save_plot("survival_rate_by_age_group.png")


plt.figure(figsize=(10, 6))
sns.barplot(x='pclass', y='survived', data=stage_data)
plt.title('Survival by Passenger Class')
plt.ylabel('Count')
plt.xlabel('Passanger Class')
plt.ylim(0, 1)
save_plot("survival_by_passenger_class.png")

relevant_features = ['pclass', 'age', 'gender', 'survived']
data = stage_data[relevant_features].copy()
data = pd.get_dummies(data, columns=['gender'], drop_first=True)
correlation_matrix = data.corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True)
plt.title('Correlation Heatmap of Relevant Features (with One-Hot Encoded Gender)')
save_plot("correlation_heatmap.png")

plt.figure(figsize=(10, 6))
sns.heatmap(embarked_pclass, annot=True, cmap='Blues', fmt='d', cbar=False)
plt.title('Count of Passengers by Embarkation Port and Passenger Class')
plt.ylabel('Embarkation Port')
plt.xlabel('Passenger Class')
save_plot("embarked_vs_pclass_heatmap.png")

# Bar plot for survival statistics by embarkation port
embarked_stats = embarked_stats.reset_index()  # Reset index to make 'embarked' a column for plotting
embarked_stats_melted = embarked_stats.melt(id_vars='embarked', value_vars=['total_passengers', 'survivors'],
                                             var_name='Metric', value_name='Value')

plt.figure(figsize=(10, 6))
sns.barplot(x='embarked', y='Value', hue='Metric', data=embarked_stats_melted, palette='Set2')
plt.title('Survival Statistics by Embarkation Port')
plt.ylabel('Value')
plt.xlabel('Embarkation Port')
save_plot("embarked_survival_stats.png")

# Plotting the survival statistics for different family sizes
plt.figure(figsize=(10, 6))
sns.lineplot(x='family', y='mean', data=family_class_survival, marker='o', color='b', label='Survival Rate')
plt.title('Survival Rate by Family Size')
plt.ylabel('Value')
plt.xlabel('Family Size')
plt.legend()
save_plot("survival_rate_by_family_size.png")

# Group by passenger class and calculate the mean fare
pclass_fare = stage_data.groupby('pclass')['fare'].mean().reset_index()

# Plotting the average fare by passenger class
plt.figure(figsize=(10, 6))
sns.barplot(x='pclass', y='fare', data=pclass_fare)
plt.title('Average Fare by Passenger Class')
plt.ylabel('Average Fare')
plt.xlabel('Passenger Class')
save_plot("average_fare_by_pclass.png")