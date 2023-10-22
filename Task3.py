"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re
from typing import Dict, Any

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

# A dictionary of area code of answering phone to the number of calls made to that
# area code.
calls_from_bangalore: dict[str, int] = dict()


def update_calls_by_code(code):
    if code in calls_from_bangalore:
        n_calls = calls_from_bangalore[code]
        calls_from_bangalore.update({code: n_calls + 1})
    else:
        calls_from_bangalore[code] = 1


# Group calls by area code, and keep track of the number of calls
pat_bangalore = r"\(080\)"
pat_fixed = r"\(0\d+\)"
pat_mobile = r"(7|8|9)\d{3}\d+ \d+"
for item in calls:
    if re.match(pat_bangalore, item[0]):
        result = re.match(pat_fixed, item[1])
        if result:
            area_code = result.group()
            update_calls_by_code(area_code)
        else:
            result = re.match(pat_mobile, item[1])
            if result:
                prefix = result.group()[0:4]
                update_calls_by_code(prefix)

sorted_codes = sorted(calls_from_bangalore)
print("The number called by people in Bangalore have codes:")
for item in sorted_codes:
    print(item)

num_calls = calls_from_bangalore.values()
total = 0
for item in num_calls:
    total = total + item
to_bangalore = float(calls_from_bangalore["(080)"])
total = float(total)
percentage = "{:.2%}".format(to_bangalore / total)
print(f"{percentage} percent of calls from fixed lines in Bangalore are calls "
      "to other fixed lines in Bangalore")

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
