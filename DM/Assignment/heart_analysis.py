import pandas as pd
import numpy as np

# Load the heart disease dataset
print("=" * 60)
print("HEART DISEASE DATASET ANALYSIS")
print("=" * 60)

# Load the data
df = pd.read_csv('heart.csv')
print(f"Dataset shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
print("\nFirst 5 rows:")
print(df.head())

print("\n" + "=" * 60)
print("1. BASIC STATISTICAL ANALYSIS")
print("=" * 60)

# Basic statistics
print("\n1.1 Descriptive Statistics:")
print(df.describe())

print("\n1.2 Data Types:")
print(df.dtypes)

print("\n1.3 Missing Values:")
print(df.isnull().sum())

print("\n" + "=" * 60)
print("2. TARGET VARIABLE ANALYSIS")
print("=" * 60)

# Target variable analysis
print("\n2.1 Target Distribution:")
target_counts = df['target'].value_counts()
print(target_counts)
print(f"\nPercentage distribution:")
print(target_counts / len(df) * 100)

print("\n2.2 Target by Gender:")
target_by_sex = pd.crosstab(df['sex'], df['target'], margins=True)
print(target_by_sex)

print("\n" + "=" * 60)
print("3. AGE ANALYSIS")
print("=" * 60)

# Age analysis
print("\n3.1 Age Statistics:")
print(f"Mean age: {df['age'].mean():.2f}")
print(f"Median age: {df['age'].median():.2f}")
print(f"Min age: {df['age'].min()}")
print(f"Max age: {df['age'].max()}")
print(f"Age standard deviation: {df['age'].std():.2f}")

print("\n3.2 Age Groups:")
df['age_group'] = pd.cut(df['age'], bins=[0, 40, 50, 60, 70, 100], 
                        labels=['<40', '40-50', '50-60', '60-70', '70+'])
age_group_target = pd.crosstab(df['age_group'], df['target'])
print(age_group_target)

print("\n3.3 Age Distribution by Target:")
print(df.groupby('target')['age'].describe())

print("\n" + "=" * 60)
print("4. GENDER ANALYSIS")
print("=" * 60)

# Gender analysis
print("\n4.1 Gender Distribution:")
sex_counts = df['sex'].value_counts()
print(sex_counts)
print(f"\nGender distribution (%):")
print(sex_counts / len(df) * 100)

print("\n4.2 Heart Disease by Gender:")
heart_disease_by_sex = df.groupby('sex')['target'].agg(['count', 'sum', 'mean'])
heart_disease_by_sex.columns = ['Total', 'Heart_Disease_Count', 'Heart_Disease_Rate']
print(heart_disease_by_sex)

print("\n" + "=" * 60)
print("5. BLOOD PRESSURE ANALYSIS")
print("=" * 60)

# Blood pressure analysis
print("\n5.1 Blood Pressure Statistics:")
print(f"Mean blood pressure: {df['trestbps'].mean():.2f}")
print(f"Median blood pressure: {df['trestbps'].median():.2f}")
print(f"Blood pressure range: {df['trestbps'].min()} - {df['trestbps'].max()}")

print("\n5.2 Blood Pressure Categories:")
df['bp_category'] = pd.cut(df['trestbps'], 
                          bins=[0, 120, 130, 140, 160, 300],
                          labels=['Normal', 'Elevated', 'High1', 'High2', 'Crisis'])
bp_target = pd.crosstab(df['bp_category'], df['target'])
print(bp_target)

print("\n5.3 Blood Pressure by Target:")
print(df.groupby('target')['trestbps'].describe())

print("\n" + "=" * 60)
print("6. CHOLESTEROL ANALYSIS")
print("=" * 60)

# Cholesterol analysis
print("\n6.1 Cholesterol Statistics:")
print(f"Mean cholesterol: {df['chol'].mean():.2f}")
print(f"Median cholesterol: {df['chol'].median():.2f}")
print(f"Cholesterol range: {df['chol'].min()} - {df['chol'].max()}")

print("\n6.2 Cholesterol Categories:")
df['chol_category'] = pd.cut(df['chol'], 
                            bins=[0, 200, 240, 300, 1000],
                            labels=['Normal', 'Borderline', 'High', 'Very_High'])
chol_target = pd.crosstab(df['chol_category'], df['target'])
print(chol_target)

print("\n6.3 Cholesterol by Target:")
print(df.groupby('target')['chol'].describe())

print("\n" + "=" * 60)
print("7. HEART RATE ANALYSIS")
print("=" * 60)

# Heart rate analysis
print("\n7.1 Heart Rate Statistics:")
print(f"Mean heart rate: {df['thalach'].mean():.2f}")
print(f"Median heart rate: {df['thalach'].median():.2f}")
print(f"Heart rate range: {df['thalach'].min()} - {df['thalach'].max()}")

print("\n7.2 Heart Rate by Target:")
print(df.groupby('target')['thalach'].describe())

print("\n7.3 Heart Rate Categories:")
df['hr_category'] = pd.cut(df['thalach'], 
                          bins=[0, 60, 100, 140, 300],
                          labels=['Bradycardia', 'Normal', 'Tachycardia', 'Very_High'])
hr_target = pd.crosstab(df['hr_category'], df['target'])
print(hr_target)

print("\n" + "=" * 60)
print("8. CORRELATION ANALYSIS")
print("=" * 60)

# Correlation analysis
print("\n8.1 Correlation with Target:")
correlations = df.corr()['target'].sort_values(ascending=False)
print(correlations)

print("\n8.2 Top 5 Positive Correlations with Target:")
print(correlations.head(6))  # Including target itself

print("\n8.3 Top 5 Negative Correlations with Target:")
print(correlations.tail(5))

print("\n" + "=" * 60)
print("9. MULTIVARIATE ANALYSIS")
print("=" * 60)

# Multivariate analysis
print("\n9.1 Age and Gender Analysis:")
age_sex_target = df.groupby(['sex', 'age_group'])['target'].mean().unstack()
print(age_sex_target)

print("\n9.2 Blood Pressure and Cholesterol Analysis:")
bp_chol_target = df.groupby(['bp_category', 'chol_category'])['target'].mean().unstack()
print(bp_chol_target)

print("\n9.3 Chest Pain Type Analysis:")
cp_target = pd.crosstab(df['cp'], df['target'])
print("Chest Pain Type vs Target:")
print(cp_target)

print("\n" + "=" * 60)
print("10. NUMERICAL OPERATIONS WITH NUMPY")
print("=" * 60)

# Numpy operations
print("\n10.1 Numpy Array Operations:")
age_array = np.array(df['age'])
chol_array = np.array(df['chol'])
bp_array = np.array(df['trestbps'])

print(f"Age array shape: {age_array.shape}")
print(f"Age array mean (numpy): {np.mean(age_array):.2f}")
print(f"Age array std (numpy): {np.std(age_array):.2f}")
print(f"Age array median (numpy): {np.median(age_array):.2f}")

print("\n10.2 Statistical Calculations with Numpy:")
print(f"Age percentiles (25%, 50%, 75%): {np.percentile(age_array, [25, 50, 75])}")
print(f"Cholesterol percentiles (25%, 50%, 75%): {np.percentile(chol_array, [25, 50, 75])}")

print("\n10.3 Z-Score Calculations:")
age_zscore = np.abs((age_array - np.mean(age_array)) / np.std(age_array))
chol_zscore = np.abs((chol_array - np.mean(chol_array)) / np.std(chol_array))
print(f"Number of age outliers (z-score > 2): {np.sum(age_zscore > 2)}")
print(f"Number of cholesterol outliers (z-score > 2): {np.sum(chol_zscore > 2)}")

print("\n10.4 Correlation Matrix with Numpy:")
numeric_cols = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'target']
corr_matrix = np.corrcoef(df[numeric_cols].T)
print("Correlation matrix (numpy):")
print(corr_matrix)

