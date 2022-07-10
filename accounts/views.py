from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views import View


from .forms import SignupForm, LoginForm


class SignupView(View):
    def get(self, request):
        form = SignupForm()
        return render(request, 'signup.html', {'form':form})
    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            user.is_active=False
            user.save()
            login(request,user)
            return redirect('login')
        return render(request, 'signup.html', {'form':form})


class Login(LoginView):
    form_class = LoginForm
    def form_valid(self, form):
        self.request.session.set_expiry(0)
        self.request.session.modified = True
        return super(Login, self).form_valid(form)

@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')

def home(request):
    return render(request, 'index.html')