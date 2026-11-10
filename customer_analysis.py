# Customer data analysis using Python file handling
# Read the file once and store every record in a list
customers = []
with open("customer_data.txt", "r") as f:
    for line in f:
        customers.append(line.strip().split(","))
# Columns: 0 id | 1 first name | 2 last name | 3 age | 4 gender
#          5 city | 6 country | 7 profession
# 1. Display all records
print("1. All records")
for c in customers:
    print(c)
# 2. Age above 50
print("\n2. Age above 50")
for c in customers:
    if int(c[3]) > 50:
        print(c)
# 3. Age below 25
print("\n3. Age below 25")
for c in customers:
    if int(c[3]) < 25:
        print(c)
# 4. Age between 25 and 40
print("\n4. Age between 25 and 40")
for c in customers:
    if 25 <= int(c[3]) <= 40:
        print(c)
# 5. People from India
print("\n5. From India")
for c in customers:
    if c[6] == "India":
        print(c)
# 6. All Doctors
print("\n6. Doctors")
for c in customers:
    if c[7] == "Doctor":
        print(c)

# 7. All Engineers
print("\n7. Engineers")
for c in customers:
    if c[7] == "Engineer":
        print(c)

# 8. People from the UK
print("\n8. From the UK")
for c in customers:
    if c[6] == "UK":
        print(c)

# 9. Doctors from India
print("\n9. Doctors from India")
for c in customers:
    if c[7] == "Doctor" and c[6] == "India":
        print(c)

# 10. Doctors from the UK
print("\n10. Doctors from the UK")
for c in customers:
    if c[7] == "Doctor" and c[6] == "UK":
        print(c)

# 11. Pilots above age 40
print("\n11. Pilots above 40")
for c in customers:
    if c[7] == "Pilot" and int(c[3]) > 40:
        print(c)

# 12. First name, age and profession of all females
print("\n12. Females: name, age, profession")
for c in customers:
    if c[4] == "Female":
        print(c[1], c[3], c[7])

# 13. People living in Kochi
print("\n13. Living in Kochi")
for c in customers:
    if c[5] == "Kochi":
        print(c)

# 14. Total number of Doctors
doctor_count = 0
for c in customers:
    if c[7] == "Doctor":
        doctor_count += 1
print("\n14. Total doctors:", doctor_count)

# 15. Count of each profession
profession_count = {}
for c in customers:
    profession_count[c[7]] = profession_count.get(c[7], 0) + 1
print("\n15. Profession count:", profession_count)

# 16. Count of each country
country_count = {}
for c in customers:
    country_count[c[6]] = country_count.get(c[6], 0) + 1
print("\n16. Country count:", country_count)

# 17 & 18. Oldest and youngest person
ages = [int(c[3]) for c in customers]
oldest_age = max(ages)
youngest_age = min(ages)

print("\n17. Oldest person")
for c in customers:
    if int(c[3]) == oldest_age:
        print(c)

print("\n18. Youngest person")
for c in customers:
    if int(c[3]) == youngest_age:
        print(c)

# 19. Average age
average_age = sum(ages) / len(ages)
print("\n19. Average age:", average_age)

# 20. Indian Engineers or Doctors older than 30
print("\n20. Indian Engineers/Doctors above 30")
for c in customers:
    if c[6] == "India" and int(c[3]) > 30 and (c[7] == "Engineer" or c[7] == "Doctor"):
        print(c[1], c[2], c[3], c[5], c[7])