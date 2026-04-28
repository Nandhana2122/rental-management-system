from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
import random
from django.contrib import messages
from .google_sheets import save_to_sheet  # ✅ import from your google_sheets.py

from django.utils import timezone

from datetime import timedelta
from django.contrib.auth.decorators import login_required









# In-memory OTP storage (you can use session or DB)
signup_otps = {}

# Home page
def home(request):
    return render(request, 'vacation-rental-master/home.html')


def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')

        otp = str(random.randint(100000, 999999))

        # ✅ SAVE EVERYTHING
        request.session["signup_otp"] = otp
        request.session["otp_username"] = username
        request.session["otp_email"] = email
        request.session["otp_password"] = password
        request.session["otp_mobile"] = mobile
        request.session["otp_time"] = timezone.now().isoformat()

        print("SIGNUP SESSION DATA:", dict(request.session))  # DEBUG

        send_mail(
            'Your Signup OTP',
            f'Hello {username}, your OTP is {otp}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        return redirect("verify_otp")

    return render(request, 'vacation-rental-master/signup.html')


def send_signup_otp(request):
     if request.method == "POST":
        email = request.POST.get("email")

        otp = random.randint(100000, 999999)

        request.session["signup_otp"] = str(otp)
        request.session["otp_time"] = timezone.now().isoformat()

        send_mail(
            "Your Signup OTP",
            f"Your OTP is {otp}. It is valid for 5 minutes.",
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False,
        )

        return redirect("verify_otp")

     return render(request, "vacation-rental-master/signup.html")





def verify_otp(request):
    if request.method == "POST":
        entered_otp = request.POST.get("otp")
        saved_otp = request.session.get("signup_otp")
        otp_time = request.session.get("otp_time")

        print("VERIFY SESSION DATA:", dict(request.session))  # DEBUG

        if not saved_otp or not otp_time:
            messages.error(request, "Invalid or expired OTP.")
            return redirect("verify_otp")

        otp_time = timezone.datetime.fromisoformat(otp_time)

        if timezone.now() > otp_time + timedelta(minutes=5):
            messages.error(request, "OTP expired.")
            return redirect("verify_otp")

        if str(entered_otp) == str(saved_otp):
            username = request.session.get("otp_username")
            email = request.session.get("otp_email")
            password = request.session.get("otp_password")

            if not username or not email or not password:
                messages.error(request, "Signup data is missing.")
                return redirect("verify_otp")

            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )

            request.session.flush()
            messages.success(request, "OTP verified successfully.")
            return redirect("login")

        else:
            messages.error(request, "Invalid OTP.")
            return redirect("verify_otp")

    return render(request, "vacation-rental-master/verify-otp.html")


# users/views.py
# Temporary OTP storage



# Logout
def logout_view(request):
    logout(request)
    return redirect('login')


# Google login (allauth will handle actual login)
def google_login(request):
    return redirect('/accounts/google/login/')

# GitHub login
def github_login(request):
    return redirect('/accounts/github/login/')

from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("index")   # ✅ GO TO INDEX
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "vacation-rental-master/login.html")


from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    return render(request, "vacation-rental-master/index.html")




def home(request):
    return render(request, 'vacation-rental-master/home.html')

def about(request):
    return render(request, 'vacation-rental-master/about.html')

def departments(request):
    return render(request, 'vacation-rental-master/departments.html')

def services(request):
    return render(request, 'vacation-rental-master/services.html')

def rooms(request):
    return render(request, 'vacation-rental-master/rooms.html')

def blog(request):
    return render(request, 'vacation-rental-master/blog.html')

def contact(request):
    return render(request, 'vacation-rental-master/contact.html')




# views.py
# users/views.py
# users/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .google_sheets import save_to_sheet  # ✅ import from your google_sheets.py

