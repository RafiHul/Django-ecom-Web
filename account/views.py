from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User

from .forms import SignupForm, TopupSaldo, EditProfileForm, EditImageForm
from .models import UserProfile
from core.models import Produk


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            get_username = form.cleaned_data['username']
            user = User.objects.get(username=get_username)
            wall = UserProfile(username_acc=user)
            wall.save()

            return redirect('/login/')
    else:
        form = SignupForm()
    
    return render(request, 'account/signup.html',{
        'form': form
    })

@login_required
def logout_user(request):
    logout(request)
    return redirect('core:index')

@login_required
def profile(request):

    profile = UserProfile.objects.get(username_acc=request.user)
    return render(request, 'account/profile.html', {
        'profile': profile,
    })

@login_required
def topup(request):
    if request.method == 'POST':
        form = TopupSaldo(request.POST)
        if form.is_valid():
            saldo = form.cleaned_data['saldo']

            if saldo > 0:
                user_profile = UserProfile.objects.get(username_acc=request.user)
                user_profile.saldo += saldo
                user_profile.save()
                return redirect('account:profile')
            else:
                messages.error(request, "Masukkan angka yang benar")
        else:
            messages.error(request, "Form tidak valid. Pastikan Anda memasukkan angka yang benar.")
    else:
        form = TopupSaldo()
    
    formsd = UserProfile.objects.get(username_acc=request.user)
    return render(request, 'account/topup.html', {
        'form': formsd.saldo,
        'form1': form,
    })

@login_required
def settings(request):
    uss_prof = UserProfile.objects.get(username_acc=request.user)
    if request.method == "POST":
        form = EditProfileForm(request.POST,instance=request.user)
        
        if form.is_valid():
            form.save()
            return redirect('account:profile')

    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'account/settings.html',{
        'form':form,
    })

def another_profile(request,user):
    qck = get_object_or_404(UserProfile, username_acc=user)
    gyat = User.objects.get(username=user)
    ff = Produk.objects.filter(created_by=gyat)
    return render(request, 'account/another_profile.html',{
        'uss':qck,
        'created_by':ff,
    })
    
@login_required
def vendor_menu(request):
    produk = Produk.objects.filter(created_by=request.user)
    return render(request, 'account/vendor_menu.html',{
        'produk':produk
    })

@login_required
def settingprofile(request):
    uss_prof = get_object_or_404(UserProfile,username_acc=request.user)
    if request.method == 'POST':
        form = EditImageForm(request.POST,request.FILES,instance=uss_prof)
        if form.is_valid():
            form.save()
            return redirect('account:profile')
    else:
        form = EditImageForm(instance=uss_prof)

    return render(request, 'account/settingprofile.html',{'form':form})