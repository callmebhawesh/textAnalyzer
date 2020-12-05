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
    audtonpr = request.GET.get("audtonpr", "off")


    if removepunc == 'on':
        punctuations = '''+-*/=_)(*&^%$£"![{]};:'@#~,<.>/?|'''
        analyzedText = ""

        for char in text:
            if char not in punctuations:
                analyzedText += char
        param = {'textWritten':"The Punctuations has been removed from your text", 'analyzedText' :analyzedText}
        return render(request, "analyze.html", param)

    elif makeCapital == 'on':
        analyzedText = ""

        for char in text:
            analyzedText += char.upper()
        param = {'textWritten':"You text has been successfully capitalized", 'analyzedText' :analyzedText}
        return render(request, "analyze.html", param)

    elif makeLower == 'on':
        analyzedText = ""
        
        for char in text:
            analyzedText += char.lower()
        param = {'textWritten':"You text has been successfully lower cased", 'analyzedText' :analyzedText}
        return render(request, "analyze.html", param)

    elif kbtogb == "on":
        text = int(text)
        analyzedText = text * 0.000001
       

        param = {'textWritten':"Kilobyte has been successfully converted into Gigabyte", 'analyzedText' :analyzedText}
        return render(request, "analyze.html", param)

    elif mbtogb == "on":
        text = int(text)
        analyzedText = text * 0.001
        

        param = {'textWritten':"Megabyte has been successfully converted into Gigabyte", 'analyzedText' :analyzedText}
        return render(request, "analyze.html", param)
        
    elif pbtogb == "on":
        text = int(text)
        analyzedText = text * 1000000
       
        param = {'textWritten':"Petabyte has been successfully converted into Gigabyte", 'analyzedText' :analyzedText}
        return render(request, "analyze.html", param)

    elif usdtonpr == "on":
        text = int(text)
        analyzedText = text * 119
       
        param = {'textWritten':"USD has been successfully converted into Nepali Rupees", 'analyzedText':analyzedText}
        return render(request, "analyze.html", param)

    elif audtonpr == "on":
        text = int(text)
        analyzedText = text * 87.63
  
        param = {'textWritten':"AUD has been successfully converted into Nepali Rupees", 'analyzedText':analyzedText}
        return render(request, "analyze.html", param)


    else:
        return HttpResponse("Error: Please check any box.")

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')