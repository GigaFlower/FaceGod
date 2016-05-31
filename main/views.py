from django.http import *
from .models import Photo

import json
import base64
import os.path


def hello(request):
    return HttpResponse("Hello world!")


def upload(request):
    if request.method == "POST":
        # form = PhotoForm(request.POST, request.FILES)
        # if form.is_valid():
        json_dict = _check_json(request.body.decode())
        if json_dict:
            _handle_upload(json_dict)
            return HttpResponse("upload success!")
        else:
            return HttpResponse("Invalid data.")

    return HttpResponse("Use POST please!")


def get_ranking(request):
    ret = Photo.objects.all()
    ret = sorted(ret, key=lambda x: x.score, reverse=True)
    return HttpResponse(json.dumps(ret, default=Photo.serialize), content_type="application/json")


def get_photo(request, filename):
    img = open(os.path.join("photo", filename), "rb")
    if img:
        return HttpResponse(img.read(), content_type="image/png")
    else:
        return HttpResponse("Photo not found.")


def _check_json(json_str):
    ret = json.loads(json_str)
    if all(key in ret for key in ['name', 'score', 'filename', 'photo']):
        return ret
    else:
        return {}


def _handle_upload(json_dict):
    photo = Photo(name=json_dict['name'], score=int(json_dict['score']), file_name=json_dict['filename'])
    photo.save()

    img = open(os.path.join("photo", json_dict['filename']), 'wb')
    img.write(base64.b64decode(json_dict['photo']))
    img.close()
