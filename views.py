import django
# this is my website which is building using django
from django.http import HttpResponse
from django.shortcuts import render

def Home(request):
    return render(request,'index.html')



def about(request):
    return render(request,'about.html')



def contact(request):
    return render(request,'contact.html')



# def about(request):
#     return render (request,'index.html')

# def index(request):
#     return HttpResponse("index")

def analyze(request):
    # get the text
    # use GET instead of POST if you have small data
    djtext=request.POST.get('text','default')

# check checkbox value
    removepunc=(request.POST.get('removepunc','off'))

    fapscap = request.POST.get('fapscap','off')

    newlineremover = request.POST.get('newlineremover','off')

    extraspaceremover = request.POST.get('extraspaceremover','off')
    print(djtext)
    # print(removepunc)
    if removepunc=="on":
        Punctuations='''!@#$%^&*()-=_+[]{}|;:'",.<>?/`'''
        analyzed=""
        for char in djtext:
            if char not in Punctuations:
                analyzed=analyzed+char
        # return HttpResponse("remove punc")
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)



    if(fapscap=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Changed to Uppercase','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)
    

    if(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if (char!='\n'):
                analyzed=analyzed+char
        params={'purpose':'New line Removed','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params)
    

    if(extraspaceremover=="on"):
        analyzed=""
        for index , char in enumerate(djtext):
          if not(djtext[index]==" " and djtext[index + 1]==" "):
           
              analyzed=analyzed+char

        params={'purpose':'Extra Space Removed','analyzed_text':analyzed}
        djtext=analyzed

    return render(request,'analyze.html',params)


    # else :
    #     return HttpResponse("Sorry you are offline")

# def capfirst(request):
#     return HttpResponse("capfirst")

# def newlineremover(request):
#     return HttpResponse("captilize first")

# def charcount(request):
#     return HttpResponse("charcount")

# def spaceremove(request):
#     return HttpResponse("spaceremove")
