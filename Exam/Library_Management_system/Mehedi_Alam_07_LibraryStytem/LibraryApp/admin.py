from django.contrib import admin
from LibraryApp.models import *

# Register your models here.
admin.site.register(CustomUserModel)
admin.site.register(BookModel)
admin.site.register(StudentProfileModel)
admin.site.register(LibrarianProfileModel)