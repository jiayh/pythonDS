"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    # list of texting records: calling and receiving numbers, and timestamp
    texts = list(reader)  # Type List[List[string, string, string]]

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    # list of calling records: calling and receiving numbers, timestamp, duration
    calls = list(reader)  # Type List[List[string, string, string, string]]

# Retrieve all the phone numbers, both calling and receiving
phones = list()
for item in texts:
    phones.append(item[0])
    phones.append(item[1])

for item in calls:
    phones.append(item[0])
    phones.append(item[1])

# De-dup
phones_unique = set(phones)

print(f"There are {len(phones_unique)} different telephone numbers in the records")

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
