from datetime import datetime
import os
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from career_app.models import *
from .prediction_fn import read_pdf,predict
def logout(request):
    auth.logout(request)
    return render(request,'homepage/loginindex.html')

def logins(request):
    return render(request,'homepage/loginindex.html')

def logincheck(request):
    uname=request.POST['textfield']
    pswd=request.POST['textfield2']
    try:
        ob=login.objects.get(username=uname,password=pswd)

        if ob.type == "admin":
            ob1=auth.authenticate(username="admin",password="admin")
            if ob1 is not None:
                auth.login(request,ob1)
            return HttpResponse('''<script>alert("welcome");window.location='/admin_home'</script>''')
        elif ob.type == "student":
            ob1 = auth.authenticate(username="admin", password="admin")
            if ob1 is not None:
                auth.login(request, ob1)
            request.session['lid'] = ob.id
            return HttpResponse('''<script>alert("welcome");window.location='/student_homepage'</script>''')
        elif ob.type == "expert":
            request.session['lid']=ob.id
            ob1 = auth.authenticate(username="admin", password="admin")
            if ob1 is not None:
                auth.login(request, ob1)
            return HttpResponse('''<script>alert("welcome");window.location='/expert_homepage'</script>''')
        elif ob.type == "agency":
            request.session['lid']=ob.id
            ob1 = auth.authenticate(username="admin", password="admin")
            if ob1 is not None:
                auth.login(request, ob1)
            return HttpResponse('''<script>alert("welcome");window.location='/add_homepage'</script>''')

        else:
            return HttpResponse('''<script>alert("invalid username or password");window.location='/'</script>''')
    except:
        return HttpResponse('''<script>alert("invalid username or password");window.location='/'</script>''')
@login_required(login_url='/')
def add_agency(request):
    return render(request,'homepage/add agency.html')



def mainindex(request):
    return render(request,'mainindex.html')

@login_required(login_url='/')

def addagencypost(request):
    name=request.POST['textfield']
    place=request.POST['place']
    post=request.POST['post']
    pin=request.POST['pin']
    phno=request.POST['phone']
    email=request.POST['email']
    profile=request.FILES['file']
    fs=FileSystemStorage()
    fsave=fs.save(profile.name,profile)
    username=request.POST['username']
    password=request.POST['password']
    ob=login()
    ob.username=username
    ob.password=password
    ob.type='agency'
    ob.save()
    obu=agency()
    obu.name=name
    obu.place=place
    obu.post=post
    obu.pin=pin
    obu.phno=phno
    obu.email=email
    obu.photo=fsave
    obu.LOGIN=ob
    obu.save()
    return HttpResponse('''<script>alert("Added");window.location='/manage_agency'</script>''')


@login_required(login_url='/')
def editagn(request,id):
    ob=agency.objects.get(id=id)
    request.session['ag']=id
    return render(request,'homepage/editagn.html',{'v':ob})

@login_required(login_url='/')
def deleteag(request,id):
    ob=agency.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location='/manage_agency'</script>''')

@login_required(login_url='/')
def delete_tips(request,id):
    ob=tipstable.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location='/manage_tips'</script>''')


@login_required(login_url='/')
def editagnpost(request):
    if 'file' in request.FILES:
        name=request.POST['textfield']
        place=request.POST['place']
        post=request.POST['post']
        pin=request.POST['pin']
        phno=request.POST['phone']
        email=request.POST['email']
        profile=request.FILES['file']
        fs=FileSystemStorage()
        fsave=fs.save(profile.name,profile)
        obu=agency.objects.get(id=request.session['ag'])
        obu.name=name
        obu.place=place
        obu.post=post
        obu.pin=pin
        obu.phno=phno
        obu.email=email
        obu.photo=fsave
        obu.save()
        return HttpResponse('''<script>alert("Added");window.location='/manage_agency'</script>''')
    else:
        name = request.POST['textfield']
        place = request.POST['place']
        post = request.POST['post']
        pin = request.POST['pin']
        phno = request.POST['phone']
        email = request.POST['email']
        obu = agency.objects.get(id=request.session['ag'])
        obu.name = name
        obu.place = place
        obu.post = post
        obu.pin = pin
        obu.phno = phno
        obu.email = email
        obu.save()
        return HttpResponse('''<script>alert("Added");window.location='/manage_agency'</script>''')




@login_required(login_url='/')
def add_expert(request):
    return render(request,'homepage/add  expert.html')

