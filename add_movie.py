import csv


# Opens file, then checks if movie exists.  If not it adds the movie to the list

name = "Superman"
x = 0


with open('sample.csv', 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)

    for line in csv_reader:
        #print(line)
        #print(x)
        if line['title'] != name:
            x = x + 0
        else:
            x += 1

    if x == 1:
        print('[!] NO UPDATE: {} is in the list'.format(name))
    elif x == 0:
        print('Adding "{}" to the list'.format(name))

        with open('sample.csv', 'a') as csvfile:
            fieldnames = ['title', 'year', 'rank', 'rating', 'bo']
            csv_append = csv.DictWriter(csvfile, fieldnames=fieldnames, )

            csv_append.writerow({'title' : name})







