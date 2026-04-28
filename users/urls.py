# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),

#     path("", views.index, name="index"),
#     path("login/", views.login_view, name="login"),
#     path('', views.home, name='home'),  # Home page
#     path("index/", views.index, name="index"),

#     path('signup/', views.signup_view, name='signup'),

#     path('send-signup-otp/', views.send_signup_otp, name='send_signup_otp'),

#   # Signup page
#     # path('verify-signup-otp/', views.verify_signup_otp, name='verify_signup_otp'),  # OTP verification
#     path("verify-otp/", views.verify_otp, name="verify_otp"),
#     path('login/', views.login_view, name='login'),  # Normal login page
#     path('logout/', views.logout_view, name='logout'),  # Logout

#     # Social login URLs (Django allauth handles the backend)
#     path('google-login/', views.google_login, name='google_login'),
#     path('github-login/', views.github_login, name='github_login'),


#     path('home/', views.home, name='home'),

#     path('index/', views.home, name='home'),
#     path('about/', views.about, name='about'),
#     path('departments/', views.departments, name='departments'),
#     path('services/', views.services, name='services'),
#     path('rooms/', views.rooms, name='rooms'),
#     path('blog/', views.blog, name='blog'),
#     path('contact/', views.contact, name='contact'),
#     path("contact/success/", views.contact_success, name="contact_success"),
#     path('categories/', views.categories, name='categories'),
#     path("properties/", views.properties_view, name="properties"),
#     path("property/add/", views.add_property, name="add_property"),
#     path("property/edit/<int:id>/", views.edit_property, name="edit_property"),
#     path("property/delete/<int:id>/", views.delete_property, name="delete_property"),


#    path("profile/", views.profile_view, name="profile"),
#    path("property/<int:id>/", views.property_detail, name="property_detail"),

#    # urls.py

# path("pay/<int:property_id>/", views.demo_payment, name="demo_payment"),
# path("success/<int:payment_id>/", views.payment_success, name="payment_success"),
# path("history/", views.payment_history, name="payment_history"),1




# ]


from django.urls import path
from . import views






urlpatterns = [

    # main
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),

    # auth
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('send-signup-otp/', views.send_signup_otp, name='send_signup_otp'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('logout/', views.logout_view, name='logout'),

    # social
    path('google-login/', views.google_login, name='google_login'),
    path('github-login/', views.github_login, name='github_login'),

    # pages
    path('about/', views.about, name='about'),
    path('departments/', views.departments, name='departments'),
    path('services/', views.services, name='services'),
    path('rooms/', views.rooms, name='rooms'),
    path('blog/', views.blog, name='blog'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('categories/', views.categories, name='categories'),
 # ---------------- PUBLIC PAGES ----------------
    path('properties/', views.properties_view, name='properties'),
    path('property/<int:pk>/', views.property_detail, name='property_detail'),
    path('property/<int:pk>/edit/', views.edit_property, name='edit_property'),

    path('properties/', views.properties, name='properties'),
    path('property/<int:pk>/delete/', views.delete_property, name='delete_property'),
   
    # profile
    path('profile/', views.profile_view, name='profile'),

    # payment
    
    path("pay/<int:property_id>/", views.demo_payment, name='pay_rent'),
    path("payment-success/", views.payment_success, name="payment_success"),

    path('property/<int:pk>/video-call/', views.video_call, name='video_call'),

    path('chat/<int:property_id>/', views.chat_with_owner, name='chat_with_owner'),

    path('add-property/', views.add_property, name='add_property'),


 

       

    

]
