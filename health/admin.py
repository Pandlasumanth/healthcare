from django.contrib import admin
from .models import patients
from .models import diseases
from .models import genric_medicines
from .models import nongenric_medicines
from .models import patients_register
from .models import Prescription
from .models import doctor
from .models import Report



# Register your models here.
admin.site.register(patients)
admin.site.register(diseases)
admin.site.register(genric_medicines)
admin.site.register(nongenric_medicines)
admin.site.register(patients_register)
admin.site.register(Prescription)
admin.site.register(doctor)
admin.site.register(Report)