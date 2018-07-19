#######
# Date created: 01/30/2018
# Using Socrata v2.1 and sodapy-1.4.5
#######

# Calls the SocrataAPI to scrape different types of 311 data
# Stores in .csv file

from sodapy import Socrata
from socrata_credentials import app_token

client = Socrata(domain = "data.cityofnewyork.us", app_token = app_token)
complaints_data = []

## Illegal Animals
file = open('311complaints_Animals.csv', 'w')
types = ["Illegal Animal Sold", "Illegal Animal - Sold/Kept"]
for i in types:
    try:
        complaints_data += client.get("fhrw-4uyv", content_type = "csv", complaint_type = i)
    except Exception:
        pass
    print("Writing to file...")
    for complaint in complaints_data:
        line = ""
        # print(complaint)
        for word in complaint:
            # print("x" + word)
            line += word
            line += ","
        file.write(line)
        file.write("\n")
    complaints_data = []
file.close()

## Plumbing
file = open('311complaints_Plumbing.csv', 'w')
types = ["Plumbing", "PLUMBING", "Water System", "Water Quality", "Water Maintenance", "WATER LEAK", "Indoor Sewage", "Home Repair", "HEAT/HOT WATER"]
for i in types:
    try:
        complaints_data += client.get("fhrw-4uyv", content_type="csv", complaint_type=i)
    except Exception:
        pass
    print("Writing to file...")
    for complaint in complaints_data:
        line = ""
        # print(complaint)
        for word in complaint:
            # print("x" + word)
            line += word
            line += ","
        file.write(line)
        file.write("\n")
    complaints_data = []
file.close()

## Department
file = open('311complaints_Dept.csv', 'w')
types = ["DOB", "HPD", "DEP", "DOHMH"]
for i in types:
    try:
        complaints_data += client.get("fhrw-4uyv", content_type = "csv", agency = i)
    except Exception:
        pass
    print("Writing to file...")
    for complaint in complaints_data:
        line = ""
        # print(complaint)
        for word in complaint:
            # print("x" + word)
            line += word
            line += ","
        file.write(line)
        file.write("\n")
    complaints_data = []
file.close()

# LinkNYC
file = open('311complaints_LinkNYC.csv', 'w')

try:
    complaints_data += client.get("fhrw-4uyv", content_type = "csv", complaint_type = "LinkNYC")
except Exception:
    pass
print("Writing to file...")
for complaint in complaints_data:
    line = ""
    # print(complaint)
    for word in complaint:
        # print("x" + word)
        line += word
        line += ","
    file.write(line)
    file.write("\n")
complaints_data = []
file.close()

## Ewaste
file = open('311complaints_EWaste.csv', 'w')

try:
    complaints_data += client.get("fhrw-4uyv", content_type = "csv", complaint_type = "Electronics Waste")
except Exception:
    pass
print("Writing to file...")
for complaint in complaints_data:
    line = ""
    # print(complaint)
    for word in complaint:
        # print("x" + word)
        line += word
        line += ","
    file.write(line)
    file.write("\n")
complaints_data = []
file.close()

## Compliment
file = open('311complaints_Compliments.csv', 'w')

try:
    complaints_data += client.get("fhrw-4uyv", content_type = "csv", complaint_type = "Compliment")
except Exception:
    pass
print("Writing to file...")
for complaint in complaints_data:
    line = ""
    # print(complaint)
    for word in complaint:
        # print("x" + word)
        line += word
        line += ","
    file.write(line)
    file.write("\n")
complaints_data = []
file.close()