from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'newsApp/index.html')

def sportsinfo(request):
    head_msg="SPORTS NEWS!!!!"
    msg1="vk loves AS"
    msg2="RS hits centyuwfbjdskd"
    msg3="wkfhsdvjdsjvndslvnlslds"
    mydict={"head_msg":head_msg,"msg1":msg1,"msg2":msg2,"msg3":msg3}
    return render(request,'newsApp/newspage.html',context=mydict)


def moviesinfo(request):
    head_msg="MOVIES NEWS!!!!"
    msg1="vk loves AS"
    msg2="RS hits centyuwfbjdskd"
    msg3="wkfhsdvjdsjvndslvnlslds"
    mydict={"head_msg":head_msg,"msg1":msg1,"msg2":msg2,"msg3":msg3}
    return render(request,'newsApp/newspage.html',context=mydict)

def generalinfo(request):
    head_msg="GENERAL NEWS!!!!"
    msg1="vk loves AS"
    msg2="RS hits centyuwfbjdskd"
    msg3="wkfhsdvjdsjvndslvnlslds"
    mydict={"head_msg":head_msg,"msg1":msg1,"msg2":msg2,"msg3":msg3}
    return render(request,'newsApp/newspage.html',context=mydict)
