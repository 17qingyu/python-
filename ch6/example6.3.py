import pyperclip

text = pyperclip.paste()
lines = text.split("\n")
for index in range(0, len(lines)):
    lines[index] = '* ' + lines[index]
text = "\n".join(lines)
pyperclip.copy(text)
