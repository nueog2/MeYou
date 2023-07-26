from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation


class MainContent(models.Model, HitCountMixin):
    title = models.CharField(max_length=200)
    content = models.TextField()
    photo = models.ImageField(blank=True, null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.title

    # def __str__(self):
    #     return f'{self.price}₩'

    pub_date = models.DateTimeField('date published')
    hit_count_generic = GenericRelation(

        HitCount, object_id_field = 'object_pk',
        related_query_name = 'hit_count_generic_relation'
    )

class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content_list = models.ForeignKey(MainContent, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    modify_date = models.DateTimeField(auto_now=True)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(MainContent, through='CartItem')
    created_at = models.DateTimeField(auto_now_add=True)

   

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(MainContent, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.title}"
    
    def get_total_items(self):
        total_items = self.cartitem_set.aggregate(total_items=models.Sum('quantity'))
        return total_items['total_items'] or 0


