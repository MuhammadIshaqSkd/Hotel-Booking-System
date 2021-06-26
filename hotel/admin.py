from django.contrib import admin

# Register your models here.
from .models import Hotel,Contact,Booking,BookingUpdate

admin.site.register(Hotel)
admin.site.register(Contact)
admin.site.register(Booking)
admin.site.register(BookingUpdate)