@login_required(login_url='/')
def addexpertpost(request):
    fname=request.POST['fname']
    lname=request.POST['lname']
    place=request.POST['place']
    post=request.POST['post']
    pin=request.POST['pin']
    phno=request.POST['phno']
    email=request.POST['email']
    profile=request.FILES['file']
    fs = FileSystemStorage()
    fsave = fs.save(profile.name, profile)
    username = request.POST['username']
    password = request.POST['password']
    ob = login()
    ob.username = username
    ob.password = password
    ob.type = 'expert'
    ob.save()
    obu=expert()
    obu.fname=fname
    obu.LOGIN=ob
    obu.lname=lname
    obu.place = place
    obu.post = post
    obu.pin = pin
    obu.phno = phno
    obu.email = email
    obu.photo = fsave
    obu.save()
    return HttpResponse('''<script>alert("Added");window.location='/manage_expert'</script>''')




@login_required(login_url='/')
def editexp(request,id):
    ob=expert.objects.get(id=id)
    request.session['ex']=id
    return render(request,'homepage/editexp.html',{'v':ob})



@login_required(login_url='/')
def deleteexp(request,id):
    ob=expert.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location='/manage_agency'</script>''')






@login_required(login_url='/')
def editexppost(request):
    if 'file' in request.FILES:
        fname=request.POST['fname']
        lname=request.POST['lname']
        place=request.POST['place']
        post=request.POST['post']
        pin=request.POST['pin']
        phno=request.POST['phno']
        email=request.POST['email']
        profile=request.FILES['file']
        fs = FileSystemStorage()
        fsave = fs.save(profile.name, profile)
        obu=expert.objects.get(id=request.session['ex'])
        obu.fname=fname
        obu.lname=lname
        obu.place = place
        obu.post = post
        obu.pin = pin
        obu.phno = phno
        obu.email = email
        obu.photo = fsave
        obu.save()
        return HttpResponse('''<script>alert("Added");window.location='/manage_expert'</script>''')
    else:
        fname = request.POST['fname']
        lname = request.POST['lname']
        place = request.POST['place']
        post = request.POST['post']
        pin = request.POST['pin']
        phno = request.POST['phno']
        email = request.POST['email']
        obu =expert.objects.get(id=request.session['ex'])
        obu.fname = fname
        obu.lname = lname
        obu.place = place
        obu.post = post
        obu.pin = pin
        obu.phno = phno
        obu.email = email
        obu.save()
        return HttpResponse('''<script>alert("Added");window.location='/manage_expert'</script>''')







@login_required(login_url='/')
def add_notification(request):
    return render(request, 'homepage/add notification.html')


@login_required(login_url='/')
def add_notification_search(request):
    notification=request.POST['textfield']
    ob=notificationtable.objects.filter(date__istartswith=notification)
    return render(request, 'homepage/mng_notn.html',{'val':ob})


@login_required(login_url='/')
def addnotification(request):
    notifications=request.POST['textfield']
    ob=notificationtable()
    ob.notification=notifications
    ob.date=datetime.now()
    ob.save()
    return HttpResponse('''<script>alert("Added");window.location='/admin_home'</script>''')





@login_required(login_url='/')
def admin_home(request):
    return render(request, 'homepage/admin home.html')

@login_required(login_url='/')
def block_and_unblock(request):
    ob=agency.objects.all()
    return render(request, 'homepage/block and unblock agency.html',{'val':ob})


@login_required(login_url='/')
def manage_agency(request):
    ob=agency.objects.all()
    return render(request, 'homepage/manage agency.html',{'val':ob})


@login_required(login_url='/')
def manage_agency_search(request):
    name=request.POST['textfield']
    ob=agency.objects.filter(name__istartswith=name)
    return render(request, 'homepage/manage agency.html',{'val':ob})

@login_required(login_url='/')
def manage_agency_search1(request):
    name=request.POST['textfield']
    ob=agency.objects.filter(name__istartswith=name)
    return render(request, 'homepage/block and unblock agency.html',{'val':ob})



@login_required(login_url='/')
def manage_expert(request):
    ob=expert.objects.all()
    return render(request, 'homepage/manage expert.html',{'val':ob})

@login_required(login_url='/')
def manage_expert_search(request):
    name=request.POST['textfield']
    ob=expert.objects.filter(fname__istartswith=name)
    return render(request, 'homepage/manage expert.html',{'val':ob})


@login_required(login_url='/')
def view_complaint_and_sendreply(request):
    ob = complainttable.objects.all()
    print(ob)
    return render(request, 'homepage/view complaint and send reply.html',{'val':ob})

@login_required(login_url='/')
def reply(request,id):
    ob=complainttable.objects.get(id=id)
    request.session['cid']=id
    return render(request, 'homepage/reply.html',{'val':ob})

@login_required(login_url='/')
def replysend(request):
    re=request.POST['textfield']
    ob=complainttable.objects.get(id=request.session['cid'])
    ob.reply=re
    ob.save()
    return HttpResponse('''<script>alert("send-");window.location='/view_complaint_and_sendreply'</script>''')

@login_required(login_url='/')
def view_feedback_and_rating(request):
    ob = feedbacktable.objects.all()
    return render(request, 'homepage/view feedback and rating.html',{'val':ob})




@login_required(login_url='/')
def view_student(request):
    ob=student.objects.all
    return render(request, 'homepage/view student.html',{'val':ob})


@login_required(login_url='/')
def student_search1(request):
    name=request.POST['textfield']
    ob=student.objects.filter(fname__istartswith=name)
    return render(request, 'homepage/view student.html',{'val':ob})




@login_required(login_url='/')
def mng_notn(request):
    ob=notificationtable.objects.all
    return render(request, "homepage/mng_notn.html",{'val':ob})

@login_required(login_url='/')
def dlt_notn(request,id):
    ob=notificationtable.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location='/mng_notn'</script>''')

