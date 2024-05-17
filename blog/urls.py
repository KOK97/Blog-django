from django.urls import path
from . import views
from .views import UpdatePostView

appName = 'blog'

urlpatterns = [
#     blogs
    path("", views.blogs, name="blogs"),
    path("comments/<str:slug>/", views.blogs_comments, name="blogs_comments"),
    path("blog/<str:slug>/", views.blogs_comments, name="blog"),
    path("draft/", views.viewDraft, name="draft"),
    path("add_blogs/", views.add_blogs, name="add_blogs"),
    path("edit_blog_post/<str:slug>/", UpdatePostView.as_view(), name="edit_blog_post"),
    path("draft/delete_blog_post/<str:slug>/", views.Delete_Blog_Post, name="delete_blog_post"),
    path("push_draft/<str:slug>/", views.push_draft, name="push_draft"),
    path('search/', views.search_blogs, name='search_blogs'),

    
#     profile
    path("profile/", views.Profile, name="profile"),
    path("edit_profile/", views.edit_profile, name="edit_profile"),
    path("user_profile/<int:myid>/", views.user_profile, name="user_profile"),
    
#    user authentication
    path("register/", views.Register, name="register"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
]