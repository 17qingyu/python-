import re

import pyperclip

text = pyperclip.paste()
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?
(\s|-|\.)?
(\d{3})
(\s|-|\.)
(\d{4})
(\s*(ext|x|ext.)\s*(\d{2,5}))?
)''', re.VERBOSE)

emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9._-]+
(\.[a-zA-Z]{2,4})
)''', re.VERBOSE)
contacts = []

for groups in phoneRegex.findall(text):
    phoneNum = ''
    if groups[1] != '':
        phoneNum = groups[1]+'-'
    phoneNum += '-'.join([groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    contacts.append(phoneNum)
for groups in emailRegex.findall(text):
    contacts.append(groups[0])
if len(contacts):
    print("Copied to clipboard:")
    print("\n".join(contacts))
    pyperclip.copy("\n".join(contacts))
else:
    print('No phone numbers or email addresses found.')
