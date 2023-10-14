import json
import os


def extract_user_ids_from_json(json_file_path):
    unique_user_ids = set()  # 重複を避けるために集合を使用
    thread_number = None

    with open(json_file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        if 'thread' in data[0]:  # 0番目の要素からthread番号を取得
            thread_number = data[0]['thread'].get('thread', None)

        for entry in data:
            if 'chat' in entry:
                user_id = entry['chat'].get('user_id', None)
                if user_id:
                    unique_user_ids.add(user_id)

    return unique_user_ids, thread_number


if __name__ == "__main__":
    directory_path = './JSONs/vocaloidcomments/'  # JSONファイルが保存されているディレクトリ
    result_list = []

    for json_file in os.listdir(directory_path):
        if json_file.endswith('.json'):
            full_path = os.path.join(directory_path, json_file)
            user_ids, thread_number = extract_user_ids_from_json(full_path)

            if thread_number:
                result_list.append({
                    "threadId": thread_number,
                    "user_ids": list(user_ids)
                })

    with open('vocaloid_combined_data.json', 'w', encoding='utf-8') as f:
        json.dump(result_list, f, indent=4, ensure_ascii=False)
