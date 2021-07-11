#! python3
import sys
import os
sys.path.append(os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]+r'\venv\lib\site-packages')
import pyperclip

PASSWORDS = {
    "qunar": "dsadasd",
    "csdn": "123156421231",
    "mooc": "dhasjdh2889@e@##@"
}

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()
account = sys.argv[1]
try:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
except KeyError:
    print('There is no account named ' + account)
