from django.urls import path, include

from petstagram.accounts.views import register_user, login_user, profile_details_user, profile_edit_user, \
    profile_delete_user

urlpatterns = (
    path('register/', register_user, name='register-user'),
    path('login/', login_user, name='login-user'),
    path('profile/<int:pk>/', include([
        path('', profile_details_user, name='profile-details-user'),
        path('edit/', profile_edit_user, name='profile-edit-user'),
        path('delete/', profile_delete_user, name='profile-delete-user'),
    ]))
)
