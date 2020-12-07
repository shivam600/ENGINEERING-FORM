from django.db import models
from django.contrib.auth.models import User



# Create your models here
class stream(models.Model):
   title=models.CharField(max_length=100)

   def __str__(self):
      return self.title

class college_name(models.Model):
   title=models.CharField(max_length=100)

   def __str__(self):
      return self.title      

class student(models.Model):
   fullname=models.CharField(max_length=100)
   contact_no=models.CharField(max_length=15)
   address=models.CharField(max_length=100)
   stream=models.ForeignKey(stream,on_delete=models.CASCADE)
   college_name=models.ForeignKey(college_name,on_delete=models.CASCADE)
   user=models.OneToOneField(User,on_delete=models.CASCADE)


   def __str__(self):
      return str(self.user)      


   # first_name=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
   # last_name=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
   # email=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
   # password1=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
   # password2=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

# class information(models.Model):
#    Another_contact_no=models.CharField(max_length=100)
#    Roll_no=models.CharField(max_length=15)
#    Percentage=models.IntegerField()
#    Favourite_subject=models.CharField(max_length=15)
#    user2=models.ForeignKey(User,on_delete=models.CASCADE)
#    password1=models.CharField(max_length=15)
#    password2=models.CharField(max_length=15)
   



