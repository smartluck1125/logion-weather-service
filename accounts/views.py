from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import send_mail
from django.template.loader import get_template
from django.template import Context
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login


# Create your views here.
def IndexView(request):
  return render(request, 'accounts/index.html', {'title' : 'index'})
########### register here ##################################### 

def RegisterView(request):
  if(request.method == 'POST'):
    form = UserRegisterForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      email = form.cleaned_data.get('email')
      ####################### mail system #################################### 
      htmly = get_template('accounts/email.html')
      d = { 'username': username }
      subject, from_email, to = 'welcome', 'ivan.super.dev@gmail.com', email
      html_content = htmly.render(d)
      msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
      msg.attach_alternative(html_content, "text/html")
      # msg.send()
      ################################################################## 
      messages.success(request, f'Your account has been created ! You are now able to log in')
      return redirect('login')
  else:
    form = UserRegisterForm()
  return render(request, 'accounts/register.html', {'form' : form, 'title': 'register'})
#######################################
def LoginView(request):
  if request.method == 'POST':
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username = username, password = password)
    if user is not None:
        form = login(request, user)
        messages.success(request, f' welcome {username} !!')
        return redirect('index')
    else:
        messages.info(request, f'account done not exit plz sign in')
  form = AuthenticationForm()
  return render(request, 'accounts/login.html', {'form':form, 'title':'log in'})
  ###########################################
def LogOutView(request):
  
  return render(request, 'accounts/log_out.html', {'title' : 'index'})