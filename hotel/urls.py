#-------------------  Hotel Urls.py.................
from django.urls import path
from . import views
urlpatterns = [
    path("",views.index,name = "HBSHome"),
    path("about/",views.about,name = "AboutUs"),
    path("booking/<int:myid>",views.bookings,name = "BookingDetails"),
    path("Order/",views.order,name = "Order"),
    path("search/",views.search,name = "search"),
    path("hotelview/<int:myid>",views.hotelview,name = "HotelView"),
    path("Tracker/",views.tracker,name = "Tracker"),
    path("Contact/",views.contact,name = "Contact"),
]