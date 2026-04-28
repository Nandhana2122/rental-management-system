# from django.contrib import admin
# from django.urls import path, include
# from django.shortcuts import redirect
# from users import views
# from django.conf import settings
# from django.conf.urls.static import static

# def redirect_to_login(request):
#     return redirect('login')

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', redirect_to_login),
#     path('', include('users.urls')),
#     path('accounts/', include('allauth.urls')),  # ✅ REQUIRED
#     path('auth/', include('social_django.urls', namespace='social')),
#     path('properties/', views.properties_view, name='properties'),
#     path("", include("users.urls")),



# ]    


# # Add this at the bottom
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)









from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static


def redirect_to_login(request):
    return redirect('login')


urlpatterns = [
    path('admin/', admin.site.urls),

    # root redirect
    path('', redirect_to_login, name='root'),

    # app urls
    path('', include('users.urls')),
    # path("", include("properties.urls")),

    # auth
    path('accounts/', include('allauth.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


