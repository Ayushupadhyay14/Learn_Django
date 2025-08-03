from django.shortcuts import render
from myapp.models import Post
from django.core.paginator import Paginator


def post_list(request):
    all_post = Post.objects.all().order_by('id')
    paginator = Paginator(all_post, per_page=3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print("page object", page_obj)  # it reatur a page object :
    print("page number:", page_number)  # it reatur a page object :
    return render(request, 'myapp/index.html', {'all_post': all_post})
