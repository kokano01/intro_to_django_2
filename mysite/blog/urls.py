from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'blog-index'),
    path('about/',  views.aboutPage, name = 'blog-about'),
    path('posts/',  views.posts, name = 'blog-posts'),
    path('posts/create',  views.createPost, name = 'blog-createpost'),
    path('register/',  views.registerPage, name = 'blog-register'),
    path('login/',  views.loginPage, name = 'blog-login'),
    path('logout/',  views.logoutUser, name = 'blog-logout'),
    path('posts/<int:post_id>',  views.individualPost, name = 'blog-individualpost'),
    path('posts/update/<int:post_id>',  views.updatePost, name = 'blog-updatepost'),
    path('posts/delete/<int:post_id>',  views.deletePost, name = 'blog-deletepost'),
    
]