from django.contrib import admin

from root.models import UseCase, Feature, FAQ, Author, Weblog, ContactMessage, Release


@admin.register(UseCase)
class UseCaseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'order', 'active')
    list_filter = ('active',)
    search_fields = ('question', 'answer')
    ordering = ('order',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user',)


@admin.register(Weblog)
class WeblogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name', 'email', 'message')
    readonly_fields = ('name', 'email', 'phone', 'website', 'message', 'created_at')


@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
    list_display = ('version',)