from django.urls import path
from AutoSpa.views import user_list, create_user, edit_user, delete_user, \
                   reservation_list, create_reservation, edit_reservation, delete_reservation

urlpatterns = [
    # Trasy URL dla użytkowników
    path('users/', user_list, name='user_list'),
    path('users/create/', create_user, name='create_user'),
    path('users/edit/<int:user_id>/', edit_user, name='edit_user'),
    path('users/delete/<int:user_id>/', delete_user, name='delete_user'),

    # Trasy URL dla rezerwacji
    path('reservations/', reservation_list, name='reservation_list'),
    path('reservations/create/', create_reservation, name='create_reservation'),
    path('reservations/edit/<int:reservation_id>/', edit_reservation, name='edit_reservation'),
    path('reservations/delete/<int:reservation_id>/', delete_reservation, name='delete_reservation'),
]
