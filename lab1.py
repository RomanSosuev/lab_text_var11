import re

with open("text.txt", "r") as f:
    text = f.read()
    splittext = re.split("\?|!|\.|\n", text)
    for i in range (len(splittext)):
        t=splittext[i]
        t = t.strip()
        if len(t) == 1 and t[0] != ",":
            print(t)
        elif t != "":
            if (t[1] == " " or t[1] == "." or t[1] == "!" or t[1] == "?") and t[0] != ",":
                print(t)
