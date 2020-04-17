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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

def main():
    numbers=[]

    for num in range(len(texts)):
        for i in range(2):
            # collecting incomming and answering numbers
            numbers.append(texts[num][i])

    for num in range(len(calls)):
        for i in range(2):
            numbers.append(calls[num][i])    

    phonenumbers = set(numbers)

    print("There are {} different telephone numbers in the records.".format(len(phonenumbers)))

if __name__ == '__main__':
    main()