from django.contrib import admin

from root.models import UseCase, Feature, FAQ, Author, Weblog


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
class WeAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')