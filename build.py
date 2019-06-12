import csv
import json

csvfile = open('C:/Users/Ashok/Desktop/builds.csv', 'r')
jsonfile = open('C:/Users/Ashok/Desktop/buildfile.json', 'w')

fieldnames = ("project","build")
reader = csv.DictReader( csvfile, fieldnames)
out = json.dumps( [ row for row in reader ] )
jsonfile.write(out)