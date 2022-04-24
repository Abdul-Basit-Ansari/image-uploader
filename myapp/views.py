from django.shortcuts import render

# Create your views here.
from .form import ImageForm
from .models import Image
# Create your views here.

def home(request):
  if request.method == "POST":
      form = ImageForm(request.POST, request.FILES)
      if form.is_valid():
        form.save()
  form = ImageForm()
  img = Image.objects.all()
  return render(request, 'home.html', {'img':img, 'form':form})