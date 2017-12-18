import os
import sqlite3

VERSION = '1.0'

DB_PATH = os.environ['DB_PATH']
OUT_PATH = os.environ['OUT_PATH']

MODULE_PATH = os.path.join(OUT_PATH, 'eo_lookup_revo.py')
README_PATH = os.path.join(OUT_PATH, 'README.rst')
SETUP_PY_PATH = os.path.join(OUT_PATH, 'setup.py')
MANIFEST_IN_PATH = os.path.join(OUT_PATH, 'MANIFEST.in')

MANIFEST_IN = """
include LICENSE.txt
include README.rst
"""

README_RST = """ReVo content for eo-lookup
==========================

This package contains GPL-licensed content for the eo-lookup tool
taken from `Reta Vortaro <http://www.reta-vortaro.de/revo/>`_.

.. code-block:: python
   >>> import eo_lookup_revo
   >>> eo_lookup_revo.get_content()

"""

SETUP_OPTS = {
    'name': 'eo_lookup_revo',
    'version': VERSION,
    'description': 'GPL-licensed ReVo content for eo-lookup',
    'long_description': README_RST,
    'url': 'https://github.com/open-esperanto/eo-lookup-revo',
    'author': 'Open Esperanto',
    'classifiers': [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 3'
    ],
    'keywords': 'esperanto revo',
    'py_modules': ['eo_lookup_revo']
}

SETUP_PY = """from setuptools import setup

setup(**{})
""".format(repr(SETUP_OPTS))


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


def main():
    dictionary = get_dictionary()
    module_text = 'def get_content():\n    return {}\n'.format(repr(dictionary))

    with open(README_PATH, 'w', encoding='utf-8') as f:
        f.write(README_RST)

    with open(SETUP_PY_PATH, 'w', encoding='utf-8') as f:
        f.write(SETUP_PY)

    with open(MANIFEST_IN_PATH, 'w', encoding='utf-8') as f:
        f.write(MANIFEST_IN)

    with open(MODULE_PATH, 'w', encoding='utf-8') as f:
        f.write(module_text)


if __name__ == '__main__':
    main()
