import pandas

# read a csv file, skipping the last line
rats = pandas.read_csv('~/Downloads/rats.csv', skipfooter=1)

print(rats.describe())

# investigate values of a certain field
print(rats['Current Activity'].unique())

# filter data
crew_dispatched = rats[rats['Current Activity'] == 'Dispatch Crew']
print(len(crew_dispatched))

# find 10 most rat-infested Zip codes in Chicago
print(crew_dispatched['ZIP Code'].value_counts().nlargest(10))

# group by completion date
dates = crew_dispatched.groupby('Completion Date')
print(dates)
print(len(dates))

# determine counts on each day
date_counts = dates.size()
print(date_counts[0:10])

# sort the counts
date_counts.sort_values(inplace=True)
print(date_counts[-10:])
