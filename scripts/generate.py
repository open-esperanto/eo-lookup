import os
import sys
import json
import sqlite3

DB_PATH = os.environ['DB_PATH']


def get_dictionary():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    trans = {}
    for code, en in c.execute("SELECT mrk, txt FROM traduko WHERE lng = 'en'"):
        trans[code] = en

    dictionary = {}
    for code, eo in c.execute("SELECT mrk, kap FROM nodo"):
        if ' ' not in eo and code in trans:
            en = trans[code]
            if eo not in dictionary:
                dictionary[eo] = []
            if en not in dictionary[eo]:
                dictionary[eo].append(en)
    return dictionary


if __name__ == '__main__':
    sys.stdout.write(json.dumps(get_dictionary()))
