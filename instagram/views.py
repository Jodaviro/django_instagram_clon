""" Instagram views """
#django
from django.shortcuts import render
#utilities

#models
from users.models import Profile

#forms
from users.forms import SignUpForm
from users.forms import ProfileForm



def test(request):
    profile = request.user.profile
    instance = Profile.objects.get(pk=profile.pk)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()

    else:
        form = ProfileForm(instance=instance)


    # if request.method == 'POST':
    #     form = SignUpForm(request.POST)
    #     if form.is_valid() :
    #         form.save()
    # else:
    #     form = SignUpForm
    return render(request,'test.html', {'form': form})