@login_required(login_url='/')
def add_doubt(request):
    return render(request,'student module/add doubt.html')





@login_required(login_url='/')
def doubt_clearance(request):
    return render(request,'student module/doubt clearance.html')


@login_required(login_url='/')
def send_complaint_and_view_reply1(request):
    print(request.session['lid'])
    ob=complainttable.objects.filter(LOGIN__id=request.session['lid'])
    return render(request,'student module/send complaint and view reply.html',{'val':ob})


@login_required(login_url='/')
def send_rating_and_feedback1(request):
    return render(request,'student module/send rating and feedback.html')


@login_required(login_url='/')
def student_homepage(request):
    return render(request,'student module/student homepage.html')

@login_required(login_url='/')
def upload_resume(request):
    return render(request,'student module/upload resume.html')




@login_required(login_url='/')
def viewapplicationstts(request):
    ob=apply.objects.filter(STUDENT__LOGIN__id=request.session['lid'])
    return render(request,'student module/view_application_status.html',{'val':ob})



@login_required(login_url='/')
def upres(request):
    res=request.FILES['file']
    fs=FileSystemStorage()
    fn = fs.save(res.name, res)
    ob=resume()
    ob.resume=fn
    ob.date=datetime.now()
    ob.STUDENT=student.objects.get(LOGIN__id=request.session['lid'])
    ob.save()
    txt=read_pdf(os.path.join(r"C:\Users\Aleefa\Desktop\New folder\career_navigator\media",fn))
    print(txt,"=======================================")
    res=predict(txt)
    return render(request,"student module/prediction result.html",{"val":res})
    # return HttpResponse('''<script>alert("Uploaded");window.location='/student_homepage'</script>''')

@login_required(login_url='/')
def view_job_vaccancy_and_apply(request):
    ob = jobs.objects.all()
    return render(request,'student module/view job vaccancy and apply.html',{'val':ob})

@login_required(login_url='/')
def japply(request,id):
    obb=apply.objects.filter(STUDENT__LOGIN__id=request.session['lid'],JOB__id=id,status="Accepted")
    if len(obb) == 0:
        ob=apply()
        ob.STUDENT=student.objects.get(LOGIN__id=request.session['lid'])
        ob.JOB=jobs.objects.get(id=id)
        ob.date=datetime.now()
        ob.status='pending'
        ob.save()
        return HttpResponse('''<script>alert("apply");window.location='/view_job_vaccancy_and_apply'</script>''')

    else:
        return HttpResponse('''<script>alert("already applied");window.location='/view_job_vaccancy_and_apply'</script>''')



@login_required(login_url='/')
def view_tips(request):
    ob =tipstable.objects.all()
    return render(request,'student module/view tips.html',{'val':ob})

@login_required(login_url='/')
def tip_search(request):
    tips=request.POST['textfield']
    ob=tipstable.objects.filter(tips__istartswith=tips)
    return render(request, 'student module/view tips.html', {'val': ob})

