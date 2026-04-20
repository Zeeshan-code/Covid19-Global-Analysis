import pandas as pd

df = pd.read_csv(r'C:\Users\zeekh\OneDrive\Desktop\covid_project\compact.csv',
                 low_memory=False)

print("Shape:", df.shape)
print("\nAll columns:")
for col in df.columns:
    print(" -", col)
print("\nFirst 3 rows:")
print(df.head(3).to_string())
print("\nNull counts:")
print(df.isnull().sum().sort_values(ascending=False).head(20))