from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def counter(request):
    text = request.POST['text']
    amount_of_words =len(text.split())
    return render(request,'counter.html',{'amount_of_words':amount_of_words})