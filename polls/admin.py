from django.contrib import admin
from polls.models import Poll, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class PollAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question']
    #Adding a filter by pub_date
    list_filter = ['pub_date']
    
    #List of items to be displayed
    list_display = ('question', 'pub_date', 'was_published_recently')
    
    #Adding a search field
    search_fields = ['question']
    
    #Adding a breadcrumb for date hierarchy
    date_hierarchy = 'pub_date'
    
    fieldsets = [
        (None,                  {'fields' : ['question']}),
        ('Date information',    {'fields' : ['pub_date']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)

#admin.site.register(Choice)