@login_required(login_url='/')
def view_videos(request):
    ob = video.objects.all()
    return render(request,'student module/view videos.html',{'val':ob})

@login_required(login_url='/')
def view_notifications(request):
    ob = notificationtable.objects.all()
    print(ob)
    return render(request,'student module/view notification.html',{'val':ob})

@login_required(login_url='/')
def add_tips(request):
    tip=request.POST['textfield']
    ob=tipstable()
    ob.tips=tip
    ob.date = datetime.now()
    ob.EXPERT=expert.objects.get(LOGIN__id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("Added");window.location='/expert_homepage'</script>''')

@login_required(login_url='/')
def add_tip(request):
    return render(request,'expert module/add tip.html')



#======================================================================================================================
@login_required(login_url='/')
def chat_with_expert(request):
    ob = expert.objects.all()
    return render(request,'student module/fur_chat.html')

@login_required(login_url='/')
def chateview(request):
    ob = expert.objects.all()
    d=[]
    for i in ob:
        r={"name":i.fname,'photo':i.photo.url,'email':i.email,'loginid':i.LOGIN.id}
        d.append(r)
    return JsonResponse(d, safe=False)

@login_required(login_url='/')
def coun_msge(request,id):

    ob1=chat.objects.filter(from_id=id,to_id=request.session['lid'])
    ob2=chat.objects.filter(from_id=request.session['lid'],to_id=id)
    print("===================")
    combined_chat = ob1.union(ob2)
    combined_chat=combined_chat.order_by('id')
    res=[]
    for i in combined_chat:
        res.append({"from_id":i.from_id.id,"msg":i.message,"date":i.date,"chat_id":i.id})
    obu=expert.objects.get(LOGIN__id=id)
    return JsonResponse({"data":res,"name":obu.fname,"photo":obu.photo.url,"user_lid":obu.LOGIN.id})





@login_required(login_url='/')
def chat_with_student(request):
    ob = student.objects.all()
    return render(request,'expert module/fur_chat.html',{'val':ob})


@login_required(login_url='/')
def chatview(request):
    ob = student.objects.all()
    d=[]
    for i in ob:
        r={"name":i.fname,'photo':i.photo.url,'email':i.email,'loginid':i.LOGIN.id}
        d.append(r)
    return JsonResponse(d, safe=False)




@login_required(login_url='/')
def coun_msg(request,id):

    ob1=chat.objects.filter(from_id=id,to_id=request.session['lid'])
    ob2=chat.objects.filter(from_id=request.session['lid'],to_id=id)
    print("===================")
    combined_chat = ob1.union(ob2)
    combined_chat=combined_chat.order_by('id')
    res=[]
    for i in combined_chat:
        res.append({"from_id":i.from_id.id,"msg":i.message,"date":i.date,"chat_id":i.id})

    obu=student.objects.get(LOGIN__id=id)


    return JsonResponse({"data":res,"name":obu.fname,"photo":obu.photo.url,"user_lid":obu.LOGIN.id})






@login_required(login_url='/')
def coun_insert_chat(request,msg,id):
    print("===",msg,id)
    ob=chat()
    ob.from_id=login.objects.get(id=request.session['lid'])
    ob.to_id=login.objects.get(id=id)
    ob.message=msg
    ob.date=datetime.now().strftime("%Y-%m-%d")
    ob.save()

    return JsonResponse({"task":"ok"})
    # refresh messages chatlist










#######################################################################################################################

@login_required(login_url='/')
def expert_homepage(request):
    return render(request,'expert module/expertindex.html')


@login_required(login_url='/')
def manage_tips(request):
    ob =tipstable.objects.filter(EXPERT__LOGIN__id=request.session['lid'])

    return render(request,'expert module/manage tips.html',{'val':ob})

@login_required(login_url='/')
def send_rating_and_feedback(request):
    return render(request,'expert module/send rating and feedback.html')


@login_required(login_url='/')
def view_notification(request):
    ob = notificationtable.objects.all()
    print(ob)
    return render(request,'expert module/view notification.html',{'val':ob})

@login_required(login_url='/')
def add_and_manage_video(request):
    ob=video.objects.filter(AGENCY__LOGIN__id=request.session['lid'])
    return render(request,'agency module/add and manage video.html',{'val':ob})


@login_required(login_url='/')
def add_job(request):
    return render(request,'agency module/add job.html')


@login_required(login_url='/')
def add_job1(request):
    jobx=request.POST['textfield']
    details=request.POST['textfield2']
    vaccancy=request.POST['textfield3']
    salary_range=request.POST['textfield4']
    last_date=request.POST['textfield5']
    ob=jobs()
    ob.AGENCY=agency.objects.get(LOGIN__id=request.session['lid'])
    ob.job=jobx
    ob.details=details
    ob.vaccancy=vaccancy
    ob.salary_range=salary_range
    ob.last_date=last_date
    ob.save()
    return HttpResponse('''<script>alert("Added");window.location='/manage_job_details'</script>''')

@login_required(login_url='/')
def add_placed_student(request):
    return render(request,'agency module/add placed student.html')


@login_required(login_url='/')
def placed_stud_search(request):
    notification=request.POST['textfield']
    ob=notificationtable.objects.filter(date__istartswith=notification)
    return render(request, 'homepage/mng_notn.html',{'val':ob})


@login_required(login_url='/')
def add_video(request):
    return render(request,'agency module/add video.html')

@login_required(login_url='/')
def addvideo(request):
    print(request.POST)
    profile = request.FILES['file']
    fs = FileSystemStorage()
    fsave = fs.save(profile.name, profile)
    nme=request.POST['textfield']
    ob=video()
    ob.video=fsave
    ob.name=nme
    ob.date=datetime.now()
    ob.AGENCY=agency.objects.get(LOGIN__id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("Added");window.location='/add_and_manage_video'</script>''')








