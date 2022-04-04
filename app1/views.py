from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse



#CODE FOR VIDEO 7
def index(request):

   return render(request, 'index.html')

def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    print(removepunc)
    print(djtext)

    # return HttpResponse(
    #     '''<h1>home</h> <a href="https://support.google.com/chrome/?p=help&ctx=settings">WELCOME TO GOOGLE</a>''')

    #analyzed = djtext
    # punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
    else:
        return HttpResponse("Error")

    params = {'purpose': 'Remove Punctuation', 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)



