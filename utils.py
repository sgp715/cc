import csv

def read_links(file_path):

    links = []
    with open(file_path, 'r') as f:
        r = csv.reader(f)
        for row in r:
            links.append(row)

    return links

def save_links(file_path, links):

    with open(file_path, 'w') as f:
        w = csv.writer(f)
        for l in links:
            w.writerow(l)
