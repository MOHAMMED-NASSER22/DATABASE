from django.contrib import admin
from .models import Admins,Manger ,Hospital ,Department ,Doctor ,Nurse ,DoctorHasHospital ,Receptinist ,Pathient ,PathientHasHospital ,Rooms ,Bed ,Report


admin.site.register(Admins)
admin.site.register(Manger)
admin.site.register(Hospital)
admin.site.register(Department)
admin.site.register(Doctor)
admin.site.register(DoctorHasHospital)
admin.site.register(Nurse)
admin.site.register(Receptinist)
admin.site.register(Pathient)
admin.site.register(PathientHasHospital)
admin.site.register(Rooms)
admin.site.register(Bed)
admin.site.register(Report)




# Register your models here.
