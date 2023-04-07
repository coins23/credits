import json
import re

with open('./kdb.json', 'r', encoding='utf8') as f:
    kdb = json.load(f)

courses = kdb['subject']

courses = []
for course in kdb['subject']:
    if course[3] == '-':
        creditCount = 0.0
    else:
        creditCount = float(course[3])
    courses.append({
        'code': course[0],
        'title': course[1],
        'creditCount': creditCount,
    })

with open('./courses.json', 'w', encoding='utf8') as f:
    json.dump(courses, f, ensure_ascii=False)
