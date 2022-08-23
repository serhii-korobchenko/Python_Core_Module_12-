import csv

with open ('eggs.csv', 'w', newline='') as  fh:
    spam_writer = csv.writer(fh)
    spam_writer.writerow(['Spam'] * 5 + ['Bakd beans'])
    spam_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

with open ('eggs.csv', newline='') as fh:
    spam_reader = csv.reader(fh)
    for row in spam_reader:
        print(', '.join(row))



