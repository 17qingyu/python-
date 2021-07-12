import re


def regexStrip(replacedStr, replaceStr=' '):
    stripRegex = re.compile(r'^({0})*|({0})*$'.format(replaceStr))
    return stripRegex.sub(r"", replacedStr)


replaceStr = input()
replacedStr = input()
print(regexStrip(replacedStr, replaceStr))