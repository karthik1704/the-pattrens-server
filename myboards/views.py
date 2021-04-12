from django.shortcuts import render


def myboards(request):

    return render(request, 'myboards/myboards.html', {})