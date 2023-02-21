import requests as re
from bs4 import BeautifulSoup
import json
import time

COOKIE = open("cookie").read()
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"\
    " Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61"


def get_ranklist():
    # return in list(tuple(handle, rating))
    # not up-to-date
    li = json.load(open("user.ratedList.json", encoding="utf8"))["result"]
    return list(map(lambda x: (x["handle"], x["rating"]), li))


def get_submissions(handle: str, count: int, count_unique: int):
    # Get the code of the first `count` submissions, and remove duplicate problems
    r = re.get(
        f"https://codeforces.com/api/user.status?handle={handle}&from=1&count={count}",
        headers={"User-Agent": USER_AGENT,
                 "Cookie": COOKIE,
                 "origin": "https://codeforces.com"})
    res = []
    probs = set()
    for i in json.loads(r.text)["result"]:
        id = i["id"]
        prob = json.dumps(i["problem"])
        if prob in probs:
            continue
        if "contestId" not in i["problem"] or type(i["problem"]["contestId"]) != int:
            continue
        typ = "contest"
        if i["problem"]["contestId"] >= 100000:
            typ = "gym"
        r = re.get(
            f"https://codeforces.com/{typ}/{i['problem']['contestId']}/submission/{id}",
            headers={"User-Agent": USER_AGENT,
                     "Cookie": COOKIE,
                     "origin": "https://codeforces.com"})
        if r.text.find(str(id))==-1:
            probs.add(prob)
            continue
        bs = BeautifulSoup(r.text, features="html.parser")
        code = bs.find("pre").text
        res.append(code)
        probs.add(prob)
        if len(probs) >= count_unique:
            break
        time.sleep(1)
    return res
