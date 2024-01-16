import pandas as pd


df = pd.read_csv('Datasets/Airline Dataset.csv')  

# first name və last name - i concatenate edərək full name yaradın.
df['Full Name'] = df['First Name'] + ' ' + df['Last Name']
print(df)

# Departure Date-i DateTime formatina cevirin
df['Departure Date'] = pd.to_datetime(df['Departure Date'])
print(df)

# Yaşı 50 və üzəri olan və US- dən səyahət edən bütün recordları tapın
us = df[(df['Age'] >= 50) & (df['Airport Country Code'] == 'US')]
print(us)

# Yaşa görə desc order ilə sıralayın
sorted= us.sort_values(by='Age', ascending=False)
print(sorted)

# Flight statusa görə qruplaşdırın və hər statusa görə ortalama sərnişin yaşının ortalamasını tapıns
average = df.groupby('Flight Status')['Age'].mean()
print(average)

# Create a new column 'Age Group' to categorize passengers into 'Youth' (age < 30), 'Adult' (30 ≤ age < 60), and 'Senior' (age ≥ 60).
# Age Group deyə yeni kateqorik sütun yaradın. Youth 30 dan azdırsa Adult 30 a bərabər və ya 60 dan azdırsa Adult , 60 a bərabər və 60 dan yuxarıdırsa Senior olaraq status versin.
def age_group(age):
    if age < 30:
        return 'Youth'
    elif 30 <= age < 60:
        return 'Adult'
    else:
        return 'Senior'
df['Age Group'] = df['Age'].apply(age_group)
print(df)

# ən çox departure olan 3 ölkəni tapın
top_countries = df['Country Name'].value_counts().head(3)
print(top_countries)

# Senior sərnişinlərin ən çox getdiyi destination- ları tapın
senior_destinations = df[df['Age Group'] == 'Senior']['Arrival Airport'].value_counts().head()
print(senior_destinations)

# Delay statusunda olan gedişlərin faizini totala nisbətən tapın.
delayed_percentage = (df['Flight Status'] == 'Delayed').mean() * 100
print(delayed_percentage)

