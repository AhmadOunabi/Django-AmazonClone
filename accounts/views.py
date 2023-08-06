from django.shortcuts import render
from .forms import SignupForm

# Create your views here.

def signup(request):
    if request.method == 'POST':
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            
            # Send Gmail Confirmation Code
            
            #redirect to Confirmation Code page
            
    else:
            form=SignupForm()
    return render(request, 'registration/signup.html', {'form': form})