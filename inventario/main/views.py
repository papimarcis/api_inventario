from django.conf import settings
from django.http import JsonResponse
from django.core.files import File
import os
from django.shortcuts import render

def home(request):
    res = {'code': 500, 'founded': False, 'response': {}}
    f = open(os.path.join(settings.STATIC_LOG, 'deleteUser.txt'), "a")
    log_file = File(f)
    try:
        if request.method == "POST":
            res = {'code': 200, 'founded': True, 'response': "Hi"}
    except Exception as e:
        log_file.write('ERR: (deleteUser) {}\n'.format(str(e)))
    try:
        log_file.close()
        f.close()
    except Exception as e:
        print(res)
    
    return JsonResponse(res)