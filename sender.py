from urllib.request import *
import json


def upload(**kwargs):
    # json data
    data = json.dumps(kwargs)
    data = data.encode()
    # img data
    img = open(kwargs['filename'], 'br')

    # post
    url = "http://127.0.0.1:8000/upload"
    header_dict = {"Content-type": "application/json"}
    req = Request(url=url, headers=header_dict, method="POST")
    f = urlopen(req, data=data, timeout=120)

    print(f.read())

    # post photo
    url = "http://127.0.0.1:8000/upload/photo/" + kwargs['filename']
    header_dict = {"Content-type": "image/jpg"}
    req = Request(url=url, headers=header_dict, method="POST")
    f = urlopen(req, data=img.read(), timeout=120)

    print(f.read())


def ask():
    url = "http://127.0.0.1:8000/ranking"
    req = Request(url=url, method="GET")
    f = urlopen(req, timeout=120)

    print(f.read())


if __name__ == '__main__':
    # upload(name="MaYun", score="20", filename="filename1.jpg")
    upload(name="ZhangJie", score="66", filename="demo1.jpg")
    # ask()
    # req = Request(url="http://127.0.0.1:8000/upload/statistic", method="POST")
    # f = urlopen(req, data=b"212123123", timeout=120)
    #
    # print(f.read())
