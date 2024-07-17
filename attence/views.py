from django.shortcuts import render
from .views import *
from .forms import *
from .models import *
from .views import *
import ast
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect,reverse
from pytz import timezone
from datetime import datetime
from django.core.management import call_command
from django.conf import settings
from django.db import connections,connection
import os


def ven(request):
    return render(request, 'backend/def.html')
    
def home(request):
       
    data={
    'ug':course_ug.objects.all(),
    'pg':course_pg.objects.all()
    }
    if request.method == 'POST':
        print(request.POST)
           
        if request.POST['department']=='PG':
            pgcource=course_pg()
            departmentname=request.POST['departmentname'].upper()
            pgcource.department=departmentname
            pgcource.year1=departmentname+"_1YEAR"
            pgcource.year2=departmentname+"_2YEAR"

            
            pgcource.save()
           
        else:
            ugcource=course_ug()
            departmentname=request.POST['departmentname'].upper()
            ugcource.department=departmentname
            ugcource.year1=departmentname+"_1YEAR"
            ugcource.year2=departmentname+"_2YEAR"
            ugcource.year3=departmentname+"_3YEAR"
            ugcource.save()

                 

    return render(request, 'backend/index.html',data)

def create_details(request,year):
    data={
        'year':year,
        'students':student_details.objects.filter(key=year)
        
    }
    
    if request.method == 'POST':
        
        course=student_details()
        
        course.name=request.POST['student_name'].upper()
        course.regnumber=request.POST['register_number'].upper()
        course.key=year
        
        course.save()
        return redirect(f"/student_details/{year}",data)
    
    
    
    return render(request, 'backend/stdd.html',data)
           
       
def delete_student(request,id):
    
    
    student_details.objects.filter(id=id).delete()
    print(id)
    return redirect(request.META.get('HTTP_REFERER', '/default/url/'))

def edit_student(request,id):
    student=student_details.objects.get(id=id)
    data={
       'student':student
       
    }
    if request.method == 'POST':
        
        student.name=request.POST['student_name'].upper()
        student.regnumber=request.POST['register_number'].upper()
        student.save()
        return redirect(f"/student_details/{student.key}",data)
    print(id)
    return render(request,"backend/editpage.html",data)
   
def mainpanal(request):
    takein=''
        
    date=entry_panal.objects.all()
    date1=date[::-1]
    print(date1)
    todaydate=datetime.now(timezone('Asia/Kolkata'))
    dt = datetime.now(timezone('Asia/Kolkata'))
    if date1 == []:
        day=0
        datecheck=''
    else:
        day=int(date1[0].day)
        datecheck=date1[0].date
    if request.method == 'POST':
        if datecheck==dt.strftime("%d/%m/%Y"):
            takein="attence allready taken"
            
             #return redirect('/attendance')
        else:
            entry=entry_panal()
            entry.day=request.POST['day']
            entry.date=request.POST['date']
            entry.dayorder=request.POST['dayorder']
            entry.save()
            return redirect('/mainpanal')
    
    data={
        'datas':entry_panal.objects.all(),
        'day':day+1,
        'date':dt.strftime("%d/%m/%Y"),
        'takein':takein
    }
    return render(request,'backend/mainpanal.html',data)

def login(request):
    passt=''  
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        
        if username=='admin' and password=='sou@123':
            return redirect('/home')
        elif username=='attendance' and password=='sou@123':
            return redirect('/attencemainpage') 
        elif username=='view' and password=='sou@123':
            return redirect('/viewall') 
        elif username=='principal' and password=='sou@123':
            return redirect('/mainpage') 
        else: 
            passt="Invalid credentials"
    data={
        'pass':passt
        }  
    return render(request,'backend/login.html',data)

def viewpage(request):
    data={
    'ug':course_ug.objects.all(),
    'pg':course_pg.objects.all(),
    }
    return render(request, 'backend/viewmainpage.html',data)

def reattence(request):
    date=entry_panal.objects.all()

    date1=date[::-1]
    print(date1[0].day)
    day=int(date1[0].day)+1
    print(day)
    data={
    'ug':course_ug.objects.all(),
    'pg':course_pg.objects.all(),
    
    'order':date1[0].dayorder,
    'day':day-1,
    'date':(date1[0].date),
    }


    return render(request, 'backend/attencetakemain.html',data)

