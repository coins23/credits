import json
import re

with open('./kdb.json', 'r', encoding='utf8') as f:
    kdb = json.load(f)

cources = kdb['subject']

items = [
    {
        'name': '専門科目 - 必修科目 - 実験',
        'creditCount': 6,
        'courses': [
            'GB26403', 'GB26503',
            'GB36403', 'GB36503',
            'GB46403', 'GB46503',
        ],
        'filter': '',
    },
    {
        'name': '専門科目 - 必修科目 - 卒業研究',
        'creditCount': 6,
        'courses': ['GB19948', 'GB19958', 'GB19848', 'GB19858'],
        'filter': '',
    },
    {
        'name': '専門科目 - 必修科目 - 専門語学',
        'creditCount': 4,
        'courses': ['GB19091', 'GB19101'],
        'filter': '',
    },
    {
        'name': '専門科目 - 選択科目 - GB20,GB30,GB40で始まる科目',
        'creditCount': 16,
        'courses': [],
        'filter': '^(GB20|GB30|GB40)[0-9A-Z]+$',
    },
    {
        'name': '専門科目 - 選択科目 - GB2,GB3,GB4で始まる科目',
        'creditCount': 0,
        'courses': [],
        'filter': '^(GB2|GB3|GB4)[0-9A-Z]+$',
    },
    {
        'name': '専門基礎科目 - 必修科目',
        'creditCount': 26,
        'courses': [
            "GA15211",
            "GA15221",
            "GB10234",
            "GB10244",
            "GA15311",
            "GA15321",
            "GB10444",
            "GB10454",
            "GA15111",
            "GA15121",
            "GB19061",
            "GA18212",
            "GA18312",
            "GB11964",
            "GB11931",
            "GB11956",
            "GB11966",
            "GB10804",
            "GB12017",
        ],
        'filter': '',
    },
    {
        'name': '専門基礎科目 - 選択科目 - 1',
        'creditCount': 8,
        'courses': [
            "GB11601",
            "GB11621",
            "GB12301",
            "GB12601",
            "GB12801",
            "GB12812",
        ],
        'filter': '',
    },
    {
        'name': '専門基礎科目 - 選択科目 - 2',
        'creditCount': 2,
        'courses': [
            "GB13614",
            "GB13624"
        ],
        'filter': '',
    },
    {
        'name': '専門基礎科目 - 選択科目 - GB1で始まる科目',
        'creditCount': 4,
        'courses': [],
        'filter': '^GB1[0-9]+$',
    },
    {
        'name': '専門基礎科目 - 選択科目 - GA1で始まる科目',
        'creditCount': 8,
        'courses': [],
        'filter': '^GA1[0-9]+$',
    },
    {
        'name': '基礎科目 - 共通科目 - 必修科目 - 総合科目',
        'creditCount': 2,
        'courses': [
            '1118102',
            '1118202',
            '1118302',
            '1118402',
            '1227571',
            '1227581',
            '1227591',
            '1227601',
        ],
        'filter': '',
    },
    {
        'name': '基礎科目 - 共通科目 - 必修科目 - 体育',
        'creditCount': 2,
        'courses': [ ],
        'filter': '^2[0-9A-Z]+$',
    },
    {
        'name': '基礎科目 - 共通科目 - 必修科目 - 外国語（英語）',
        'creditCount': 4,
        'courses': [ ],
        'filter': '^31[0-9A-Z]+$',
    },
    {
        'name': '基礎科目 - 共通科目 - 必修科目 - 情報',
        'creditCount': 4,
        'courses': [ ],
        'filter': "^6[0-9A-Z]+$",
    },
    {
        'name': '基礎科目 - 共通科目 - 選択科目 - 学士基盤科目',
        'creditCount': 1,
        'courses': [],
        'filter': "^(12|14)[0-9A-Z]+$",
    },
    {
        'name': '基礎科目 - 共通科目 - 選択科目 - 体育/外国語/国語/芸術',
        'creditCount': 0,
        'courses': [],
        'filter': "^(2|3|4|5)[0-9A-Z]+$",
    },
    {
        'name': '専門科目 - 関連科目 - 選択科目 - 「E,F,G,Hで始まる科目、共通科目及び教職に関する科目」以外の科目',
        'creditCount': 6,
        'courses': [],
        'filter': "[^1234569EFGH][0-9A-Z]+",
    },
    {
        'name': '専門科目 - 関連科目 - 選択科目 - E,F,GC,GE,Hで始まる科目',
        'creditCount': 0,
        'courses': [],
        'filter': "^(E|F|GC|GE|H)[0-9A-Z]+$",
    }
]


requirements = []

for item in items:
    req = {}
    req['name'] = item['name']
    req['description'] = ''
    req['creditCount'] = item['creditCount']
    courses = []
    if item['courses']:
        courses = item['courses']
    elif item['filter']:
        courses = list(filter(lambda c: re.match(
            item['filter'], c), map(lambda c: c[0], cources)))
    req['courses'] = courses

    requirements.append(req)


with open('./coins23.json', 'w', encoding='utf8') as f:
    json.dump({
        'name': '卒業に必要な履修科目',
        'decription': '',
        'children': requirements,
    }, f, ensure_ascii=False)
