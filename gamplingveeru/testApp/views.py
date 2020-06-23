from django.shortcuts import render

# Create your views here.
def gamblinghome(request):
    return render(request,'testApp/gamblinghome.html')

def gamblinggames(request):
    return render(request,'testApp/gamblinggames.html')