def attences_take(request,year):
    finished=''
    date=entry_panal.objects.all()

    date1=date[::-1]
    day=int(date1[0].day)
    
    
    datechek='i.day'+ str(day)  
    datechek1='day'+ str(day) 
   # print(datechek1) 
    
    student=student_details.objects.filter(key=year)
    
    #student_details.objects.filter(regnumber=i.regnumber).update(**{datechek1: 'venkateshbabu1'})
    hors="Attendance Take 1st Hors"
    b=0 
    for i in student:
        a=0 
        #student_details.objects.filter(regnumber=i.regnumber).update(**{datechek1: ''})
        for ia in eval(datechek):
            #print(eval(datechek))
            
            print(ia,"the level",a)
            a+=1
        b=a
    print(b)
    if b ==5:
        hors="Attendance Take 2nd Hors"
    elif b==10:
        hors="Attendance Take 3rd Hors"
    elif b==15:
        hors="Attendance Take 4th Hors"
    elif b==20:
        hors="Attendance Take 5th Hors"
    elif b==25:
        hors="Attendance finished"
    
    if request.method == 'POST':
        for i in student:
            renum=request.POST[i.regnumber]
            print(renum)
            levalcheck=len(datechek)
            
            
            if  25 == a :
                finished=" Attendance Close"
                return redirect('/attencemainpage/')
            else:
                if renum == '1':
                    print('if')
                    icheck=eval(datechek)
                    print(icheck)
                    if icheck== '':
                        print('insideif')
                        listval=[]
                        listval.append(str(renum))
                        student_details.objects.filter(regnumber=i.regnumber).update(**{datechek1: str(listval)})
                    else:
                        
                        listval1=eval(icheck)
                        print(type(listval1))
                        listval1.append(renum)
                        student_details.objects.filter(regnumber=i.regnumber).update(**{datechek1: str(listval1)})  
                elif renum == '0':
                    print('else')
                    icheck=eval(datechek)
                    if icheck== '':
                        listval2=[]
                        listval2.append(str(renum))
                        student_details.objects.filter(regnumber=i.regnumber).update(**{datechek1: str(listval2)})
                    else:
                        
                        listval3=eval(icheck)
                        print(type(listval3))
                        listval3.append(renum)
                        student_details.objects.filter(regnumber=i.regnumber).update(**{datechek1: str(listval3)}) 
        
            print(eval(datechek))
        return redirect('/attencemainpage/')

       
    
        
        
    data={
        'key':year,
        'student':student_details.objects.filter(key=year).order_by('regnumber'),
        'hors':hors,
        'day':day,
        'date':(date1[0].date),
        'finshed':finished,
    }
    return render(request,'backend/attencetake.html',data)


def create_deleteug(request,id):
    course_ug.objects.filter(id=id).delete()

    return redirect('/home/')
def create_deletepg(request,id):
    course_pg.objects.filter(id=id).delete()

    return redirect('/home/')
def view(request,year):
    key=year
    data_list=[]
    pre=0
    st=student_details.objects.all()
    # for i in st:
    #     student_details.objects.filter(regnumber=i.regnumber).update(day4="['0', '1', '0', '1', '0']")
    date=entry_panal.objects.all()
    datety=date.values_list('date', flat=True)
    dayorder=date.values_list('dayorder', flat=True)
    print(datety)

    date1=date[::-1]
    
    day=int(date1[0].day)+1
    print(day)
    
    student=student_details.objects.filter(key=key)
    #student_details.objects.filter(name='ABI').update(day3="['1', '1', '1', '1', '1']")
    for i in student:
        a=[]
        x=0
        b=[]
        val=''
        #ditails=student.values_list(i, flat=True)
        for dateting in range(1,day):
            l=0
            con=str('i.day'+str(dateting))
            e=eval(con)
            if eval(con) != '':
                e=eval(con)
            else:
                a.append(['not','not','not','not','not'])
            
            if e != '':
                dlen=eval(e)   
            # print(dlen)
                if len(dlen)==5:
                    if dlen[0] == '1':
                        if dlen[1] == '1':
                            if dlen[2] =='1':
                                x+=0.5
                                l+=0.5
                    if dlen[3]=='1':
                        if dlen[4]=='1':
                                x+=0.5
                                l+=0.5
                            
                a.append(eval(e))
                b.append(l)
        #print(type(a))
        today=day-1
        print("the values",x/today) 
        pre=(x/today)*100
        print(pre)
        if pre >= 80:
            val='PASS'
        elif pre >= 60:
            val='lack'
        elif pre >= 50:
            val='RS'
        elif pre <= 50:
            val='RC'
        
        
        # print(datety)
        # print(a)
        # print(dayorder)
        # print(day)
        
        
        d = [[date, day, *inner_list,b] for date, day, inner_list,b in zip(datety, dayorder, a,b)]
        
        
        data={
            'daypresent':x,
            'presentage':round(pre,2),
            'greade':val,
            'regnumber':i.regnumber,
            'name':i.name,
            'dep':key,
            'combined_list' :d ,
            'date':datety,
            'dayorder':dayorder,       
            'days': a,
        }
        data_list.append(data)
    



    maindata={
        'data':data_list,
    }
  
    return render(request,'backend/view.html',maindata)