@login_required(login_url='/')
def add_homepage(request):
    return render(request,'agency module/agency homepage.html')

@login_required(login_url='/')
def doubt_reply(request):
    return render(request,'agency module/doubt reply.html')

@login_required(login_url='/')
def doubt(request):
    return render(request, 'agency module/doubt.html')



@login_required(login_url='/')
def view_notification2(request):
    ob = notificationtable.objects.all()
    print(ob)
    return render(request,'agency module/view notification.html',{'val':ob})



@login_required(login_url='/')
def  manage_job_details(request):
    ob=jobs.objects.filter(AGENCY__LOGIN__id=request.session['lid'])
    return render(request,'agency module/manage job details.html',{'val':ob})

@login_required(login_url='/')
def manage_placed_student_details(request):
    ob=apply.objects.filter(JOB__AGENCY__LOGIN__id=request.session['lid'],status = 'Accepted')
    ob1=jobs.objects.filter(AGENCY__LOGIN__id=request.session['lid'])
    return render(request,'agency module/manage placed student details.html',{'val':ob,'val1':ob1})


@login_required(login_url='/')
def search_placed_student_details(request):
    jid=request.POST['select']
    ob=apply.objects.filter(JOB__AGENCY__LOGIN__id=request.session['lid'],status = 'Accepted',JOB__id=jid)
    ob1 = jobs.objects.filter(AGENCY__LOGIN__id=request.session['lid'])
    return render(request,'agency module/manage placed student details.html',{'val':ob,'val1':ob1})


@login_required(login_url='/')
def  view_req_stu(request):
    ob=apply.objects.filter(JOB__AGENCY__LOGIN__id=request.session['lid'])
    return render(request,'agency module/view_req_stu.html',{'val':ob})

@login_required(login_url='/')
def  view_req_stu_search(request):
    name=request.POST['textfield']
    ob=apply.objects.filter(JOB__AGENCY__LOGIN__id=request.session['lid'],STUDENT__fname__icontains=name)
    return render(request,'agency module/view_req_stu.html',{'val':ob})

@login_required(login_url='/')
def acceptreq(request,id):
    ob=apply.objects.get(id=id)

    ob.status='Accepted'
    ob.save()
    return HttpResponse('''<script>alert("Accepted");window.location='/view_req_stu'</script>''')

def first(request):
    return render(request,'homepage/firstpage.html')




@login_required(login_url='/')
def rejectreq(request,id):
    ob=apply.objects.get(id=id)

    ob.status='Rejected'
    ob.save()
    return HttpResponse('''<script>alert("Rejected");window.location='/view_req_stu'</script>''')


@login_required(login_url='/')
def send_complaint_and_view_reply(request):
    ob=complainttable.objects.filter(LOGIN__id=request.session['lid'])
    return render(request,'agency module/send complaint and view reply.html',{'val':ob})


