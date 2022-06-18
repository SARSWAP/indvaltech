from django.conf import settings
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
from django.db.models import Q
from django.views import View
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.
def login_user(request):
    if request.method=="POST":
        username = request.POST['user']
        password = request.POST['password']
        user = authenticate(username = username,password=password)
        if user is not None:
            login(request,user)
            email = User.objects.get(username = username).email
            des = HRD_table.objects.get(Company_email = email).Designation
            name=HRD_table.objects.get(Company_email = email).Name
            if(des == "CEO" or des == "HR"):
                return render(request,'HR Dashboard.html')
            elif('manager' in des or 'Manager' in des):
                return render(request,'index.html', {'name':name})
            else:
                return render(request,'Design Dashboard.html')
        else:
            messages.error(request,"Invalid Credentials")
    return render(request,'login.html')

def family(request,name):
    if request.method == "POST":
        query = HRD_table.objects.filter(Q(Name=name))
        r = query[0]
        fname = request.POST['fmember_name']
        age = request.POST['age']
        relation = request.POST['relatives']
        occupation = request.POST['occupation']
        contact = request.POST['contact']
        remarks = request.POST['remarks']
        if len(contact) == 10:
                form1 = Family(EID=r, name=fname, age=age, relation=relation,
                occupation=occupation, contact=contact, remarks=remarks)
                form1.save()
                messages.success(request, ("Details updated"))
                return render(request, 'indval work-bankDetails.html', {'name': name})
        else:
                messages.error(request, 'Invalid Phone Number')
    return render(request, 'Family.html',{'name':name})

def register(request, name):
        if request.method == 'POST':
            query=HRD_table.objects.filter(Q(Name=name))
            r=query[0]
            aadhar=request.POST['aadhar']
            Gender=request.POST['gender']
            Email=request.POST['email']
            aadharDoc=request.FILES['aDoc']
            Pan=request.POST['Pan']
            panDoc=request.FILES['panDoc']
            passport=request.POST['passport']
            passportDoc=request.FILES['passportDoc']
            esicNum=request.POST['esicNum']
            esicDoc=request.FILES['esicDoc']
            Address=request.POST['sala']
            PermanentAddress=request.POST['paddress']
            Ph=request.POST['ph']
            DOB=request.POST['dob']
            Blood=request.POST['blood']
            EmergencyPh=request.POST['eph']
            Photo=request.FILES['img']
      
         #VALIDATION

            if len(Ph) == 10 and len(EmergencyPh)==10  and len(aadhar)==10 and len(esicNum)==11:
              employeeRegistrationForm = Employee(esicNum=esicNum,esicDoc=esicDoc,passportDoc=passportDoc,passport=passport,panDoc=panDoc,Pan=Pan,aadhar=aadhar,aadharDoc=aadharDoc,Name=r,Address=Address,PermanentAddress=PermanentAddress,Ph=Ph,Gender=Gender,DOB=DOB,Email=Email,Blood=Blood,EmergencyPh=EmergencyPh,Photo=Photo)
              employeeRegistrationForm.save()
              return render(request, 'Education.html', {'name': name})
            else:
              messages.error(request, 'Invalid Phone Number of emergency phone number')
              return render(request,'employee.html',{'name':name})    

        return render(request,'employee.html',{'name':name})  

def hr(request):
    return render(request,'src/html/HR Dashboard.html')

def documents(request,name):
    if request.method == "POST":
        #name = request.POST['name']
        query = HRD_table.objects.filter(Q(Name=name))
        r = query[0]
        application = request.FILES['application']
        pan = request.FILES['pan']
        adhaar = request.FILES['adhaar']
        passport = request.FILES['passport']
        noc = request.FILES['noc']
        payslip = request.FILES['payslip']
        esic = request.FILES['esic']
        experience = request.FILES['experience']
        it = request.FILES['it']
        
        documentform = Document(EID=r, application=application, pan=pan, aadhar=adhaar, passport=passport, noc=noc, payslip=payslip, esic=esic, experience=experience, it_form=it)
        documentform.save()
        return render(request,'src/html/indval work- EmpHist.html', {'name':name})
    return render(request, 'src/html/Documentation.html',{'name': name})


