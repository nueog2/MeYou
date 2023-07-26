from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

# Create your views here.
from .models import MainContent,Comment,Cart,CartItem
from .forms import CommentForm
from  hitcount.views import HitCountDetailView

def index(request):
    content_list = MainContent.objects.order_by('-pub_date')
    context = {'content_list':content_list}
    return render(request, 'mysite/content_list.html',context)

def detail(request, content_id):
   content_list = get_object_or_404(MainContent, pk=content_id)
   context = { 'content_list': content_list}
   return render(request, 'mysite/content_detail.html', context)

@login_required(login_url='accounts:login')
def comment_create(request, content_id):
   content_list = get_object_or_404(MainContent, pk=content_id)
   
   if request.method == 'POST':
     form = CommentForm(request.POST)
     if form.is_valid():
        comment = form.save(commit=False)
        comment.content_list = content_list
        comment.author = request.user
        comment.save()
        return redirect('detail', content_id=content_list.id)
     else:
        form = CommentForm()
        context = {'content_list': content_list, 'form': form}
        return render(request, 'mysite/content_detail.html', context)
     

@login_required(login_url='accounts:login')
def comment_update(request, comment_id):
   comment = get_object_or_404(Comment, pk=comment_id)
   
   if request.user != comment.author:
      raise PermissionDenied
   if request.method == 'POST':
      form = CommentForm(request.POST, instance=comment)
      if form.is_valid():
         comment = form.save(commit=False)
         comment.save()
         return redirect('detail', content_id=comment.content_list.id)
   else:
      form = CommentForm(instance=comment)
   context = {'comment': comment, 'form': form}
   return render(request, 'mysite/comment_form.html', context)


@login_required(login_url='accounts:login')
def comment_delete(request, comment_id):
   comment = get_object_or_404(Comment, pk=comment_id)
   
   if request.user != comment.author:
      raise PermissionDenied
   else:
      comment.delete()
   return redirect('detail', content_id=comment.content_list.id)


class MainContentPopularView(HitCountDetailView):
    model = MainContent
    template_name = 'content_list_popular.html'
    count_hit = True
    context_object_name = 'popular_content'

    def get_context_data(self, **kwargs):
      context =  super().get_context_data(**kwargs)

      context['content_list'] = MainContent.objects.all()
      return context
   
   # context['popular_content'] = MainContent.objects.order_by('-hit_count_generic__hits')
@login_required(login_url='accounts:login')
def cart_view(request):
    # 현재 로그인된 사용자의 장바구니에 담긴 상품 목록을 가져옴
    user_cart, created = Cart.objects.get_or_create(user=request.user)
    user_cart = Cart.objects.filter(user=request.user).first()

    if user_cart:
        cart_items = user_cart.cartitem_set.all()  # 장바구니에 담긴 상품들을 가져옴
    else:
        cart_items = []
    
    context = {'cart_items': cart_items}
    return render(request, 'mysite/cart.html', context)

@login_required(login_url='accounts:login')
def add_to_cart(request, content_id):
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))  # 수량을 받아옵니다.
        product = get_object_or_404(MainContent, pk=content_id)  # 상품 정보를 가져옵니다.
        
        # 현재 로그인된 사용자의 장바구니를 가져옴
        user_cart, created = Cart.objects.get_or_create(user=request.user)

        # 장바구니에 해당 상품과 수량을 추가함
        cart_item, created = CartItem.objects.get_or_create(cart=user_cart, product=product)
        cart_item.quantity += quantity
        cart_item.save()

        
    return redirect('cart')  # 장바구니 페이지로 리디렉션합니다.