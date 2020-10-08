from django.shortcuts import render
from AppTwo.forms import NewUserForm

# Create your views here.

def index(request):
    return render(request,'AppTwo/index.html')

def users(request):
    form = NewUserForm()

    # after submission the form
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        # printing the values of the form fields
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("Invalid!")
    return render(request,'AppTwo/user.html',{'form':form})

def help(request):
    return render(request,'AppTwo/help.html')
