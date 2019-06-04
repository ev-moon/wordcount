from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['rawtext']
    a = text.split()
    counts = {}
    for word in a:
        if word in counts:
            counts[word] +=1
        else:
            counts[word] = 1        
    counts = sorted(counts.items(), key=lambda k : k[1], reverse=True)
    return render(request, 'result.html', {'raw': text, 'length': len(a), 'counts': counts})