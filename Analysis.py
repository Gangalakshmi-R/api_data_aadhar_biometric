import pandas as pd


import glob

df = pd.read_csv("api_data_aadhar_biometric_0_500000.csv")

df.head()

df.shape

df.columns

df.info()

df.isna().sum()

df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')

df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month

df[['date', 'year', 'month']].head()

"""AGE-WISE BIOMETRIC UPDATE ANALYSIS"""

df.columns

age_total = df[['bio_age_5_17', 'bio_age_17_']].sum()
age_total

import matplotlib.pyplot as plt

age_total.plot(kind='bar', figsize=(6,4))
plt.title("Biometric Updates by Age Group (2025)")
plt.xlabel("Age Group")
plt.ylabel("Number of Updates")
plt.show()

"""STATE-WISE ADULT BIOMETRIC LOAD"""

state_adult = df.groupby('state')['bio_age_17_'].sum().sort_values(ascending=False)
state_adult.head(10)

state_adult.head(10).plot(kind='bar', figsize=(9,5))
plt.title("Top States by Adult Biometric Updates (2025)")
plt.xlabel("State")
plt.ylabel("Total Updates (17+)")
plt.show()

"""MONTH-WISE SEASONALITY"""

month_adult = df.groupby('month')['bio_age_17_'].sum()
month_adult

month_adult.plot(marker='o', figsize=(8,4))
plt.title("Month-wise Adult Biometric Updates (2025)")
plt.xlabel("Month")
plt.ylabel("Updates")
plt.grid(True)
plt.show()

"""DISTRICT-WISE DEEP DIVE"""

district_adult = (
    df.groupby(['state', 'district'])['bio_age_17_']
    .sum()
    .reset_index()
    .sort_values(by='bio_age_17_', ascending=False)
)

district_adult.head(10)

top_districts = district_adult.head(15)

plt.figure(figsize=(10,6))
plt.barh(
    top_districts['district'],
    top_districts['bio_age_17_']
)
plt.xlabel("Adult Biometric Updates (17+)")
plt.ylabel("District")
plt.title("Top 15 Districts by Adult Biometric Updates (2025)")
plt.gca().invert_yaxis()
plt.show()

"""PINCODE-LEVEL HOTSPOT ANALYSIS"""

pincode_adult = (
    df.groupby('pincode')['bio_age_17_']
    .sum()
    .reset_index()
    .sort_values(by='bio_age_17_', ascending=False)
)

pincode_adult.head(10)

top_pincodes = pincode_adult.head(20)

plt.figure(figsize=(10,6))
plt.bar(
    top_pincodes['pincode'].astype(str),
    top_pincodes['bio_age_17_']
)
plt.xticks(rotation=90)
plt.xlabel("Pincode")
plt.ylabel("Adult Biometric Updates (17+)")
plt.title("Top 20 Pincode-Level Biometric Update Hotspots (2025)")
plt.show()