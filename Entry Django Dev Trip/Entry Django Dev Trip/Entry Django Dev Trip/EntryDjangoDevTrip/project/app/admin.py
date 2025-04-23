from django.contrib import admin
from .models import Watch, Author


from django.contrib import admin
from .models import Author, Watch, WatchImage

class WatchImageInline(admin.TabularInline):
    model = WatchImage
    extra = 3

@admin.register(Watch)
class WatchAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'price', 'author')
    list_filter = ('brand', 'gender', 'material', 'author')
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {'fields': ('title', 'brand', 'price')}),
        ('Медиа', {'fields': ('image', 'video')}),
    )
    inlines = [WatchImageInline]

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(WatchImage)