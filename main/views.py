from django.http import *
from django.core.exceptions import *
from .models import Photo, PhotoStatistic

import json
import os, os.path


class InvalidJsonError(Exception):
    pass


class DuplicatedPhotoNameError(Exception):
    pass


class StoreImgError(Exception):
    pass


def hello(request):
    return HttpResponse("Hello world!")


def upload(request):
    if request.method != "POST":
        return HttpResponse("Use POST please!")

    try:
        json_dict = _check_json(request.body.decode())
        _handle_upload(json_dict)
    except InvalidJsonError as e:
        return HttpResponse(str(e))
    except DuplicatedPhotoNameError as e:
        return HttpResponse(str(e))
    else:
        return HttpResponse("upload success!")


def upload_photo(request, filename):
    if request.method != "POST":
        return HttpResponse("Use POST please!")

    try:
        _handle_upload_photo(filename, request.body)
    except DuplicatedPhotoNameError as e:
        return HttpResponse(str(e))
    else:
        return HttpResponse("upload photo success!")


def upload_sta(request):
    if request.method != "POST":
        return HttpResponse("Use POST please!")

    try:
        statistic = request.body.decode()
        photo_sta = PhotoStatistic(statistic=statistic)
        photo_sta.save()
    except:
        return HttpResponse("Unknown Error happens, pls contact Zhouben")
    else:
        return HttpResponse("upload statistic success!")


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


def get_sta(request):
    if request.method == "GET":
        ret = PhotoStatistic.objects.all()
        ret = sorted(ret, key=lambda x: x.pub_time, reverse=True)
        return HttpResponse(json.dumps(ret, default=PhotoStatistic.serialize), content_type="application/json")
    else:
        return HttpResponse("Use GET please!")


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


def delete_sta(request):
    ret = PhotoStatistic.objects.all()
    n = ret.count()
    ret.delete()
    return HttpResponse("All %r data have been deleted." % n)


def _check_json(json_str):
    ret = json.loads(json_str)
    if all(ret.get(key, None) for key in ['name', 'score', 'filename']):
        return ret
    else:
        raise InvalidJsonError("Invalid data.All 'name', 'score', 'filename' are required in json")


def _handle_upload(json_dict):
    for f_name in os.listdir('photo'):
        if f_name == json_dict['filename']:
            raise DuplicatedPhotoNameError("Photo named %s already exist!" % f_name)

    photo = Photo(name=json_dict['name'], score=json_dict['score'], file_name=json_dict['filename'])
    photo.save()


def _handle_upload_photo(name, photo):
    # cnt = 1
    # name = json_dict['filename']
    # names = os.listdir("photo")
    # for i in range(len(names)):
    #     if name == names[i]:
    #         cnt += 1
    #         name = '.'.join(name.split('.')[:-1]) + '-%d.' % cnt + name.split('.')[-1]

    for f_name in os.listdir('photo'):
        if f_name == name:
            raise DuplicatedPhotoNameError("Photo named %s already exist!" % f_name)

    try:
        img = open(os.path.join("photo", name), 'wb')
        img.write(photo)
        img.close()
    except:
        raise StoreImgError("Can not store %r" % photo)
