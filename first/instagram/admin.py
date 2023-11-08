from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Post
from .models import Comment
from .models import Tag
from .models import Profile

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display=['photo_tag','id','title','desc_length','created_at','updated_at', 'is_public']
    list_display_links=['title']
    search_fields=['title']
    list_filter=['created_at','is_public']

    def photo_tag(self,post):
        if post.image:
            return mark_safe(f'<img src="{post.image.url}" style="width:72px;"/>')
        return None

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


#admin.site.register(Post)
#admin.site.register(Comment)
#admin.site.register(Tag)
#admin.site.register(Profile)