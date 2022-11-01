from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponse
from django import forms
from attendanceproject.settings import MEDIA_URL
from .models import *
from .data_base_admin import *
from .import urls
import pymongo
import csv
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.messages import constants as messages
from django.utils.decorators import method_decorator
import superadmin.authenticate_user as au


# Create your views here.
# User Name

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['AttendanceProject']
collection = db['superadmin_createaccounts']


@au.entry_check
def AdminHome(request):
        value = request.session.get('user')
        permission = au.check_if_allowed(value)
        if permission == True:
                return render(request, 'superadmin/index.html')
        else:
                return redirect('Login')
        

def Login(request):
        if request.method=="POST":
                admin_name = request.POST.get("adminName")
                admin_password = request.POST.get("adminPassword")
                user_auth = au.auth_user(admin_name, admin_password)
                if user_auth == True:
                        request.session['user'] = admin_name
                        print(request.session.get('user'))
                        return redirect('AdminHome')
                else:
                        return redirect('SignUp')
        return render(request, 'superadmin/login.html')


        
@au.entry_check
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

@au.entry_check
def SaveData(request):
        value = request.session.get('user')
        permission = au.check_if_allowed(value)
        if permission == True:
                redirect('UploadFiles')
                if request.method=="POST":
                        coures = request.POST.get("coures")
                        branch = request.POST.get("branch")
                        year = request.POST.get("year")
                        file_csv = request.FILES["file_csv"]
                        data = FileUpload.objects.create(coures=coures,branch=branch,year=year,file=file_csv)
                        data.save()
                        MakeAccounts(file_csv) 
                return render(request, 'superadmin/uploadfile.html')
        else:
             return redirect('Login')   

@au.entry_check
def ShowAccounts(request):
        value = request.session.get('user')
        permission = au.check_if_allowed(value)
        if permission == True:
                StudentDetails = CreateAccounts.objects.all()
                context = {'details':StudentDetails}
        # for item in StudentDetails:
        #         print(item.studentPrn,item.studentName, item.studentEmail, item.studentNumber)
                return render(request, 'superadmin/UpdateStudent.html', context)
        else:
                return redirect('Login')



def SignUp(request):
         return render(request, 'superadmin/signup.html')


def ForgotPassword(request):
        return render(request, 'superadmin/forgot.html')


