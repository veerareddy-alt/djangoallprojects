from django.shortcuts import render

# Create your views here.
def home1(request):
    return render (request,'newsApp/home1.html')

def movieinfo(request):
    head_msg="latest movie information"
    msg1="Salman marriage"
    msg2="anushaka in love with virat"
    msg3="kareena quit movies"
    mydict={"head_msg":head_msg,"msg1":msg1,"msg2":msg2,"msg3":msg3}
    return render (request,'newsApp/news.html',context=mydict)

def sportsinfo(request):
    head_msg="latest sports information"
    msg1="rohit marriage"
    msg2="  virat in love with anushaka"
    msg3="india won the match"
    mydict={"head_msg":head_msg,"msg1":msg1,"msg2":msg2,"msg3":msg3}
    return render (request,'newsApp/news.html',context=mydict)

def generalinfo(request):
    head_msg="latest general information"
    msg1="Karanata CM second marriage"
    msg2="anushaka shetty loves MP Teja"
    msg3="whether is very cool in bangalore"
    mydict={"head_msg":head_msg,"msg1":msg1,"msg2":msg2,"msg3":msg3}
    return render (request,'newsApp/news.html',context=mydict)
