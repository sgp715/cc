def read_links(file_path):

    links = []
    with open(file_path, 'r') as f:
        l = f.readline()
        while l:
            links.append(l[:-1])
            l = f.readline()

    return links

def save_links(file_path, links):

    with open(file_path, 'w') as f:
        f.seek(0)
        f.truncate()
        for l in links:
            f.write("%s\n" % l)
