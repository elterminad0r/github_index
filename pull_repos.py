import json
import sys

for repo in json.load(sys.stdin):
    print("{0[name]}\t{0[html_url]}\t{0[description]}".format(repo))
