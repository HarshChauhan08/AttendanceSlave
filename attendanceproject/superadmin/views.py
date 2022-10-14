from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from attendanceproject.settings import MEDIA_URL
from .models import *
from .data_base_admin import *
from .import urls
import pymongo
import csv
from django.contrib.auth.models import User


# Create your views here.
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['AttendanceProject']
collection = db['superadmin_createaccounts']
def AdminHome(request):
        return render(request, 'superadmin/index.html')

def MakeAccounts(CsvFile):
        db = client['AttendanceProject']
        collection = db['superadmin_createaccounts']
        data = []
        FileWithLocation = '../attendanceproject'+MEDIA_URL+str(CsvFile)
        with open(FileWithLocation) as f:
                reader = csv.reader(f)
                for i in reader:
                        dict1 = {'studentPrn':i[0],'studentName':i[1],'studentEmail':i[2],'studentNumber':i[3]}
                        data.append(dict1)
        collection.insert_many(data)

def SaveData(request):
        if request.method=="POST":
                coures = request.POST.get("coures")
                branch = request.POST.get("branch")
                year = request.POST.get("year")
                file_csv = request.FILES["file_csv"]
                data = FileUpload.objects.create(coures=coures,branch=branch,year=year,file=file_csv)
                data.save()
                MakeAccounts(file_csv) 
        return render(request, 'superadmin/uploadfile.html')

def ShowAccounts(request):
        StudentDetails = CreateAccounts.objects.all()
        context = {'details':StudentDetails}
        # for item in StudentDetails:
        #         print(item.studentPrn,item.studentName, item.studentEmail, item.studentNumber)
        return render(request, 'superadmin/UpdateStudent.html', context)

def Login(request):
        return render(request, 'superadmin/login.html')

def SignUp(request):
         if request.method == 'POST':
                adminName = request.POST['admin_name']
                adminEmail = request.POST['admin_email']
                adminPassword = request.POST['admin_password']

                #Validation

                #creat user
                admin_account = User.objects.create_user(adminName,adminEmail,adminPassword)
                admin_account.save()
        # else:
        #         return HttpResponse("Not Allowed")
         return render(request, 'superadmin/signup.html')

def ForgotPassword(request):
        return render(request, 'superadmin/forgot.html')
