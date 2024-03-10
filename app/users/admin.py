from django.contrib import admin

from .models import UserReadingList, UserReview


class ReadingListAdmin(admin.ModelAdmin):
    pass


class ReviewAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserReadingList, ReadingListAdmin)
admin.site.register(UserReview, ReviewAdmin)
