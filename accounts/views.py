from django.shortcuts import redirect, render
from .forms import SignupForm, UserActivationForm
from .models import Profile,Phones,Address
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            
            # Get the Data from the form 
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            
            form.save()
            #get the User
            user = User.objects.get(username=username)
            #get User's Profile
            user_profile = Profile.objects.get(user=user)
            # Send Gmail Confirmation Code
            send_mail(
                "Activation Code",
                f"Hello {username} \n use this Code to activate your account \n {user_profile.code}",
                "ahmad@yahoo.com",
                [email],
                fail_silently=False,
            )
            #redirect to Confirmation Code page
            return redirect(f"/accounts/{username}/activate")
            
    else:
            form=SignupForm()
    return render(request, 'registration/signup.html',{'form': form})




def user_activate(request, username):
    user=User.objects.get(username=username)
    user_profile=Profile.objects.get(user=user)
    
    if request.method == 'POST':
        form=UserActivationForm(request.POST)
        if form.is_valid():
            code=form.cleaned_data['code']
            if code == user_profile.code:
                user.is_active == True
                user.save()
                user_profile.code=''
                user_profile.save()
                return redirect('/')
    else:
        form=UserActivationForm()
    
    return render(request, 'registration/activate.html',{'form':form} )