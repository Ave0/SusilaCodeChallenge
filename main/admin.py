from django.contrib import admin
from .models import *
# Register your models here.


# class CombinacionesBombaMotorInLine(admin.StackedInline):
#     model = CombinacionesBombaMotor
# 
# class PuntosGastoMetrosInLine(admin.StackedInline):
#     model = PuntosGastoMetros
# 
# class NPSHRBombaInline(admin.StackedInline):
#     model = NPSHRBomba    
# 
# 
# class BombasAdmin(admin.ModelAdmin):
#     inlines=[
#              CombinacionesBombaMotorInLine,
#              PuntosGastoMetrosInLine,
#              NPSHRBombaInline,
#              ]

admin.site.register( Author)
admin.site.register(Book)
admin.site.register(Subscriber)
admin.site.register(Subscription)

