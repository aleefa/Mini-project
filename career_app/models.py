from django.db import models

class login(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    type=models.CharField(max_length=50)

class student(models.Model):
    LOGIN=models.ForeignKey(login,on_delete=models.CASCADE)
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    dob=models.DateField()
    gender = models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    post=models.CharField(max_length=50)
    pin = models.IntegerField()
    phno=models.BigIntegerField()
    email = models.CharField(max_length=50)
    photo=models.FileField()

class expert(models.Model):
    LOGIN = models.ForeignKey(login,on_delete=models.CASCADE)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    pin = models.IntegerField()
    phno = models.BigIntegerField()
    email = models.CharField(max_length=50)
    photo = models.FileField()

class agency(models.Model):
    LOGIN = models.ForeignKey(login,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    place = models.CharField(max_length=50)
    post = models.CharField(max_length=50)
    pin = models.IntegerField()
    phno = models.BigIntegerField()
    email = models.CharField(max_length=50)
    photo = models.FileField()

class feedbacktable(models.Model):
    LOGIN = models.ForeignKey(login,on_delete=models.CASCADE)
    feedback = models.CharField(max_length=50)
    date= models.DateField()
    rating=models.FloatField()


class complainttable(models.Model):
    LOGIN = models.ForeignKey(login,on_delete=models.CASCADE)
    complaint= models.CharField(max_length=50)
    date= models.DateField()
    reply= models.CharField(max_length=50)

class notificationtable(models.Model):
    notification= models.CharField(max_length=50)
    date= models.DateField()

class tipstable(models.Model):
    EXPERT= models.ForeignKey(expert,on_delete=models.CASCADE)
    tips= models.CharField(max_length=50)
    date= models.DateField()


class jobs(models.Model):
    AGENCY= models.ForeignKey(agency,on_delete=models.CASCADE)
    job= models.CharField(max_length=50)
    details= models.CharField(max_length=50)
    vaccancy= models.IntegerField()
    salary_range= models.CharField(max_length=50)
    last_date= models.DateField()


class apply(models.Model):
    STUDENT = models.ForeignKey(student, on_delete=models.CASCADE)
    JOB = models.ForeignKey(jobs, on_delete=models.CASCADE)
    date = models.DateField()
    status=models.CharField(max_length=50)



class chat(models.Model):
    from_id= models.ForeignKey(login,on_delete=models.CASCADE,related_name="fid")
    to_id= models.ForeignKey(login,on_delete=models.CASCADE,related_name="tid")
    message= models.CharField(max_length=50)
    date= models.DateField()

class video(models.Model):
    AGENCY= models.ForeignKey(agency,on_delete=models.CASCADE)
    video= models.FileField()
    name= models.CharField(max_length=50)
    date= models.DateField()

class resume(models.Model):
    STUDENT= models.ForeignKey(student,on_delete=models.CASCADE)
    resume= models.CharField(max_length=50)
    date= models.DateField()


class doubt(models.Model):
    STUDENT= models.ForeignKey(student,on_delete=models.CASCADE)
    AGENCY= models.ForeignKey(agency,on_delete=models.CASCADE)
    doubt= models.CharField(max_length=50)
    date= models.DateField()
    reply= models.CharField(max_length=50)

















































