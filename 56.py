ages = {
    "sama": 30,
    "ali": 15,
    "sepehr": 24,
    "kamran": 32,
    "roya": 19,
    "zamyar": 20
}

maxage = max(ages.values())

for i in ages:
    if ages[i] == maxage:
        print(i)
