from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. Estás en el index de Polls")
