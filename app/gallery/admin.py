from django.contrib import admin

from .models import Albums
from .models import Question
from .models import Photos
from .models import Author

admin.site.register(Question)
admin.site.register(Albums)
admin.site.register(Photos)
admin.site.register(Author)
# admin.site.register(AlbumAdmin)
# admin.site.register(Tag, TagAdmin)
# admin.site.register(Photo, PhotoAdmin)

# Register your models here.
# class AlbumAdmin(admin.ModelAdmin):
#     search_fields = ["title"]
#     list_display = ["title"]

# class TagAdmin(admin.ModelAdmin):
#     list_display = ["tag"]

# class PhotoAdmin(admin.ModelAdmin):
#     search_fields = ["title"]
#     list_display = ["title", "user", "created"]
#     list_filter = ["tags", "albums"]