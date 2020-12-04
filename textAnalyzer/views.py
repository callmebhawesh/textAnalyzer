from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def analyze(request):
    text = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    makeCapital = request.GET.get('makeCapital', 'off')
    makeLower = request.GET.get('makeLower', 'off')
    kbtogb = request.GET.get('kbtogb', 'off')
    mbtogb = request.GET.get('mbtogb', 'off')
    pbtogb = request.GET.get("pbtogb", "off")
    usdtonpr = request.GET.get("usdtonpr", "off")

    if removepunc == 'on':
        punctuations = '''+-*/=_)(*&^%$£"![{]};:'@#~,<.>/?|'''
        analyzedText = ""
        textWritten = text

        for char in text:
            if char not in punctuations:
                analyzedText += char
        param = {'textWritten':textWritten, 'analyzedText' :analyzedText}
        return render(request, "analyze.html", param)

    elif makeCapital == 'on':
        analyzedText = ""
        textWritten = text
        for char in text:
            analyzedText += char.upper()
        param = {'textWritten':textWritten, 'analyzedText' :analyzedText}
        return render(request, "analyze.html", param)

    elif makeLower == 'on':
        analyzedText = ""
        textWritten = text
        for char in text:
            analyzedText += char.lower()
        param = {'textWritten':textWritten, 'analyzedText' :analyzedText}
        return render(request, "analyze.html", param)

    elif kbtogb == "on":
        text = int(text)
        analyzedText = text * 0.000001
        textWritten = text

        param = {'textWritten':textWritten, 'analyzedText' :analyzedText}
        return render(request, "analyze.html", param)

    elif mbtogb == "on":
        text = int(text)
        analyzedText = text * 0.001
        textWritten = text

        param = {'textWritten':textWritten, 'analyzedText' :analyzedText}
        return render(request, "analyze.html", param)
        
    elif pbtogb == "on":
        text = int(text)
        analyzedText = text * 1000000
        textWritten = text
        param = {'textWritten':textWritten, 'analyzedText' :analyzedText}
        return render(request, "analyze.html", param)

    elif usdtonpr == "on":
        text = int(text)
        analyzedText = text * 119
        textWritten = text
        param = {'textWritten':textWritten, 'analyzedText':analyzedText}
        return render(request, "analyze.html", param)


    else:
        return HttpResponse("Error: Please check any box.")
