from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    return render(request, 'BOT/index.html')


def board(request):

    context = {
        'player': request.POST['name'],
        'level': request.POST['level'],
        'color': request.POST['color'],
        'clock': True if 'clock' in request.POST else False
    }
    return render(request, 'BOT/board.html', context)


def bot(request):
    if request.is_ajax():
        # do something
        request_data = request.GET
        print(request_data)
        return JsonResponse({"coin": "wp4", "to": "d4"})
