from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render, get_object_or_404

from .models import TweetModel
from .forms import TweetForm

# Create your views here.
def index_home(request):
    return render(request, 'tweet/index.html')

def twigos_home(request):
    twigos = TweetModel.objects.all().order_by('-created_at')
    return render(request, 'tweet/index.html', {"twigos": twigos})

def create_twigo(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('twigos_home')
    else:
        form = TweetForm()
    return render(request, 'index.html', {"form": form})

def update_twigo_post(request, twigo_id):
    twigo_post = get_object_or_404(TweetModel, pk=twigo_id, user=request.user)
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES, instance=twigo_post)
        if form.is_valid():
            twigo_post = form.save(commit=False)
            twigo_post.user = request.user
            twigo_post.save()
            return redirect('twigos_home')
    else:
        form = TweetForm(instance=twigo_post)
    return render(request, 'tweet/index.html', {"form": form})

def delete_twigo_post(request, twigo_id):
    twigo_post = get_object_or_404(TweetModel, pk=twigo_id, user=request.user)
    if request.method == "POST":
        twigo_post.delete()
        return redirect('twigos_home')
    else:
        form = TweetForm(instance=twigo_post)
    return render(request, 'tweet/delete_confirm_page.html', {"form": form})
