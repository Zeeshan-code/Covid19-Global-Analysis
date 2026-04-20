import pandas as pd

# Load data
df = pd.read_csv(r'C:\Users\zeekh\OneDrive\Desktop\covid_project\compact.csv',
                 low_memory=False)

# Fix date
df['date'] = pd.to_datetime(df['date'])

# Remove non-country rows (continents and income groups)
remove = [
    'World', 'Europe', 'Asia', 'Africa',
    'North America', 'South America', 'Oceania',
    'European Union', 'High income', 'Low income',
    'Upper middle income', 'Lower middle income', 'International'
]
df = df[~df['country'].isin(remove)]
df = df[df['continent'].notna()]

# Select only useful columns (using YOUR exact column names)
cols = [
    'country', 'code', 'continent', 'date',
    'total_cases', 'new_cases', 'new_cases_smoothed',
    'total_deaths', 'new_deaths', 'new_deaths_smoothed',
    'total_cases_per_million', 'total_deaths_per_million',
    'people_fully_vaccinated', 'people_fully_vaccinated_per_hundred',
    'total_vaccinations_per_hundred',
    'positive_rate', 'reproduction_rate',
    'stringency_index', 'population',
    'gdp_per_capita', 'median_age', 'life_expectancy',
    'human_development_index'
]
df = df[cols]

# Rename for clarity
df = df.rename(columns={
    'people_fully_vaccinated_per_hundred': 'vax_rate',
    'total_cases_per_million': 'cases_per_million',
    'total_deaths_per_million': 'deaths_per_million',
})

# Calculate death rate
df['death_rate'] = (
    df['total_deaths'] / df['total_cases'] * 100
).round(4)

# Add time columns
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['year_month'] = df['date'].dt.to_period('M').astype(str)

# Fill numeric nulls with 0
num_cols = [
    'total_cases', 'new_cases', 'new_cases_smoothed',
    'total_deaths', 'new_deaths', 'new_deaths_smoothed',
    'cases_per_million', 'deaths_per_million',
    'vax_rate', 'death_rate'
]
df[num_cols] = df[num_cols].fillna(0)

# Print summary
print("=== CLEANED DATA SUMMARY ===")
print("Shape:", df.shape)
print("Date range:", df['date'].min(), "to", df['date'].max())
print("Countries:", df['country'].nunique())
print("Continents:", df['continent'].unique())

print("\n=== TOP 10 COUNTRIES BY TOTAL CASES ===")
top = df.groupby('country')[['total_cases','total_deaths']].max()
top['death_rate'] = (top['total_deaths'] / top['total_cases'] * 100).round(2)
print(top.sort_values('total_cases', ascending=False).head(10).to_string())

print("\n=== CASES & DEATHS BY CONTINENT ===")
cont = df.groupby('continent').agg(
    countries=('country','nunique'),
    total_cases=('total_cases','max'),
    total_deaths=('total_deaths','max')
).reset_index()
print(cont.sort_values('total_cases', ascending=False).to_string())

print("\n=== AVG DEATH RATE BY CONTINENT ===")
dr = df[df['death_rate'] > 0].groupby('continent')['death_rate'].mean().round(2)
print(dr.sort_values(ascending=False))

print("\n=== VACCINATION RATE — TOP & BOTTOM 10 ===")
vax = df.groupby('country')['vax_rate'].max().reset_index()
vax = vax[vax['vax_rate'] > 0].sort_values('vax_rate', ascending=False)
print("TOP 10 vaccinated:")
print(vax.head(10).to_string())
print("\nLOWEST 10 vaccinated:")
print(vax.tail(10).to_string())

print("\n=== YEARLY GLOBAL NEW CASES ===")
yearly = df.groupby('year')['new_cases'].sum().reset_index()
yearly['new_cases'] = yearly['new_cases'].apply(lambda x: f"{x:,.0f}")
print(yearly.to_string())

# Save full cleaned file
df.to_csv(
    r'C:\Users\zeekh\OneDrive\Desktop\covid_project\covid_clean.csv',
    index=False
)

# Save latest snapshot per country (for Tableau map)
latest = (df.sort_values('date')
            .groupby('country')
            .last()
            .reset_index())
latest.to_csv(
    r'C:\Users\zeekh\OneDrive\Desktop\covid_project\covid_latest.csv',
    index=False
)

print("\nDone! Both files saved.")