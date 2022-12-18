from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from .form import UploadFileForm,WordCountForm
# Create your views here.

def handle_uploaded_file(f):
    with open('./file.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
   
def handle_read_count_file(word):
    with open('./file.txt', 'r') as destination:
         return destination.readlines().count(word)
   
                     
           
            
def load_file(request):
   
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('count_word/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def count_word(request):
   
    if request.method == 'POST':
        form = WordCountForm(request.POST)
        print(form.data)
        print(form.errors)
        if form.is_valid():
            l =  handle_read_count_file(form.data['text'])
            return HttpResponse(l)
    else:
        form = WordCountForm()
    return render(request, 'count.html', {'f1': form})

