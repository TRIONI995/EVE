from django.contrib import admin
from .models import Rating, RatingStar, Corporation, Di, Category, Chin


admin.site.register(RatingStar)
admin.site.register(Corporation)
admin.site.register(Di)
admin.site.register(Rating)
admin.site.register(Category)
admin.site.register(Chin)
