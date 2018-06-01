import csv

with open ('answers.csv', 'r', encoding='utf-8') as file:
    fields = ['hi', 'how r u', 'bye']
    reader = csv.DictReader(file, fields, delimiter = ';')

    for row in reader:
        print(row)