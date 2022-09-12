from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from .models import FileUpload

# Create your views here.
def AdminHome(request):
        return render(request, 'superadmin/index.html')



# class CsvImportForm(forms.Form):
#     csv_upload = forms.FileField()

# def UploadFiles(request):
#     form = CsvImportForm()
#     data = {"form" : form}
#     return render(request, 'superadmin/uploadfile.html', data)

# def check(request):
#     # if request.method == "POST":
#     #     file2 = request.FILES['file']
#     #     document = documents.objects.create(file = file2)
#     #     document.save()
#     #     return HttpResponse("YOur File Was SAVEF")
#     return render(request, 'superadmin/uploadfile.html')

def SaveData(request):
        if request.method=="POST":
                coures = request.POST.get("coures")
                branch = request.POST.get("branch")
                year = request.POST.get("year")
                file_csv = request.FILES["file_csv"]
                data = FileUpload.objects.create(coures=coures,branch=branch,year=year,file=file_csv)
                data.save()
        return render(request, 'superadmin/uploadfile.html')


