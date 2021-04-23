from django.contrib import admin
from .models import User
from .models import Competence
from .models import Vacancy

# Register your models here.

admin.site.register(User)
admin.site.register(Competence)
admin.site.register(Vacancy)


