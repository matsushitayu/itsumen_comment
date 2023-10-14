import requests, random, string

movieId = 'sm35919998'
headers = {
  "X-Frontend-Id": "6",
  "X-Frontend-Version": "0"
}

def generate_track_id():
  # 10文字の英数字をランダムに生成
  first_part = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

  # アンダースコアを1文字
  second_part = '_'

  # 13桁の数字をランダムに生成
  third_part = str(random.randint(10**12, 10**13-1))

  # 3つを連結して返す
  return first_part + second_part + third_part



actionTrackId = generate_track_id()

url = "https://www.nicovideo.jp/api/watch/v3_guest/{}?actionTrackId={}&_frontendVersion=6".format(
  movieId, actionTrackId)

res = requests.post(url, headers=headers).json()
print(str(res))

# nvComment = res["data"]["comment"]["nvComment"]