from django.shortcuts import render

def SimpleIndex(request):
    return render(request, 'app_IndexHtml/index.html')