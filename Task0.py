"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    # list of texting records: calling and receiving numbers, and timestamp
    texts = list(reader)  # Type List[List[string, string, string]]
    if len(texts) > 0:
        print(f'First record of texts, {texts[0][0]} texts {texts[0][1]} at time {texts[0][2]}')

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    # list of calling records: calling and receiving numbers, timestamp, duration
    calls = list(reader)  # Type List[List[string, string, string, string]]
    if len(calls) > 0:
        lastCall = len(calls) - 1
        print(f'Last record of calls, {calls[lastCall][0]} calls {calls[lastCall][1]}'
              f' at time {calls[lastCall][2]}, lasting {calls[lastCall][3]} seconds')

"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
