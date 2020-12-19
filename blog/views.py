from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def post_list(request):
    #페이지 받아오기
    page=request.GET.get('page','1')#page의 값을 get방식으로 가져오는데 없을시 디폴트를 '1'로 지정한다.

    #조회
    #posts = Post.objects.order_by('-created_date')
    posts = Post.objects.all()

    #페이징처리
    paginator=Paginator(posts, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:#페이지 번호가 없을시
        posts = paginator.page(1)#첫번째페이지 보여줌
    except EmptyPage:#페이지가 비어있을시(페이지 번호 초과시)
        posts = paginator.page(paginator.num_pages)#마지막페이지 보여줌

    #해당 페이지를 index
    index = posts.number

    #마지막 페이지
    max_index = len(paginator.page_range)

    #하단에 보여줄 페이지 범위크기
    page_size=3

    #해당 페이지에서 앞으로 두칸 2보다 작으면 1
    start_index = index - page_size if index > page_size else 1

    #해당 페이지에서 뒤로 두칸
    if index + page_size == max_index:#총 페이지가 3칸 이하일때
        end_index=max_index
    else:#현재 페이지 +2 Max보다 크면 Max로 설정
        end_index = index + page_size if index <= max_index else max_index

    #범위 생성
    # 1' Max
    # 1 Max'
    # 1' 2 3 ... Max
    # 1 2' 3 4 ... Max
    # 1 2 3' 4 5 ... Max
    # 1 ... 2 3 4' 5 6 ... Max
    # 1 ... Max-2 Max-1 Max'
    # 1 ... Max-3 Max-2 Max-1' Max

    #리스트는 0부터 시작함
    page_range = list(paginator.page_range[start_index-1:end_index])

    return render(request, 'blog/post_list.html', {'posts': posts, "page_range":page_range, 'max_index': max_index,'page_size':page_size})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})





def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
