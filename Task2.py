"""
Read file into texts and calls.
It's ok if you don't understand how to read files
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

# A Dictionary phone: time-spent that keeps track of the total time a phone spent on calls
call_time_totals = dict()  # Type dict[string : int]


def update_call_time(phone, dur):
    if phone in call_time_totals:
        existing = call_time_totals[phone]
        call_time_totals.update({phone: existing + dur})
    else:
        call_time_totals.update({phone: dur})


# Going through call log to accumulate call time by phone number
for item in calls:
    calling = item[0]
    answering = item[1]
    duration = int(item[3])
    update_call_time(calling, duration)
    update_call_time(answering, duration)

longest = 0
the_phone = ""
for key, value in call_time_totals.items():
    if value > longest:
        longest = value
        the_phone = key

print(f"{the_phone} spent the longest time, {longest} seconds, on the phone during "
      f"September 2016.")

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
