import re


def is_strong(password):
    regexs = [
        re.compile(r"[a-z0-9]*[a-z][a-zA-Z0-9]*"),
        re.compile(r"[a-z0-9]*[A-Z][a-zA-Z0-9]*"),
        re.compile(r"[A-Z0-9]*[0-9][a-zA-Z0-9]*")
    ]
    if len(password) < 8:
        return False
    for regex in regexs:
        if regex.search(password) is None:
            return False
    return True


while True:
    password = input()
    if is_strong(password):
        print("密码设置成功")
        break
    else:
        print("密码强度不足，请重新输入")
        print("密码必须满足长度不少于 8 个字符，同时包含大写和小写字符，至少有一位数字。")
