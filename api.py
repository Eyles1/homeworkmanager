import json
import datetime
import base64
import hashlib

gethomeworks = lambda : json.loads(open("./data/homework.json", "r").read())

def write_homeworks(subject:str, to_do: str, end_date:type(datetime.datetime.now()), done=False):
    homeworks = gethomeworks()
    todo = base64.b64encode(to_do.encode()).decode()
    homeworks.append({"subject":subject, "todo":todo, "enddate":end_date, "id":hashlib.sha256((subject+todo+"".join(end_date)).encode()).hexdigest(), "done":done})
    open("./data/homework.json", "w").write(json.dumps(homeworks))

def getwork():
    work = gethomeworks()
    work_form = ""
    for i in work:
        work_form += "{},{},{},{},{}\n".format(i["subject"], base64.b64decode(i["todo"].encode()).decode(), "-".join(i["enddate"]), i["id"], str(i["done"]).lower())
    work_form = work_form[:-1]
    return work_form

def setdone(id_hash, value):
    did = False
    work = gethomeworks()
    for i in range(0, len(work)):
        if work[i]["id"] == id_hash:
            work[i]["done"] = value
            did = True
    open("./data/homework.json", "w").write(json.dumps(work))
    return did
