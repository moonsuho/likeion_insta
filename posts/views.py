from django.shortcuts import render,redirect,get
from django.http import HttpResponse,JsonResponse
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required

from .models import Post
# Create your views here.

def index(request):
    post_list = Post.objects.all().order_by('-created_at')
    context={
        'post_list':post_list,
    }
    return render(request,'index.html')

def post_list_view(request):
    #post_list = Post.objects.all()
    post_list = Post.objects.filter(writer=request.user)
    #post_list=None
    context={
        'post_list':post_list,
    }
    return render(request,'posts/post_list.html')

def post_detail_view(request,id):
    try:
        post=Post.objects.get(id=id)
    except Post.DoesNotExist:
        return redirect('index')

    context={
        'post':post,
    }
    return render(request,'posts/post_detail.html')

@login_required
def post_create_view(request):
    if(request.method == 'GET'):
        return render(request,'posts/post_form.html')
    else:
        image=request.FILES.get('image')
        content=request.POST.get('content')
        print(image)
        print(content)
        Post.objects.create(
            image=image,
            content=content,
            writer=request.user
        )
        return redirect('index')
    
def post_update_view(request,id):
    post = Post.objects.get(id=id)
    #post = get_object_or_404(Post,id=id)

    if request.method == 'GET':
        context = {
            'post': post
        }
        return render(request, 'posts/post_form.html', context)
    else:
        new_image = request.FILES.get('image')
        content = request.POST.get('content')

        if new_image:
            post.image.delete()
            post.image = new_image

        post.content = content
        post.save()
        return redirect('posts:post-detail', post.id)
    
@login_required
def post_delete_view(request,id):
    post=get_object_or_404(Post,id=id)
    if request.user !=post.writer:
        return Http404('잘못된 접근입니다')
    if request.method=='GET':
        context={'post':post}
        return render(request,'posts/post_confirm_delete.html')
    else:
        post.delete()
        return redirect('index')
    
    
def url_view(request):
    print('url_view()')
    data={'code':'001','msg':'OK'}
    #return HttpResponse('<h1>url_view</h1>')
    return JsonResponse(data)

def url_parameter_view(request,username):
    print('url_parameter_view()')
    print(f'username:{username}')
    print(f'request.GET:{request.GET}')
    return HttpResponse(username)

def  function_view(request):
    print(f'request.method:{request.method}')
    if request.method=='GET':
        print(f'request.GET:{request.GET}')
    elif request.method=='POST':
        print(f'request.POST:{request.POST}')
    return render(request,'view.html')

class class_view(ListView):
    model=Post
    template_name='cbv_view.html'
    ordering=['-id']