print("\n" + "=" * 60)
print("11. CONDITIONAL ANALYSIS")
print("=" * 60)

# Conditional analysis
print("\n11.1 High Risk Patients (Age > 60, BP > 140, Chol > 240):")
high_risk = df[(df['age'] > 60) & (df['trestbps'] > 140) & (df['chol'] > 240)]
print(f"Number of high-risk patients: {len(high_risk)}")
print(f"High-risk patients with heart disease: {high_risk['target'].sum()}")
print(f"High-risk heart disease rate: {high_risk['target'].mean():.2%}")

print("\n11.2 Young Patients with Heart Disease (Age < 40):")
young_heart = df[(df['age'] < 40) & (df['target'] == 1)]
print(f"Number of young patients with heart disease: {len(young_heart)}")
print(f"Average age of young heart disease patients: {young_heart['age'].mean():.2f}")

print("\n11.3 Gender Differences in Heart Disease by Age Group:")
gender_age_analysis = df.groupby(['sex', 'age_group'])['target'].agg(['count', 'sum', 'mean'])
print(gender_age_analysis)

print("\n" + "=" * 60)
print("12. SUMMARY STATISTICS")
print("=" * 60)

# Summary
print("\n12.1 Overall Heart Disease Rate:")
overall_rate = df['target'].mean()
print(f"Overall heart disease rate: {overall_rate:.2%}")

print("\n12.2 Key Findings:")
print(f"- Total patients: {len(df)}")
print(f"- Patients with heart disease: {df['target'].sum()}")
print(f"- Patients without heart disease: {len(df) - df['target'].sum()}")
print(f"- Average age: {df['age'].mean():.1f} years")
print(f"- Male patients: {df['sex'].sum()}")
print(f"- Female patients: {len(df) - df['sex'].sum()}")

print("\n12.3 Risk Factors Summary:")
print("Top risk factors (correlation with target):")
for col, corr in correlations.head(6)[1:]:  # Exclude target itself
    print(f"- {col}: {corr:.3f}")

print("\n" + "=" * 60)
print("ANALYSIS COMPLETE")
print("=" * 60) 