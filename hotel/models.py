from django.db import models

# Create your models here.

class Hotel(models.Model):
    hotel_id = models.AutoField
    hotel_name=models.CharField(max_length=50)
    city= models.CharField(max_length=50, default="")
    address= models.CharField(max_length=50, default="")
    vprp=models.IntegerField(default=0)
    grp= models.IntegerField(default=0)
    desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image= models.ImageField(upload_to="hotel/images",default="")
    vpr_img= models.ImageField(upload_to="hotel/images",default="")
    gr_img= models.ImageField(upload_to="hotel/images",default="")

    def __str__(self):
        return self.hotel_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name

class Booking(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")
    hotel_name = models.CharField(max_length=90)
    room_type = models.CharField(max_length=90)
    No_room = models.CharField(max_length=111, default="")

    def __str__(self):
        return self.hotel_name

class BookingUpdate(models.Model):
    update_id= models.AutoField(primary_key=True)
    order_id= models.IntegerField(default="")
    update_desc= models.CharField(max_length=5000)
    timestamp= models.DateField(auto_now_add= True)

    def __str__(self):
        return self.update_desc[0:7] + "..."