def caldas(key):
    key=key.upper()
    data_list=[]
    pre=0
    st=student_details.objects.all()
    # for i in st:
    #     student_details.objects.filter(regnumber=i.regnumber).update(day4="['0', '1', '0', '1', '0']")
    date=entry_panal.objects.all()
    datety=date.values_list('date', flat=True)
    dayorder=date.values_list('dayorder', flat=True)
    print(datety)

    date1=date[::-1]

    day=int(date1[0].day)+1
    print(day)

    student=student_details.objects.filter(regnumber=key)
    #student_details.objects.filter(name='ABI').update(day3="['1', '1', '1', '1', '1']")
    for i in student:
        a=[]
        x=0
        b=[]
        val=''
        #ditails=student.values_list(i, flat=True)
        for dateting in range(1,day):
            l=0
            con=str('i.day'+str(dateting))
            e=eval(con)
            if eval(con) != '':
                e=eval(con)
            else:
                a.append(['0','0','0','0','0'])

            if e != '':
                dlen=eval(e)
            # print(dlen)
                if len(dlen)==5:
                    if dlen[0] == '1':
                        if dlen[1] == '1':
                            if dlen[2] =='1':
                                x+=0.5
                                l+=0.5
                    if dlen[3]=='1':
                        if dlen[4]=='1':
                                x+=0.5
                                l+=0.5

                a.append(eval(e))
                b.append(l)
        #print(type(a))
        today=int(date1[0].day)




        pre=(x/today)*100




        print(pre)
        if pre >= 80:
            val='PASS'
        elif pre >= 60:
            val='lack'
        elif pre >= 50:
            val='RS'
        elif pre <= 50:
            val='RC'


        # print(datety)
        # print(a)
        # print(dayorder)
        # print(day)


        d = [[date, day, *inner_list,b] for date, day, inner_list,b in zip(datety, dayorder, a,b)]


        data={
            'daypresent':x,
            'presentage':round(pre,2),
            'greade':val,
            'regnumber':i.regnumber,
            'name':i.name,
            'dep':key,
            'combined_list' :d ,
            'date':datety,
            'dayorder':dayorder,
            'days': a,
        }
        data_list.append(data)

    return data_list


def student_view(request,key):
    
    data1=caldas(key)
    data={
        'data':data1,

    }
    
    return render(request,'backend/studentview.html',data)

def student_login(request):
    key=''
    if request.method == 'POST':
        key=request.POST['username']
        return redirect('/student_view/21uit001',key=key)
       
  
    return render(request,'backend/login_student.html',)

def searchviewpage(request):
    data1=[]
    if request.method == 'POST':
        key=request.POST['search']
        data1=caldas(key)
    data={
        'data':data1,
    }
    
    return render(request,'backend/searchviewpage.html',data)

def mainpage(request):
    ug=course_ug.objects.all()
    
    
    date=entry_panal.objects.all()
    date1=date[::-1]
    
    day=int(date1[0].day)
    datechek='i.day'+ str(day) 
    #print(day)
    ugdata=[]
    year11=[]
    department_list=[]
    
    for i in ug: 
        year=i.department
        year11.append(year)        
        for l in range(3):
            totalstudent=0
            year1=year+str(f'_{l+1}YEAR')
            student=student_details.objects.filter(key=year1)
        
        #student_details.objects.filter(regnumber=i.regnumber).update(**{datechek1: 'venkateshbabu1'})
            hors="NOT Attendance Take"
            b=0 
            for i in student:
                #print(i.name)
                totalstudent+=1
                a=0 
                #student_details.objects.filter(regnumber=i.regnumber).update(**{datechek1: ''})
                for ia in eval(datechek):
                    a+=1
                b=a
            print('theheeheh',b)
            if b ==5:
                hors="Attendance Take 1st Hors"
            elif b==10:
                hors="Attendance Take 2nd Hors"
            elif b==15:
                hors="Attendance Take 3rd Hors"
            elif b==20:
                hors="Attendance Take 4th Hors"
            elif b==25:
                hors="Attendance Take 5th Hors"
            entry={ 
                    'year':year,
                    'dep':year1,
                    'hor':hors,
                    'student':totalstudent
                   
            }
            department_list.append(entry)

    data={
        
        'ug':department_list,
        'pg':pg_fun()
       
    }
    return render(request,'backend/mainpage.html',data)
def pg_fun():
    pg=course_pg.objects.all()
    date=entry_panal.objects.all()
    date1=date[::-1]
    day=int(date1[0].day)
    datechek='i.day'+ str(day)     
    year11=[]
    department_list=[]
    
    for i in pg: 
        year=i.department
        year11.append(year)        
        for l in range(3):
            totalstudent=0
            year1=year+str(f'_{l+1}YEAR')
            student=student_details.objects.filter(key=year1)
        
        #student_details.objects.filter(regnumber=i.regnumber).update(**{datechek1: 'venkateshbabu1'})
            hors="NOT Attendance Take"
            b=0 
            for i in student:
                #print(i.name)
                totalstudent+=1
                a=0 
                #student_details.objects.filter(regnumber=i.regnumber).update(**{datechek1: ''})
                for ia in eval(datechek):
                    a+=1
                b=a
            print('theheeheh',b)
            if b ==5:
                hors="Attendance Take 1st Hors"
            elif b==10:
                hors="Attendance Take 2nd Hors"
            elif b==15:
                hors="Attendance Take 3rd Hors"
            elif b==20:
                hors="Attendance Take 4th Hors"
            elif b==25:
                hors="Attendance Take 5th Hors"
            entry={ 
                    'year':year,
                    'dep':year1,
                    'hor':hors,
                    'student':totalstudent
                   
            }
            department_list.append(entry)

    
    return department_list