def bank(request, name):
    if request.method == "POST":
        query = HRD_table.objects.filter(Q(Name=name))
        r=query[0]
        acNo = request.POST['acNo']
        ifsc = request.POST['ifsc']
        scode = request.POST['sCode']
        iban = request.POST['iban']
        bankname = request.POST['bankname']
        branchname = request.POST['branchname']
        
        if len(ifsc)==11:
            bankform = Bank(EID=r, name=name, account=acNo, ifsc=ifsc,
            swift=scode, iban=iban, bank_name=bankname, branch=branchname)
            bankform.save()
            messages.success(request, ("Details updated"))
            return render(request, 'indval work- EmpHist.html', {'name': name})
        else:
            messages.error(request, 'Invalid IFSC Code')
    return render(request, 'bank.html', {'name': name})


def dashboard(request):
    return render(request,'src/html/index.html')


class AddProject(View):
    def get(self, request, *args, **kwargs):
        all_emp = HRD_table.objects.all()
        return render(request, 'AddProject.html', {'all_emp' : all_emp})

    def post(self, request, *args, **kwargs):
        pid = request.POST['pid']
        eid = request.POST['employees']
        query = HRD_table.objects.filter(Q(EID=eid))
        r = query[0]
        pname = request.POST['pname']
        department = request.POST['subject']
        sdate = request.POST['sop']
        edate = request.POST['eop']
        location = request.POST['subject2']
        pdesc = request.POST['remarks']

        projectform = Project(PID=pid, EID=r, Pname=pname, Department=department, 
        StartDate=sdate, EndDate=edate, location=location, ProjectDesc=pdesc )
        projectform.save()
        messages.success(request, ("Details updated"))
        return render(request, 'AddProject.html')
    
def AttendForm(request):
    return render(request,'src/html/AttendanceForm.html')

def DesignDashboard(request):
    return render(request,'src/html/Design Dashboard.html')

class AddActivity(View):
    def get(self, request, *args, **kwargs):
        all_project = Project.objects.all()
        return render(request, 'AddActivity.html', {'all_project': all_project})

    def post(self, request, *args, **kwargs):
        pname = request.POST['subject']
        query2 = Project.objects.filter(Q(Pname=pname))
        r = query2[0]
        task = request.POST['subject2']
        allocatedtime = request.POST['allocatedtime']
        actualtime = request.POST['actualtime']
        date = request.POST['date']

        addactivityform = Team(PID=r, TaskName=task, Allocated=allocatedtime, ActualTime=actualtime, dates=date)
        addactivityform.save()
        return render(request, 'AddActivity.html')


def history(request, name):
    if request.method == "POST":
        #name = request.POST['name']
        query = HRD_table.objects.filter(Q(Name=name))
        r=query[0]
        org = request.POST['org']
        work = request.POST['nature']
        designation = request.POST['designation']
        tools = request.POST['software']
        last_salary = request.POST['lsalary']
        reason_of_leaving = request.POST['reason']

        employeeHistoryForm = History(EID=r, organization=org, last_salary=last_salary, tools=tools,
        designation=designation, work=work, reason_of_leaving=reason_of_leaving)
        employeeHistoryForm.save()
        return render(request, 'src/html/index.html', {'name':name})
    return render(request, 'src/html/indval work- EmpHist.html')


def timesheet(request):
    return render(request, 'src/html/Timesheets.html')

def leave(request):
    return render(request,'src/html/Applyleave.html')

def payslip(request):
    return render(request,'src/html/payslip.html')

def hrd(request):
    return render(request,'src/html/HRD.html')

class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'src/html/pass_reset.html'

def education(request, name):
    if request.method == "POST":
        query = request.POST['name']
        r = query[0]
        q = request.POST['qual']
        b = request.POST['board']
        p = request.POST['percentage']
        y = request.POST['yop']
        
        educationform = Education(EID=r, qualification=q, board=b, percentage=p, passing=y)
        educationform.save()
        return render(request, 'src/html/bank.html', {'name':name})
    
    return render(request,'src/html/Education.html', {'name':name})


def search(request):
    return render(request,'search.html')
