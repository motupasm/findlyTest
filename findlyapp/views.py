from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import returnItemModel
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def home(request):
    return render(request, "homepage.html")


def searchItem(request):
    if request.method == "POST":
        searched = request.get("searched")
        searched = returnItemModel.objects.filter(item_type__icontains=searched)
        return render(request, "returnitem", {"searched": searched})


def returnItemviews(request):
    if request.method == "POST":
        item_type = request.POST.get("item_type")
        item_description = request.POST.get("item_description")
        location_found = request.POST.get("location_found")
        date_found = request.POST.get("date_found")
        item_image = request.FILES.get("item_image")

        returnItemInput = returnItemModel(
            item_type=item_type,
            item_description=item_description,
            location_found=location_found,
            date_found=date_found,
            item_image=item_image,
        )
        returnItemInput.save()
        messages.success(request, "Thank You for Returning the Lost Item")
        return redirect("returnitem")
    else:
        return render(request, "returnitem.html")


def foundItemviews(request):
    allReportedItems = returnItemModel.objects.all()
    context = {"allReportedItems": allReportedItems}
    return render(request, "founditems.html", context)


def search(request):
    if request.method == "POST":
        search = request.POST.get("search")
        qr = returnItemModel.objects.filter(item_type__icontains=search)
        return render(request, "search.html", {"searched": qr})
    else:
        return render(request, "founditems.html", {})


def singinItemviews(request):
    return render(request, "signup.html")


def singupItemviews(request):
    return render(request, "signup.html")
