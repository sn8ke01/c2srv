import csv


# Opens file, then if field is populated, if not then update field
# todo: need to read file into a tmp file and load contents into a dict. 
# todo: Iterate over Dict, identify empty fields then update accordingly.

rating = 'R'


with open('sample.csv', 'r') as csvfile:
    csv_reader = csv.DictReader(csvfile)

    for line in csv_reader:
        #print(line)

        if line['rating'] == '':
            #print('[!] {} :Rating field is empty'.format(line['title']))

            with open('sample.csv', 'a') as csvfile:
                fieldnames = ['title', 'year', 'rank', 'rating', 'bo']
                csv_append = csv.DictWriter(csvfile, fieldnames=fieldnames, )
                print('Adding {} rating to {}'.format(rating, line['title']))
                csv_append.writerow({'rating': rating})
