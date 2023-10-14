import requests
import json
import time

# threadIDが書かれたJSONを読み込む
with open('vocaloid_thread_sm.json', 'r') as f:
    data = json.load(f)

# threadIDをリストに格納
threadIds = []
for i in range(len(data)):
    threadIds.append(data[i]['threadId'])

# threadIDを重複を削除してリストに格納
threadIds = list(set(threadIds))

# treadIdでrequestを送信するループ
for threadId in threadIds:
    try:
        url = f"https://nvcomment.nicovideo.jp/legacy/api.json/thread?nicoru=3&res_from=-1000&scores=1&thread={threadId}&version=20090904&with_global=1"
        res = requests.get(url).json()
        print(str(res)[0:100])
        with open(f'./JSONs/vocaloidcomments/{threadId}.json', 'w', encoding="utf-8") as f:
            json.dump(res, f, indent=4, ensure_ascii=False)

    except Exception as e:
        print("threadId: " + str(threadId) +  " " + e)
        continue

    # 1000ms待つ
    time.sleep(1)