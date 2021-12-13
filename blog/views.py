from django.shortcuts import render, redirect
from .models import Article, Shop
from .forms import ArticleForm
from django.views.generic import DetailView, UpdateView, DeleteView


def blog_home(request):
    blog_info = Article.objects.order_by('title')
    return render(request, 'blog/blog_home.html', {'blog_info': blog_info})

def shops(request):
    shop_info = Shop.objects.order_by('shop_name')
    return render(request, 'blog/shops.html', {'shop_info': shop_info})


class BlogDetailView(DetailView):
    model = Article
    template_name = 'blog/detail_view.html'
    context_object_name = 'article'


class BlogUpdateView(UpdateView):
    model = Article
    template_name = 'blog/create.html'

    form_class = ArticleForm


class BlogDeleteView(DeleteView):
    model = Article
    success_url = '/blog/'
    template_name = 'blog/blog-delete.html'


def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'


    form = ArticleForm()

    data ={
        'form': form,
        'error': error
    }

    return render(request, 'blog/create.html', data)




