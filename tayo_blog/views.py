from django.shortcuts import render

posts = [
    {
        'author': 'Tella adetayo',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 15 2021'
    },
    {
        'author': 'Tella adetayo',
        'title': 'Blog Post 2',
        'content': 'second post content',
        'date_posted': 'April 15 2021'
    }

]  

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'tayo_blog/home.html', context)

def about(request):
    return render(request, 'tayo_blog/about.html', {'title': about})

