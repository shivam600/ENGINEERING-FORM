from django.shortcuts import render,redirect
from .forms import studentForm,ExtendedUserCreationForm,EditProfileForm
from django.contrib import messages
from .models import student
from django.contrib.auth.forms import UserChangeForm



 

# Create your views here.

def add_student(request,id=0):
    if request.method == "GET":
        if id==0:
            form=studentForm()
            formu=ExtendedUserCreationForm()      
        else:
            students=student.objects.get(pk=id)  
            form=studentForm(instance=students)
            # user=ExtendedUserCreationForm.objects.get(pk=id)  
            formu=EditProfileForm(instance=students.user)
            
            # formu=ExtendedUserCreationForm(instance=susers)
        return render(request,"add_student.html",{"form":form,"formu":formu})
    else:
        if id==0:
            form=studentForm(request.POST)
            formu=ExtendedUserCreationForm(request.POST)
           
        else:
            students=student.objects.get(pk=id)  
            form=studentForm(request.POST,instance=students) 
            # user=ExtendedUserCreationForm.objects.get(pk=id)  
            formu=EditProfileForm(request.POST,instance=students.user)
        
            # formu=ExtendedUserCreationForm(request.POST,instance=susers)
           
 
        if form.is_valid() and formu.is_valid():
            user=formu.save()   
            profile=form.save(commit=False)                              
            profile.user=user

            profile.save()

            messages.info(request,"your form is submitted successfully")
            messages.info(request,"your can send us mail :regarding cancellation and for changing data before or till on 17th october ")
            messages.info(request,"email us on:shivamkaran59@gmail.com")
        else:
            messages.info(request,"Invalid Credentials:TRY AGAIN")   
        return redirect("/")  

def show_student(request): 
    context={"show_student":student.objects.all()}
    return render(request,"show_student.html",context)

# def show_student(request): 
#     context={"show_student":ExtendedUserCreationForm.objects.all()}
#     return render(request,"show_student.html",context)


def student_delete(request,id):
    students=student.objects.get(pk=id)  
    students.delete()
    return redirect("show_student") 

# def register(request):

#     if request.method == "POST":
#         formu=ExtendedUserCreationForm(request.POST)
#         if password1==password2:  
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,"username taken")
#                 return redirect("/")
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request,"email taken")
#                 return redirect("/")
                
#             else:        
#                 user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
#                 user.save();
#                 print("user created")
              
#         else:
#             messages.info(request,"password not matching")     
#             return redirect("/")  
#     else:
#         return render(request,"register.html")   


