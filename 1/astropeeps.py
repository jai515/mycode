#!/usr/bin/env python3

import requests

space_peeps = requests.get('http://api.open-notify.org/astros.json').json()['people']

num_peeps = len(space_peeps)

print(f"Peeps in space: {num_peeps}")

for person in space_peeps:
    print(f"{person['name']} chillin' on the {person['craft']}")
