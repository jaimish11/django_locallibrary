from django.contrib import admin
from catalog.models import Author, Genre, Book, BookInstance, Language


# Register your models here.
class BooksInline(admin.TabularInline):
	model = Book
#admin.site.register(Book)
class BooksInstanceInline(admin.TabularInline):
	model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'display_genre')
	inlines = [BooksInstanceInline]
#admin.site.register(Author)


class AuthorAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
	fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
	inlines = [BooksInline]
	

admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre)
admin.site.register(Language)
#admin.site.register(BookInstance)

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
	"""Administration object for BookInstance models
	Defines:
	- fields to be displayed in list view (list_display)
	- filters that will be displayed in sidebar (list_filter)
	- grouping of fields into sections (fieldsets)
	"""
	list_display = ('book', 'status', 'borrower', 'due_back', 'id')
	list_filter = ('status', 'due_back')
	fieldsets = (
		(None, 
			{
				'fields': ('book', 'imprint', 'id')
			}),
		('Availability', 
			{
				'fields' : ('status', 'due_back', 'borrower')
			}),
	)
	

	
