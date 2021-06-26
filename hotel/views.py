from django.shortcuts import render
from django.http import HttpResponse
from .models import Hotel,Contact,Booking,BookingUpdate
from math import ceil
import json
#-------------------  Hotel Views.py.................



# Create your views here.

def index(request):
    allProds = []
    catprods = Hotel.objects.values('city', 'id')
    cats = {item['city'] for item in catprods}
    for cat in cats:
        prod = Hotel.objects.filter(city=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'hotel/index.html', params)


def about(request):
    return render(request,'hotel/about.html')

def bookings(request ,myid):
    #Fetch the product using the id
    product = Hotel.objects.filter(id=myid)
    return render(request, 'hotel/checkout.html', {'product': product[0]})

def order(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        amount = request.POST.get('amount', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        hname = request.POST.get('hname', '')
        room = request.POST.get('room', '')
        noroom = request.POST.get('noroom', '')
        booking = Booking(items_json=items_json, name=name, email=email, phone=phone, hotel_name=hname,room_type=room,No_room=noroom)
        booking.save()
        update = BookingUpdate(order_id=booking.order_id, update_desc="Your Booking has been placed")
        update.save()
        thank = True
        id = booking.order_id
        return render(request, 'hotel/checkout.html', {'thank':thank, 'id': id})
    return render(request, 'hotel/checkout.html')


def hotelview(request,myid):
    # Fetch the product using the id
    product = Hotel.objects.filter(id=myid)
    return render(request, 'hotel/hotelview.html', {'product': product[0]})


def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Booking.objects.filter(order_id=orderId, email=email)
            if len(order) > 0:
                update = BookingUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc,'time': item.timestamp})
                    response = json.dumps({"status": "success", "updates": updates, "itemsJson": order[0].items_json},
                                          default=str)

                return HttpResponse(response)
            else:
                return HttpResponse('{"status": "noitem"}')
        except Exception as e:
            return HttpResponse('{"status": "error"}')
    return render(request, 'hotel/tracker.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contact = Contact(name = name,email=email,phone = phone,desc = desc)
        contact.save()
    return render(request,'hotel/contact.html')

def searchMatch(query, item):
    if query in item.hotel_name or query in item.city:
        return True
    else:
        return False


def search(request):
    query= request.GET.get('search')
    allProds = []
    catprods = Hotel.objects.values('city', 'id')
    cats = {item['city'] for item in catprods}
    for cat in cats:
        prodtemp = Hotel.objects.filter(city=cat)
        prod=[item for item in prodtemp if searchMatch(query, item)]
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        if len(prod)!= 0:
            allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds, "msg":""}
    if len(allProds)==0 or len(query)<4:
        params={'msg': "Sorry Can not Find That Hotel"}
    return render(request, 'hotel/search.html', params)