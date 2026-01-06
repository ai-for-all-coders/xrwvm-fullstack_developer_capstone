from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [
    # path for registration
    path('register/', views.registration, name='register'),

    # path for login
    path('login/', views.login_user, name='login'),

    # fetch all cars
    path('get_cars/', views.get_cars, name='get_cars'),

    # fetch all dealers
    path('get_dealers/', views.get_dealerships, name='get_dealers'),

    # fetch dealers by state
    path('get_dealers/<str:state>/', views.get_dealerships, name='get_dealers_by_state'),

    # fetch dealer details by id
    path('dealer/<int:dealer_id>/', views.get_dealer_details, name='dealer_details'),

    # fetch reviews for a dealer
    path('reviews/dealer/<int:dealer_id>/', views.get_dealer_reviews, name='dealer_reviews'),

    # add a review
    path('add_review/', views.add_review, name='add_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
