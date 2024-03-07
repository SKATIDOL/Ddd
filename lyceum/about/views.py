from django.http import HttpResponse

def   description(request):
    return HttpResponse("<h1>О проекте</h1>")