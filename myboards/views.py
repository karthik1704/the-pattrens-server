from django.db.models import Q
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from myboards.models import MyBoard

@login_required
def myboards(request):
    myboard = MyBoard.objects.filter(user=request.user)
    context = {
        'myboard':myboard
    }
    return render(request, 'myboards/myboards.html', context)

@login_required
def myboard_detail(request, pk):
    myboard = MyBoard.objects.get(Q(user=request.user) | Q(pk=pk))
    print(myboard)
    context = {
        'myboard':myboard
    }
    return render(request, 'myboards/detail.html', context)