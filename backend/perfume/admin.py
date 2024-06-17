from django.contrib import admin
from perfume.models import Perfume, Aroma, Vendor, PerfumeAroma, PerfumeVendor


admin.site.register(Perfume)
admin.site.register(Aroma)
admin.site.register(Vendor)
admin.site.register(PerfumeAroma)
admin.site.register(PerfumeVendor)
