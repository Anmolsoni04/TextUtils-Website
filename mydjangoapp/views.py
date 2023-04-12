from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request, 'index.html')

def analyze(request):
    #Get the text
    samplText = request.POST.get('text', 'default')
    #Check check box values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    #Check which check box is on
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')

    if removepunc == "on":
        #analyzed = samplText
        puncs = '''!()-[]{};:'""\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in samplText:
            if char not in puncs:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        samplText = analyzed

    if(fullcaps == "on"):
        analyzed = ""
        for char in samplText:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        samplText = analyzed



    if(newlineremover == "on"):
        analyzed = ""
        for char in samplText:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre", analyzed)
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        samplText = analyzed


    if(spaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(samplText):
            if samplText[index] == " " and samplText[index+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
    if (removepunc != "on" and fullcaps != "on" and spaceremover != "on" and newlineremover != "on"):
        return HttpResponse("Error")

    return render(request, 'analyze.html', params)







