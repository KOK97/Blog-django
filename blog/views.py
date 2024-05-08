from django.shortcuts import render, redirect, HttpResponse,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, BlogPostForm
from django.views.generic import UpdateView
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def blogs(request):
     # Lấy tất cả bài viết đã xuất bản và sắp xếp theo ngày giảm dần
    posts = BlogPost.objects.filter(status='published').order_by('-dateTime')

    # Số lượng bài viết mỗi trang
    posts_per_page = 3  # Số lượng bài viết bạn muốn hiển thị trên mỗi trang

    paginator = Paginator(posts, posts_per_page)  # Tạo đối tượng paginator

    page_number = request.GET.get('page')  # Lấy số trang từ query parameters
    try:
        paginated_posts = paginator.page(page_number)
    except PageNotAnInteger:
        # Nếu không phải là số, trả về trang đầu tiên
        paginated_posts = paginator.page(1)
    except EmptyPage:
        # Nếu trang không có nội dung, trả về trang cuối cùng
        paginated_posts = paginator.page(paginator.num_pages)

    return render(request, "blog.html", {'posts': paginated_posts})

def blogs_comments(request, slug):
    post = BlogPost.objects.filter(slug=slug).first()
    comments = Comment.objects.filter(blog=post)
    if request.method=="POST":
        user = request.user
        content = request.POST.get('content','')
        blog_id =request.POST.get('blog_id','')
        comment = Comment(user = user, content = content, blog=post)
        comment.save()
    return render(request, "blog_comments.html", {'post':post, 'comments':comments})

def viewDraft(request):
    # posts = BlogPost.objects.all()
    posts = BlogPost.objects.filter(status ='draft')
    return render(request, "draft.html", {'posts_draft':posts})

def push_draft(request,slug):
    post_df = get_object_or_404(BlogPost,slug=slug)
    post_df.status = 'published'
    post_df.save()
    return redirect('/')


def Delete_Blog_Post(request, slug):
    posts = BlogPost.objects.get(slug=slug)
    if request.method == "POST":
        posts.delete()
        return redirect('/')
    return render(request, 'delete_blog_post.html', {'posts':posts})

@login_required(login_url = '/login')
def add_blogs(request):
    if request.method=="POST":
        form = BlogPostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            blogpost = form.save(commit=False)
            blogpost.author = request.user
            blogpost.save()
            obj = form.instance
            alert = True
            return render(request, "draft.html",{'obj':obj, 'alert':alert})
    else:
        form=BlogPostForm()
    return render(request, "add_blogs.html", {'form':form})

class UpdatePostView(UpdateView):
    model = BlogPost
    template_name = 'edit_blog_post.html'
    fields = ['title', 'slug', 'content', 'image']


def user_profile(request, myid):
    post = BlogPost.objects.filter(id=myid)
    return render(request, "user_profile.html", {'post':post})

def Profile(request):
    return render(request, "profile.html")

def edit_profile(request):
    profile = request.user.profile
    if request.method=="POST":
        form = ProfileForm(data=request.POST, files=request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            alert = True
            return render(request, "edit_profile.html", {'alert':alert})
    else:
        form=ProfileForm(instance=profile)
    return render(request, "edit_profile.html", {'form':form})


def Register(request):
    if request.method=="POST":   
        username = request.POST['username']
        email = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('/register')
        
        user = User.objects.create_user(username, email, password1)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return render(request, 'login.html')   
    return render(request, "register.html")

def Login(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect("/")
        else:
            messages.error(request, "Invalid Credentials")
        return render(request, 'blog.html')   
    return render(request, "login.html")

def Logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/login')