import os, csv

TOPICS_FILE_PATH = os.getenv('TOPICS_FILE_PATH')

topics = {}
with open(TOPICS_FILE_PATH, encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        category, theme = row
        topics[theme]  = category