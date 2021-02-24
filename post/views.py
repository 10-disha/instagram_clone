from django.shortcuts import render
from post.models import Post, Stream
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def index(request):
    user = request.user
    posts = Stream.objects.filter(user=user)

    group_id = []

    for post in posts:
        group_id.append(post.post_id)

    post_item = Post.objects.filter(id__in=group_id).all().order_by('-posted')
    template = loader.get_template('index.html')
    context = {
        'post_item':post_item,
    }
    return HttpResponse(template.render(context, request))