def contact_view(request):
    if request.method == "POST":
        print("POST DATA:", request.POST)  # debug

        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        print("Form Data:", name, email, subject, message)

        try:
            save_to_sheet([name, email, subject, message])
            messages.success(request, "Your message was sent successfully ✅")
            return redirect("contact")
        except Exception as e:
            print("Google Sheet Error:", e)
            messages.error(request, "Something went wrong ❌")
            return redirect("contact")

    return render(request, "vacation-rental-master/contact.html")



def contact_success(request):
    return render(request, "vacation-rental-master/contact_success.html")



import pywhatkit
import threading
import time
from django.shortcuts import render, redirect


def send_whatsapp(phone, message):
    try:
        import pywhatkit
        import time

        print("📤 Starting WhatsApp:", phone)
        time.sleep(3)

        pywhatkit.sendwhatmsg_instantly(
            phone_no=phone,
            message=message,
            wait_time=25,
            tab_close=False
        )

        print("✅ WhatsApp done")

    except Exception as e:
        print("❌ WhatsApp Error:", e)



def login_view(request):
    if request.method == 'POST':
        phone = request.POST.get('mobile') or request.POST.get('phone')
        print("📞 Phone:", phone)

        if phone:
            if not phone.startswith("+"):
                phone = "+91" + phone

            message = "Welcome to RentEase 🎉 You logged in successfully ✅"

            t = threading.Thread(target=send_whatsapp, args=(phone, message))
            t.start()

            # let browser start
            time.sleep(1)

        return redirect('index')


    return render(request, 'vacation-rental-master/login.html')


import os
from django.conf import settings

print(os.listdir(settings.TEMPLATES[0]['DIRS'][0]))

def index(request):
    success_msg = request.GET.get("success")
    return render(request, "vacation-rental-master/index.html", {"success_msg": success_msg})

def rooms(request):
    return render(request, 'vacation-rental-master/rooms.html')

def categories(request):
    return render(request, 'vacation-rental-master/categories.html')







from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ChatMessage, CustomerProfile

@login_required
def profile_view(request):
    # Get or create profile for current user
    profile, created = CustomerProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        # Update user info
        user = request.user
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")
        user.save()

        # Update profile info
        profile.phone = request.POST.get("phone")
        profile.address = request.POST.get("address")
        profile.city = request.POST.get("city")
        profile.state = request.POST.get("state")
        profile.pincode = request.POST.get("pincode")
        profile.occupation = request.POST.get("occupation")
        profile.family_size = request.POST.get("family_size")
        profile.purpose = request.POST.get("purpose")
        profile.budget = request.POST.get("budget")
        profile.preferred_type = request.POST.get("preferred_type")
        if request.FILES.get("image"):
            profile.image = request.FILES.get("image")
        profile.save()

        return redirect(request.path)  # reload page

    return render(request, "vacation-rental-master/profile.html", {"profile": profile})

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.conf import settings
import razorpay

# -----------------------------
# PROPERTIES LIST (20 HOMES)
# -----------------------------
def properties_view(request):
    min_rent = request.GET.get("min_rent")
    max_rent = request.GET.get("max_rent")

    homes = []

    for i in range(1, 21):
        home = {
            "id": i,
            "image": f"home{i}.jpg",
            "title": f"Rental Home {i}",
            "location": "City Area",
            "rent": 8000 + i * 700,
            "bedrooms": (i % 4) + 1,
            "bathrooms": (i % 3) + 1,
            "hall": 1,
            "kitchen": 1,
            "balcony": i % 2 == 0,
            "parking": i % 3 == 0,
        }

        if min_rent and home["rent"] < int(min_rent):
            continue
        if max_rent and home["rent"] > int(max_rent):
            continue

        homes.append(home)

    return render(request, "vacation-rental-master/properties.html", {
        "homes": homes
    })


