from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import Http404, HttpResponse, HttpResponseRedirect
from .models import Profile, Reading
from .forms import ProfileForm, ProfileInfoForm, ReadingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib import messages

#user = get_user_model()

# Create your views here.


def home(request):
    return render(request, 'app/home.html')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = ProfileForm(data=request.POST)
        profile_form = ProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
            messages.success(request, 'User was Successfully created!',  extra_tags='alert')
            return redirect('login')
        else:
            print(user_form.errors, profile_form.errors)
            messages.warning(request, 'sorry, something went wrong!',  extra_tags='alert')

    else:
        user_form = ProfileForm()
        profile_form = ProfileInfoForm()

    return render(request, 'app/index.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


@login_required
def reading(request):
    registered = False
    if request.method == 'POST' or None:
        form = ReadingForm(data=request.POST)
        if form.is_valid() or None:
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            registered = True
            messages.success(request, 'Data successfully Created',  extra_tags='alert')
            return HttpResponseRedirect('app:reading')

        else:
            messages.warning(request, 'Data Not Created',  extra_tags='alert')
    else:
        form = ReadingForm(data=request.POST)
    return render(request, 'app/reading.html', {'form': form, 'registered': registered})


@login_required
def reading_update(request, pk):

    if request.user.is_superuser:
        form = get_object_or_404(Reading, pk=pk)
    else:
        form = get_object_or_404(Reading, pk=pk, user=request.user)
    form = ReadingForm(request.POST or None, instance=form)
    if form.is_valid():
        form.save()
        return redirect('app:list')
    return render(request, 'app/reading.html', {'form': form})


@login_required
def reading_delete(request, pk):

    if request.user.is_superuser:
        post = get_object_or_404(Reading, pk=pk)
    else:
        post = get_object_or_404(Reading, pk=pk, user=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('app:list')
    return render(request, 'app/deleteview.html', {'object': post})


@login_required
def datareading(request):
    if request.user.is_superuser:
        user = Reading.objects.all().order_by('-Date')
    else:
        user = Reading.objects.filter(user=request.user).order_by('-Date')
    return render(request, 'app/listview.html', {'data': user})


def datefilter(request):
    if request.method == 'POST':
        srch = request.POST['search']

        if srch:
            if request.user.is_superuser:
                match = Reading.objects.filter(Date__icontains=srch)
            else:
                match = Reading.objects.filter(user=request.user, Date__icontains=srch)

            if match:
                return render(request, 'app/listview.html', {'sr': match})
            else:
                messages.error(request, 'no result found')
        else:
            return HttpResponseRedirect(reverse('app:search'))
    return render(request, 'app/listview.html')





@login_required
def datadetails(request, pk):
    if request.user.is_superuser:
        post = get_object_or_404(Reading, pk=pk)
    else:
        post = get_object_or_404(Reading, pk=pk, user=request.user)
    return render(request, 'app/details.html', {'object': post})
