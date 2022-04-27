from django.shortcuts import redirect, render

# Create your views here.
# from .form import ImageForm
from .models import Image

def home(request): 

    if request.method == "POST":
        photo = request.FILES['myimg']
        data = Image(image=photo)
        data.save()
        photo = None
          # form = ImageForm(request.POST, request.FILES)
          # if form.is_valid():
          #   form.save()
    # form = ImageForm()
    img = Image.objects.all().order_by('-date')
    dic = {'img':img}
    return render(request, 'home.html',dic )

def remove(request,sno):
  img = Image.objects.get(sno=sno)
  img.delete()
  return redirect(home)
