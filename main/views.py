from django.http import *
from django.core.exceptions import *
from .models import Photo

import json
import os, os.path


def hello(request):
    return HttpResponse("Hello world!")


def upload(request):
    if request.method == "POST":
        json_dict = _check_json(request.body.decode())
        if json_dict:
            _handle_upload(json_dict)
            return HttpResponse("upload success!")
        else:
            return HttpResponse("Invalid data.All 'name', 'score', 'filename', 'photo' are required in json")
    return HttpResponse("Use POST please!")


def get_ranking(request):
    if request.method == "GET":
        ret = Photo.objects.all()
        ret = sorted(ret, key=lambda x: x.score, reverse=True)
        return HttpResponse(json.dumps(ret, default=Photo.serialize), content_type="application/json")
    else:
        return HttpResponse("Use GET please!")


def get_photo(request, filename):
    try:
        img = open(os.path.join("photo", filename), "rb")
    except FileNotFoundError:
        return HttpResponse("Photo not found.")
    else:
        return HttpResponse(img.read(), content_type="image/jpg")


def delete_all(request):
    ret = Photo.objects.all()
    n = ret.count()
    for file in os.listdir("photo"):
        target_f = os.path.join("photo", file)
        if os.path.isfile(target_f):
            os.remove(target_f)
    ret.delete()
    return HttpResponse("All %r photos have been deleted." % n)


def delete(request, target_id):
    try:
        ret = Photo.objects.get(id=target_id)
    except MultipleObjectsReturned:
        return HttpResponse("Error!!There are multiple photo with the id!Please contact Zhou Ben")
    except ObjectDoesNotExist:
        return HttpResponse("There are no photo with id %r" % target_id)
    else:
        os.remove(os.path.join("photo", ret.file_name))
        ret.delete()
        return HttpResponse("photos with id %r have been deleted." % target_id)


def _check_json(json_str):
    ret = json.loads(json_str)
    if all(ret.get(key, None) for key in ['name', 'score', 'filename', 'photo']):
        return ret
    else:
        return {}


def _handle_upload(json_dict):
    cnt = 1
    name = json_dict['filename']
    names = os.listdir("photo")
    for i in range(len(names)):
        if name == names[i]:
            cnt += 1
            name = '.'.join(name.split('.')[:-1]) + '-%d.' % cnt + name.split('.')[-1]

    photo = Photo(name=json_dict['name'], score=int(json_dict['score']), file_name=name)
    photo.save()

    img = open(os.path.join("photo", name), 'wb')
    print(json_dict['photo'])
    img.write(json_dict['photo'])
    img.close()
