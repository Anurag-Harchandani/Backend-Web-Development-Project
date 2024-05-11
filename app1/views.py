from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    dish1 = dishes()
    dish1.dishnames = "Dal Makhani"
    dish1.dishprice = 299
    dish1.img = "dal.jpg"

    dish2 = dishes()
    dish1.dishnames = "Pizza"
    dish1.dishprice = 399
    dish1.img = "pizza.jpg"

    dish3 = dishes()
    dish1.dishnames = "Pasta"
    dish1.dishprice = 349
    dish1.img = "pasta.jpg"

    dishess = [dish1, dish2, dish3]
    try:
        if request.method == "POST":
            data=request.POST
            Dish=data.get("dishname1")
            Price=data.get("price1")
            Quantity=data.get("quantity1")

            Cart.objects.create(
                Dish=Dish,
                Price=Price,
                Quantity=Quantity
            )
    except:
        try:
            if request.method == "POST":
                data=request.POST
                Dish=data.get("dishname2")
                Price=data.get("price2")
                Quantity=data.get("quantity2")

                Cart.objects.create(
                    Dish=Dish,
                    Price=Price,
                    Quantity=Quantity
                )
        except:
            try:
                if request.method == "POST":
                    data=request.POST
                    Dish=data.get("dishname3")
                    Price=data.get("price3")
                    Quantity=data.get("quantity3")

                    Cart.objects.create(
                        Dish=Dish,
                        Price=Price,
                        Quantity=Quantity
                    )
            except:
                if request.method == "POST":
                    data=request.POST
                    Dish=data.get("dishname4")
                    Price=data.get("price4")
                    Quantity=data.get("quantity4")
                    Cart.objects.create(
                        Dish=Dish,
                        Price=Price,
                        Quantity=Quantity
                    )
                

    finally:
        return render(request, 'home.html',{'dishess':dishess})

def cart(request):
    queryset= Cart.objects.all().values()
    vari=list(queryset[len(queryset)-1].values())
    entry=vari[1:]
    
    return render(request, 'cart.html',{'cart':entry,'total':(int(entry[1])*int(entry[2]))})

def bill(request):
    name = request.POST['name1']
    phono = request.POST['num']
    email = request.POST['email']
    address = request.POST['address']
    if request.method == "POST":
        data=request.POST

        Name=data.get("name1")
        Phone_Number=data.get("num")
        Email=data.get("email")
        Address=data.get("address")

        Order.objects.create(
            Name=Name,
            Phone_Number= Phone_Number,
            Email=Email,
            Address=Address
        )

    queryset= Cart.objects.all().values()
    var=list(queryset[len(queryset)-1].values())
    entry=var[1:]


    return render(request,'bill.html',{'name':name,'phono':phono,'email':email,'address':address,'cart':entry,'total':(int(entry[1])*int(entry[2]))})

