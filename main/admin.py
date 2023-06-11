from django.contrib import admin
from .models import Test, ScoreIQ, ScoreEQ
# Register your models here.


admin.site.register(Test)
admin.site.register(ScoreEQ)
admin.site.register(ScoreIQ)