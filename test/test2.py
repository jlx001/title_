import urllib.request as ur
import io
import PIL.Image as pil
import requests

def download(url):
    # j = prom[2]

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}

    # params 接收一个字典或者字符串的查询参数，字典类型自动转换为url编码，不需要urlencode()
    response = requests.get(url, headers=headers)

    # HEADERS = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'}
    # header = ur.Request(url, headers=HEADERS)
    # header = ur.Request(url)
    err = 0
    data = response.content
    # data = ur.urlopen(header).read()

    # while (err < 3):
    #     try:
    #         data = ur.urlopen(header).read()
    #     except Exception:
    #         err += 1
    #     else:
    #         return data
    # return False
    # raise Exception("Bad network link.")
    picio = io.BytesIO(data)
    small_pic = pil.open(picio)
    small_pic.save('output.png', quality=100)
    print(1)
# http://mts0.googleapis.com/vt?lyrs=s&x=111&y=111&z=7

if __name__ == '__main__':
    url = "https://gac-geo.googlecnapps.cn/maps/vt?lyrs=s&x=111&y=111&z=7"
    data = download(url)
    print(data)
    with open("baidu.html", "wb") as f:
        f.write(data)
    print("Done.")

