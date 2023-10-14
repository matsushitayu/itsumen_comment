import json
import glob

def merge_json_files(directory_path, output_filename):
    merged_data = []

    # 指定したディレクトリ内の全てのJSONファイルを読み込む
    for filename in glob.glob(f"{directory_path}\\*.json"):
        with open(filename, 'r') as f:
            data = json.load(f)
            merged_data.extend(data)

    # 結合したデータを新しいJSONファイルに保存する
    with open(output_filename, 'w') as f:
        json.dump(merged_data, f, indent=4)

if __name__ == '__main__':
    directory_path = './JSONs/vocaloid'  # JSONファイルが保存されているディレクトリ
    output_filename = 'vocaloid_thread_sm.json'  # 結合後のJSONファイル名
    merge_json_files(directory_path, output_filename)
