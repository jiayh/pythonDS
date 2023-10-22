"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    # list of texting records: calling and receiving numbers, and timestamp
    texts = list(reader)  # Type List[List[string, string, string]]

# Retrieve phone numbers that send and receive text
non_call_sender = []
for item in texts:
    non_call_sender.append(item[0])
    non_call_sender.append(item[1])

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# Retrieve phone numbers that make calls and receive calls into separate list, respectively.
call_sender = []
for item in calls:
    call_sender.append(item[0])
    non_call_sender.append(item[1])

# Remove duplication
callers = set(call_sender)
others = set(non_call_sender)

# Telemarketers are in "callers" set but NOT in "others" set.
telemarketer = callers.difference(others)

sorted_telemarketer = sorted(telemarketer)
print("These numbers could be telemarketers: ")
for item in sorted_telemarketer:
    print(item)


"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

