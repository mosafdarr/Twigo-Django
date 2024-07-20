from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from .models import TweetModel
from .forms import TweetForm, UserRegistrationForm


def twigo_home(request):
    twigos = TweetModel.objects.all().order_by('-created_at')
    return render(request, 'tweet/index.html', {"twigos": twigos})

@login_required
def create_twigo(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('twigo_home')
    else:
        form = TweetForm()
    return render(request, 'index.html', {"form": form})

@login_required
def update_twigo_post(request, twigo_id):
    twigo_post = get_object_or_404(TweetModel, pk=twigo_id, user=request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=twigo_post)
        if form.is_valid():
            twigo_post = form.save(commit=False)
            twigo_post.user = request.user
            twigo_post.save()
            return redirect('twigo_home')
    else:
        form = TweetForm(instance=twigo_post)
    return render(request, 'tweet/index.html', {"form": form})

@login_required
def delete_twigo_post(request, twigo_id):
    twigo_post = get_object_or_404(TweetModel, pk=int(twigo_id), user=request.user)
    if request.method == "POST":
        twigo_post.delete()
        return redirect('twigo_home')
    else:
        form = TweetForm(instance=twigo_post)
    return render(request, 'tweet/index.html', {"form": form})

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('twigo_home')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {"form": form})
