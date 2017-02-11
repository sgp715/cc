import json
import requests
from bs4 import BeautifulSoup
import utils
import mail

# get the configurations
with open('./config.json') as f:
    config = json.load(f)


# get all of the cars on the page
base_url = "https://" + config["site"] + ".craigslist.org"

search = "/search/cta"
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
good_links = []
for listing in listings:

    link = base_url + listing.a["href"]
    car_text = requests.get(link).text
    soup = BeautifulSoup(car_text, "html.parser")
    info = soup.find_all("p",{"class":"attrgroup"})

    try:
        car_label = info[0].text.split(' ')
        year = car_label[0]
        if int(year) < 1996:
            continue
        tags = str(info[1].text).split('\n')
    except:
        print "Could not parse -> " + link
        good_links.append(link)
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

        if key == "transmission":
            if val != "automatic":
                send = False

        if key == "odometer":
            if int(val) > 200000:
                send = False

    if send:
        good_links.append(link)

old_links = utils.read_links("links")
utils.save_links("links", good_links)
ones_to_send = list(set(good_links) - set(old_links))

if len(ones_to_send) <= 0:
    print "No new cars to talk about :("
    exit()
message = "These ones have some potential ;)\n\n"
for l in ones_to_send:
    message += (l + '\n')

# send email
mail.send_email(message, "7sebastianperez@gmail.com")

print "SENT:"
print message
