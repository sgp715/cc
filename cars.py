import json
import requests
from bs4 import BeautifulSoup
import utils
import mail
import pandas as pd

# get the configurations
with open('./config.json') as f:
    config = json.load(f)


# get all of the cars on the page
base_url = "https://" + config["site"] + ".craigslist.org"

search = "/search/cto"
html = requests.get(base_url + search).text
soup = BeautifulSoup(html, "html.parser")
listings = soup.find_all("li", { "class" : "result-row" })

tags_list = ["cylinders",
        "title status",
        "VIN",
        "drive",
        "odometer",
        "transmission",
        "paint color",
        "fuel",
        "type",
        "condition",
        "size"]

# iterate through here and find the ones we wanna send
good_ones = {"car_labels":[], "links":[], "prices": []}
for listing in listings:

    link = base_url + listing.a["href"]
    car_text = requests.get(link).text
    soup = BeautifulSoup(car_text, "html.parser")
    info = soup.find_all("p",{"class":"attrgroup"})

    try:
        price = soup.find_all("span", {"class":"price"})[0].text
    except:
        print "Couldn't find price"
        print link
        price = ''

    try:
        car_label = info[0].text.strip('\n')
        year = car_label.split(' ')[0]
        if int(year) < 1996:
            continue
        tags = str(info[1].text).split('\n')
    except:
        print "Could not parse -> " + link
        good_ones["car_labels"].append('')
        good_ones["links"].append(link)
        good_ones["prices"].append(price)
        continue

    send = True
    for tag in tags:

        pair = tag.split(':')
        if len(pair) != 2:
            continue

        key = pair[0].strip()
        val = pair[1].strip()

        if key == "title status":
            if val.strip() != "clean":
                send = False
                break

        if key == "transmission":
            if val != "automatic":
                send = False
                break

        if key == "odometer":
            if int(val) > 200000:
                send = False
                break

    if send:
        good_ones["car_labels"].append(car_label)
        good_ones["links"].append(link)
        good_ones["prices"].append(price)


# try to read and update old ones if exists
store = "cars_stuff"

try:
    olds = pd.read_pickle(store)
    # remove repeat links
    good_ones = good_ones[good_ones.links != olds.links]
except:
    print "No saved data..."


good_ones = pd.DataFrame(good_ones)
good_ones.to_pickle(store)

if len(good_ones) <= 0:
    print "No new cars to talk about :("
    exit()

for index, row in good_ones.iterrows():
    subject = row["car_labels"] + ' - ' + row["prices"]
    message = row["links"]
    print "Sending email..."
    print "subject: " + subject
    print "message: " + message
    mail.send_email(subject, message)
    #break

# send email
# do some kind of mapping
# mail.send_email(subject, message)
