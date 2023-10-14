import json
from collections import Counter

# combined_data.json ファイルを読み込む
with open('combined_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# vocaloid_combined_data.json ファイルを読み込む
with open('vocaloid_combined_data.json', 'r', encoding='utf-8') as f:
    vocaloid_data = json.load(f)

# thread_sm.json ファイルを読み込む
with open('vocaloid_thread_sm.json', 'r', encoding='utf-8') as f:
    thread_movie_data = json.load(f)

# threadId と movieId の対応関係を辞書に格納
thread_movie_dict = {str(entry['threadId']): entry['movieId'] for entry in thread_movie_data}


# 指定された threadId の user_ids を取得
specified_thread_user_ids = None
for entry in data:
    if entry['threadId'] == '1593098944':
        specified_thread_user_ids = set(entry['user_ids'])
        break

if specified_thread_user_ids is None:
    print("指定された threadId が見つかりませんでした")
    exit()

# 他のすべての threadId での重複をカウント
overlap_count = Counter()

for entry in vocaloid_data:
    if entry['threadId'] == '1593098944':
        continue
    overlap = len(specified_thread_user_ids.intersection(set(entry['user_ids'])))
    overlap_count[entry['threadId']] = overlap

# 重複が多い順に 10 個の threadId を取得
most_common_10 = overlap_count.most_common(10)

print("重複が多い 10 個の threadId とその重複数:")
for thread_id, count in most_common_10:
    print(f"threadId: {thread_id}, 重複数: {count}, 対応する movieId: https://www.nicovideo.jp/watch/{thread_movie_dict.get(str(thread_id), '該当なし')}")
