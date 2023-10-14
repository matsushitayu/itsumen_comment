import requests
import time

sm_numbers = []
# _offsetの値を0から1000まで100ずつ動かしながらGETリクエストを送る
for _offset in range(0, 1000, 100):
    url = f"https://api.search.nicovideo.jp/api/v2/snapshot/video/contents/search?q=vocaloid&targets=tags&fields=contentId,title,commentCounter&filters[viewCounter][gte]=1000&_sort=-commentCounter&_offset={_offset}&_context=apiguide&_limit=100"

    res = requests.get(url).json()
    # resからsm_numberを取り出してsm_numbersに追加
    sm_numbers.extend([item["contentId"] for item in res["data"]])
    # 5秒待つ
    time.sleep(5)

print(sm_numbers)

with open('vocaloid_sm_numbers.txt', 'w') as f:
    for sm_number in sm_numbers:
        f.write(f"{sm_number}\n")
