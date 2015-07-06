from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import random
import subprocess

# @require_http_methods(['POST',])
@csrf_exempt
def battle(request, player1, player2):
    command = "docker build -t battlecontainer /home/ubuntu/"
    command2 = "docker run -it --rm battlecontainer python battlePy/demo.py"
    command = command.split()
    command2 = command2.split()
    command2.append(player1)
    command2.append(player2)
    subprocess.call(command)
    output = subprocess.check_output(command2)
    try:
        output = output.strip()
        output = output.split(' === ')
        result = {'games_played': output[0], output[1]: {'win':output[2]}, output[3]: {'win':output[4]}}
        return JsonResponse({'result':result})
    except:
        return

@csrf_exempt
def upload(request):
    f = request.POST.get('file')
    name = request.POST.get('name')
    if os.path.isfile('upload/'+name+'.py')==False:
        with open('upload/'+name+'.py', 'wb+') as destination:
            destination.write(f)
        return battle('','ImprovedRandomPlayer', name)
    else:
        return JsonResponse({'message': 'Name already taken, try appending numbers'})
    # return JsonResponse({'message':'uploaded successfully'})
