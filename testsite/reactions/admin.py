from django.contrib import admin

from .models import ImageReaction, TweetReaction

class ReactionAdmin(admin.ModelAdmin):
    def disable_reaction(modeladmin, request, queryset):
        queryset.update(enabled=False)
    disable_reaction.short_description = "Hide this reaction"

    list_display = ['created_at', 'image', 'enabled']
    ordering = ['created_at']
    actions = [disable_reaction]

    def get_actions(self, request):
        actions = super(ReactionAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions

class ImageReactionAdmin(ReactionAdmin):
    list_display = ['created_at', 'image', 'enabled']

class TweetReactionAdmin(ReactionAdmin):
    list_display = ['created_at', 'text', 'enabled']

admin.site.register(ImageReaction, ImageReactionAdmin)
admin.site.register(TweetReaction, TweetReactionAdmin)
