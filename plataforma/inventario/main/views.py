from django.conf import settings
from django.http import JsonResponse
from django.core.files import File
import os
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    res = {'code': 500, 'founded': False, 'response': {}}
    f = open(os.path.join(settings.STATIC_LOG, 'logs.txt'), "a")
    log_file = File(f)
    if request.method == "POST":
        vrf_token = request.POST.get('vrf_token')
        if vrf_token == "kkaiidfas":
            res = {'code': 200, 'response': "Hi"}
        else:
            error = "User no auth"
            res = {'code': 403, 'response': error}
            log_file.write('ERR: (logs) {}\n'.format(error))
    try:
        log_file.close()
        f.close()
    except Exception as e:
        print(res)
    
    return JsonResponse(res)