from django.http import HttpResponse


def home_page_view(request):
    return HttpResponse('<h1>Hello, World!<h1><h2>I\'m working with Django!</h2>')
