from urllib.request import *
import json


def upload(**kwargs):
    # base64 img
    import base64

    f = open('demo.jpg', 'br')
    bs_f = base64.b64encode(f.read())

    # json data
    data = json.dumps(kwargs)
    data = data.encode()
    # data = data[:-1] + b', "photo": "' + bs_f + b'"}'

    # post
    url = "http://127.0.0.1:8000/upload"
    header_dict = {"Content-type": "application/json"}
    req = Request(url=url, headers=header_dict, method="POST")
    f = urlopen(req, data=data, timeout=120)

    print(f.read())


def ask():
    url = "http://127.0.0.1:8000/ranking"
    req = Request(url=url, method="GET")
    f = urlopen(req, timeout=120)

    print(f.read())


if __name__ == '__main__':
    # upload(name="MaYun", score="20", filename="filename1.jpg")
    # upload(name="ZhangJie", score="66", filename="filename2.jpg")
    # ask()
    req = Request(url="http://127.0.0.1:8000/upload/statistic", method="POST")
    f = urlopen(req, data=b"212123123", timeout=120)

    print(f.read())

