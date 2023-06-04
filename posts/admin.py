from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.TabularInline):
    model = Comment

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(post=self.instance)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'text', 'created_date', 'image']
    inlines = [CommentInline]
