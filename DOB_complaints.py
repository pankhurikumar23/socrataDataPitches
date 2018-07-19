from sodapy import Socrata
from socrata_credentials import app_token

client = Socrata(domain = "data.cityofnewyork.us", app_token = app_token)
complaints_data = []

file = open('DOB_C1.csv', 'w')
try:
    complaints_data += client.get("muk7-ct23", content_type = "csv", disposition_code = "C1")
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