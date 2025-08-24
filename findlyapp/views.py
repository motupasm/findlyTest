from django.shortcuts import render, redirect
from .models import returnItemModel
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .utils.cloudinary_utils import upload_to_cloudinary

# Create your views here.


def home(request):
    return render(request, "homepage.html")


def searchItem(request):
    if request.method == "POST":
        searched = request.get("searched")
        searched = returnItemModel.objects.filter(item_type__icontains=searched)
        return render(request, "returnitem", {"searched": searched})


@login_required(login_url="signin")
def returnItemviews(request):
    if request.method == "POST":
        item_type = request.POST.get("item_type")
        item_description = request.POST.get("item_description")
        location_found = request.POST.get("location_found")
        date_found = request.POST.get("date_found")
        item_image = request.FILES.get("item_image")

        
        if not item_image:
            messages.error(request, "Please upload an image.")
            return redirect("returnitem")

        try:
            image_url = upload_to_cloudinary(item_image)
        except Exception as e:
            messages.error(request, f"Image upload failed: {e}")
            return redirect("returnitem")

        returnItemInput = returnItemModel(
            item_type=item_type,
            item_description=item_description,
            location_found=location_found,
            date_found=date_found,
            item_image=image_url,  # Save URL returned by Cloudinary
        )
        returnItemInput.save()
        messages.success(request, "Thank You for Returning the Lost Item")
        return redirect("returnitem")
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
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("returnitem")
        else:
            print("is not working")
            messages.error(request, "Invalid username or password")
            return redirect("signin")

    return render(request, "signin.html")


def singupItemviews(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        input_has_error = False

        if User.objects.filter(email=email).exists():
            input_has_error = True
            messages.error(
                request, f"Email ({email}) already exist , please try another email!"
            )
            return redirect("signup")

        if User.objects.filter(username=username).exists():
            input_has_error = True
            messages.error(
                request,
                f"Username ({username}) already exist , please try another username!",
            )
            return redirect("signup")

        if len(password) < 6:
            input_has_error = True
            messages.error(request, f"Password must at least have 6 characters")
            return redirect("signup")

        # if confirm_password != password:
        #     messages.error(request, f"Passwords does not match!")

        input_has_error = False

        new_user = User.objects.create_user(
            first_name=first_name, email=email, username=username, password=password
        )
        new_user.save()
        messages.success(
            request, "Success! Your account has been created. You can now log in."
        )
        send_mail(
            "Welcome to Findly!",
            f"Hi {first_name},\nWelcome to Findly! Your account is ready to go.\n\nWe’re glad to have you on board!",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=True,
        )
        return redirect("signup")
    return render(request, "signup.html")


def logoutviews(request):
    logout(request)

    return redirect("signin")


def contact(request):
    if request.method == "POST":
        print("form submitted")
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        message = request.POST.get("message")

        email_messageC = "Thank you for reaching out! We've received your message and will get back to you as soon as possible."
        email_messageD = (
            f"Name : {name} \nPhone : {phone} \nMessage : {message}\nEmail: {email}"
        )

        try:
            send_mail(
                "Findly Support: We've Got Your Message",
                email_messageC,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=True,
            )
            send_mail(
                "New Message Received via Findly Contact Form",
                email_messageD,
                email,
                [settings.EMAIL_HOST_USER],
                fail_silently=True,
            )
            messages.success(request, "Message was sent!")
            return redirect("contact")
        except request.method != "POST":
            messages.success(request, "Message was not sent!")
            print("form was not submited")
            return redirect(contact)

    return render(request, "contact.html")
