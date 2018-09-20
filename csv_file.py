import csv


name = "Green Room"
x = 0
with open('sample.csv', 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)

    for line in csv_reader:
        #print(line)
        #print(x)
        if line['title'] != name:
            x = x + 0
        else:
            x = x + 1
    print(x)
    if x == 1:
        print('{} is in the list'.format(name))
    elif x == 0:
        print('Adding "{}" to the list'.format(name))

        with open('sample.csv', 'a') as csvfile:
            fieldnames = ['title', 'year', 'rank', 'rating', 'bo']
            csv_append = csv.DictWriter(csvfile, fieldnames=fieldnames, )

            csv_append.writerow({'title' : name, 'year' : '2017', 'rank' : '100', 'rating' : 'R'})







