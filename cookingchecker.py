import requests, os
req = requests.Session()
cookiefilefolder = os.path.dirname(__file__)
cookiefile = (cookiefilefolder + "\cookies.txt")
cookie = open(cookiefile).read().splitlines()
validcount = 0
invalidcount = 0

if len(cookie) > 0:
    print(str(len(cookie)) + " Cookie(s) Found")
    print(" ")
    pathnameforvalid = os.path.join(os.path.dirname(__file__), "validcookies.txt")
    newfileforvalid = open(pathnameforvalid, "w")
    newfileforvalid.truncate(0)
    pathnameforinvalid = os.path.join(os.path.dirname(__file__), "invalidcookies.txt")
    newfileforinvalid = open(pathnameforinvalid, "w")
    newfileforinvalid.truncate(0)
    for line in cookie:
        check = req.get('https://api.roblox.com/currency/balance', cookies={'.ROBLOSECURITY': str(line)})
        if check.status_code == 200:
            newfileforvalid.write(str(line) + "\n")
            validcount += 1
        else:
            newfileforinvalid.write(str(line) + "\n")
            invalidcount += 1
    print("Valid Cookie(s): " + str(validcount) + "\nInvalid Cookie(s):" + str(invalidcount))
else:
    print("No cookies found.")
