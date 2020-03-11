import csv
import json

results = {}

with open('instructions.csv') as infile:
    reader = csv.reader(infile)

    for row in reader:
        project, key, value, code = row
        if project not in results:
            results[project] = {
                'title': '',
                'description': '',
                'websiteUrl': '',
                'hints': [],
                'instructions': []
            }

        if key in ["hints", "instructions"]:
            results[project][key].append({'text': value, 'code': code})
        else:
            results[project][key] = value

with open('exercises.json', 'w') as outfile:
    outfile.write(json.dumps(results))

