#to read data
import csv
# for calculations on the data
import numpy as np
import matplotlib.pyplot as plotlib
import statistics
# for conversion of time to Unix timestamp
from datetime import datetime
import time

# Opening my csv and creating a DictReader
myFile = open("DOB_C2.csv", 'rU')
DOBData = csv.DictReader(myFile)

# creating a new data set of just the plumbing complaints, to prevent excess memory usage
# row_names are "complaint_type", "created_date" and "closed_date"
communityBoard = []
for row in DOBData:
    # some of the plumbing complaints are still open, so there is no closed date
    # hence putting in a try-except statement
    try:
        # convert API's datetime representation to datetime, and then Unix timestamp
        # and then subtract to get time to response
        communityBoard.append(int(row['community_board']))
    except:
        pass

# zipHistogram = plotlib.hist(communityBoard, bins = 200, histtype='bar', color=['green'])


myFile = open("DOB_C1.csv", 'rU')
DOBData = csv.DictReader(myFile)

# creating a new data set of just the plumbing complaints, to prevent excess memory usage
# row_names are "complaint_type", "created_date" and "closed_date"
communityBoard = []
for row in DOBData:
    # some of the plumbing complaints are still open, so there is no closed date
    # hence putting in a try-except statement
    try:
        # convert API's datetime representation to datetime, and then Unix timestamp
        # and then subtract to get time to response
        communityBoard.append(int(row['community_board']))
    except:
        pass

# zip2Histogram = plotlib.hist(communityBoard, bins = 200, histtype='bar', color=['green'])

myFile = open("DOB_Active.csv", 'rU')
DOBData = csv.DictReader(myFile)

# creating a new data set of just the plumbing complaints, to prevent excess memory usage
# row_names are "complaint_type", "created_date" and "closed_date"
communityBoard = []
for row in DOBData:
    # some of the plumbing complaints are still open, so there is no closed date
    # hence putting in a try-except statement
    try:
        if (row['inspection_date'] == ""):
            communityBoard.append(int(row['community_board']))
    except:
        pass

zip2Histogram = plotlib.hist(communityBoard, bins = 200, histtype='bar', color=['green'])

plotlib.show()