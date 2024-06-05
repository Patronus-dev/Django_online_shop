from django.contrib import admin
from .models import Product, Comment


# <--------------- This will show each comment under its own product --------------->
class CommentsInline(admin.TabularInline):  # or (admin.StackedInline):
    model = Comment
    fields = ['author', 'body', 'stars', 'active', ]
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'active',)

    # <------- This part is for connect to CommentsInline ------->
    inlines = [
        CommentsInline,
    ]


# <--------------- This will show comments in separately section --------------->
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('product', 'author', 'body', 'stars', 'active', )
