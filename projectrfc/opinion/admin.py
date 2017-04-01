from django.contrib import admin
from opinion.models import Speaker, Mention, Sentence, Comment, Crowd

class SpeakerAdmin(admin.ModelAdmin):
    list_display = ("name", "profile")

class MentionAdmin(admin.ModelAdmin):
    list_display = ("hash_id", "date_time")

class SentenceAdmin(admin.ModelAdmin):
    list_display = ("id", "hash_id", "text", "fact")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("hash_id", "crowd_id", "uid", \
            "text", "vote_up", "vote_down", "assert_kind")

class CrowdAdmin(admin.ModelAdmin):
    list_display = ("crowd_id", "name", "score")

admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Mention, MentionAdmin)
admin.site.register(Sentence, SentenceAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Crowd, CrowdAdmin)
