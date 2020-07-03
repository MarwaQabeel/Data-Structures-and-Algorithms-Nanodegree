"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

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

def main():
    callers = set([data[0] for data in calls])
    receivers = set([data[1] for data in calls])
    sms_senders = set([data[0] for data in texts])
    sms_receivers = set([data[1] for data in texts])

    telemarketers = []

    for caller in callers:
        if (caller not in receivers and caller not in sms_senders and caller not in sms_receivers):
            telemarketers.append(caller)
    
    telemarketers.sort()

    print("\n These numbers could be telemarketers:")
    for telemarketer in telemarketers:
        print(telemarketer)

if __name__ == "__main__":
    main()
