from django.contrib import admin
from quiz.models import Question, Category

class postAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    # fields = ('status',)
    #exclude = ['counted_views']
    list_display = ('category','created_date','content')
    list_filter = ('category',)
    #ordering = ['created_date']
    search_fields = ['category','content']

admin.site.register(Question,postAdmin)
admin.site.register(Category)