@login_required(login_url='/')
def sendcomagency(request):
    comp=request.POST['textfield']
    ob=complainttable()
    ob.complaint=comp
    ob.date=datetime.now()
    ob.reply='pending'
    ob.LOGIN=login.objects.get(id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("Added");window.location='/send_complaint_and_view_reply'</script>''')


@login_required(login_url='/')
def sendcomstud(request):
    comp=request.POST['textfield']
    ob=complainttable()
    ob.complaint=comp
    ob.date=datetime.now()
    ob.reply='pending'
    ob.LOGIN=login.objects.get(id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("Added");window.location='/send_complaint_and_view_reply1'</script>''')




def send_rating_and_feedback(request):
    return render(request,'agency module/send rating and feedback.html')

@login_required(login_url='/')
def agenfeedback(request):
    feedback=request.POST['textfield']
    rating=request.POST['select']
    ob=feedbacktable()
    ob.feedback=feedback
    ob.date=datetime.today()
    ob.rating=rating

    ob.LOGIN=login.objects.get(id=request.session['lid'])
    ob.save()
    return HttpResponse('''<script>alert("sent");window.location='/add_homepage '</script>''')






@login_required(login_url='/')
def view_profile(request):
    ob=agency.objects.get(LOGIN__id=request.session['lid'])
    return render(request,'agency module/view profile.html',{'val':ob})



def reg_index(request):
    return render(request,'reg_index.html')



def s_registration(request):
    return render(request,'sregindex.html')


def s_registration_post(request):
    fname=request.POST['fname']
    lname=request.POST['lname']
    dob=request.POST['dob']
    gender=request.POST['radiobutton']
    place=request.POST['place']
    post=request.POST['post']
    pin=request.POST['pin']
    phno=request.POST['phone']
    email=request.POST['email']
    profile=request.FILES['file']
    fs=FileSystemStorage()
    fsave=fs.save(profile.name,profile)
    username=request.POST['username']
    ob=login.objects.all()
    for i in ob:
        unm = i.username
        if username == unm:
            return HttpResponse('''<script>alert("Already exists");window.location='/'</script>''')
    password=request.POST['password']
    ob=login()
    ob.username=username
    ob.password=password
    ob.type='student'
    ob.save()
    obu=student()
    obu.fname=fname
    obu.lname=lname
    obu.dob=dob
    obu.gender=gender
    obu.place=place
    obu.post=post
    obu.pin=pin
    obu.email=email
    obu.phno=phno
    obu.photo=fsave
    obu.LOGIN=ob
    obu.save()
    return HttpResponse('''<script>alert("Registered successfully");window.location='/'</script>''')

@login_required(login_url='/')
def block_agency(request,id):
    ob=login.objects.get(id=id)
    ob.type='blocked'
    ob.save()
    return HttpResponse('''<script>alert("Blocked successfully");window.location='/block_and_unblock'</script>''')

@login_required(login_url='/')
def unblock_agency(request,id):
    ob=login.objects.get(id=id)
    ob.type='agency'
    ob.save()
    return HttpResponse('''<script>alert("Unblocked successfully");window.location='/block_and_unblock'</script>''')


@login_required(login_url='/')
def view_stud(request):
    ob = student.objects.get(LOGIN__id=request.session['lid'])
    return render(request, 'student module/view stud.html', {'val': ob,"d":str( ob.dob)})


@login_required(login_url='/')
def profile(request):
    ob = student.objects.get(LOGIN__id=request.session['lid'])
    return render(request, 'student module/profile.html', {'val': ob,"d":str( ob.dob)})


@login_required(login_url='/')
def view_stud_update(request):
    fname=request.POST['fname']
    lname=request.POST['lname']
    dob=request.POST['dob']
    gender=request.POST['radiobutton']
    place=request.POST['place']
    post=request.POST['post']
    pin=request.POST['pin']
    phno=request.POST['phone']
    email=request.POST['email']
    obu= student.objects.get(LOGIN__id=request.session['lid'])
    obu.fname=fname
    obu.lname=lname
    obu.dob=dob
    obu.gender=gender
    obu.place=place
    obu.post=post
    obu.pin=pin
    obu.email=email
    obu.phno=phno
    try:
        profile = request.FILES['file']
        fs = FileSystemStorage()
        fsave = fs.save(profile.name, profile)
        obu.photo=fsave
    except:
        pass

    obu.save()
    return HttpResponse('''<script>alert("Updated successfully");window.location='/view_stud'</script>''')

def likepost(request):
    username = request.GET['username']
    print(username)
    data = {
        'is_taken': login.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = "A user with this username already exists."
        # return HttpResponse("A user with this username already exists.")
    return JsonResponse(data)