# -----------------------------
# PROPERTY DETAIL (STATIC)
# -----------------------------
def property_detail(request, id):
    images = []

    for i in range(id, id + 4):
        img_id = i if i <= 20 else i - 20
        images.append(f"home{img_id}.jpg")

    home = {
        "id": id,
        "images": images,
        "title": f"Rental Home {id}",
        "location": "City Area",
        "rent": 8000 + id * 700,
        "bedrooms": (id % 4) + 1,
        "bathrooms": (id % 3) + 1,
        "hall": 1,
        "kitchen": 1,
        "balcony": id % 2 == 0,
        "parking": id % 3 == 0,
        "description": "Spacious rental home with modern facilities, balcony and parking."
    }

    return render(request, "vacation-rental-master/property_detail.html", {
        "home": home
    })


# -----------------------------
# RAZORPAY PAYMENT
# -----------------------------
client = razorpay.Client(
    auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET)
)

def demo_payment(request, property_id):
    amount = 50000  # ₹500 in paise

    order = client.order.create({
        "amount": amount,
        "currency": "INR",
        "payment_capture": 1
    })

    return render(request, "vacation-rental-master/pay_rent.html", {
        "order_id": order["id"],
        "amount": amount,
        "razorpay_key": settings.RAZORPAY_KEY_ID,
        "property_id": property_id
    })


def payment_success(request):
    return render(request, "vacation-rental-master/payment_success.html")


from django.shortcuts import render, get_object_or_404
from .models import Property

def video_call(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    return render(request, "vacation-rental-master/video_call.html", {"property": property})








    





    
from django.shortcuts import render

def property_page(request):
    return render(request, "vacation-rental-master/property_management.html" )

from .models import Property


from django.shortcuts import get_object_or_404
def property_detail(request, pk):
    from .models import Property
    property = Property.objects.first()   # just test
    return render(request,
        "vacation-rental-master/property_detail.html",
        {"home": property}
    )

from django.shortcuts import render, get_object_or_404, redirect
from .models import Property

def edit_property(request, pk):
    property = get_object_or_404(Property, pk=pk)

    if request.method == "POST":
        property.title = request.POST.get('title')
        property.price = request.POST.get('price')
        property.location = request.POST.get('location')
        property.save()
        return redirect('properties')

    return render(request, 'vacation-rental-master/edit_property.html', {'property': property})

from django.shortcuts import render, redirect
from .models import Property

def add_property(request):

    if request.method == "POST":

        title = request.POST['title']
        location = request.POST['location']
        rent = request.POST['rent']
        image = request.FILES['image']

        Property.objects.create(
            title=title,
            location=location,
            rent=rent,
            image=image
        )

        return redirect('properties')

    return render(request, 'vacation-rental-master/add_property.html')







from django.views.generic import ListView
from .models import Property

class PropertyListView(ListView):
    model = Property
    template_name = 'properties.html'
    context_object_name = 'properties'


from django.shortcuts import render
from .models import Property

def properties(request):
    properties = Property.objects.all()


from django.shortcuts import get_object_or_404, redirect
from .models import Property

def delete_property(request, pk):
    property = get_object_or_404(Property, pk=pk)

    property.delete()

    return redirect('properties')    

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Property, ChatMessage
from django.contrib.auth.models import User

@login_required
def chat_with_owner(request, property_id):

    property = get_object_or_404(Property, id=property_id)
    owner = property.user   # property owner

    # show messages between owner and current user
    messages = ChatMessage.objects.filter(property=property).order_by('timestamp')

    if request.method == "POST":
        text = request.POST.get("message")

        # determine receiver
        if request.user == owner:
            receiver = messages.first().sender   # customer
        else:
            receiver = owner

        ChatMessage.objects.create(
            property=property,
            sender=request.user,
            receiver=receiver,
            message=text
        )

        return redirect("chat_with_owner", property_id=property.id)

    return render(request, "vacation-rental-master/chat.html", {
        "property": property,
        "messages": messages
    })




def video_call(request, pk):
    return render(request, "vacation-rental-master/video_call.html")


from django.shortcuts import render, get_object_or_404
from .models import Property

def property_detail(request, pk):
    home = get_object_or_404(Property, pk=pk)
    return render(request, "vacation-rental-master/property_detail.html", {"home": home})