from django.shortcuts import render
from django.views import View


class MainView(View):
    def get(self, request, *args, **kwargs):
        title = 'My Blog - Главная'
        message = ''
        context = {
            'title': title,
            "message": message
        }
        return render(request,'blog/index.html', context=context)



class PostDetail(View):
    def get(self, request, *args, **kwargs):
        title = 'My Blog - Пост'
        message = ''
        context = {
            'title': title,
            "message": message
        }
        return render(request, 'blog/post.html', context=context)


class ContactForm(View):
    def get(self, request, *args, **kwargs):
        title = 'My Blog - Сообщение'
        message = ''
        context = {
            'title': title,
            "message": message
        }
        return render(request, 'blog/contact.html', context=context)



def index(request):
    title = 'Главная'
    message = ''
    context = {
        'title': title,
        "message": message
        }
    return render(request, 'blog/index.html', context=context)
