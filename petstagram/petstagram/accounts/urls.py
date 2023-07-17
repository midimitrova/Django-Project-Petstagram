from django.urls import path, include

from petstagram.accounts.views import profile_details_user, profile_edit_user, \
    profile_delete_user, RegisterUserView, LoginUserView, LogoutUserView

urlpatterns = (
    path('register/', RegisterUserView.as_view(), name='register-user'),
    path('login/', LoginUserView.as_view(), name='login-user'),
    path('logout/', LogoutUserView.as_view(), name='logout-user'),
    path('profile/<int:pk>/', include([
        path('', profile_details_user, name='profile-details-user'),
        path('edit/', profile_edit_user, name='profile-edit-user'),
        path('delete/', profile_delete_user, name='profile-delete-user'),
    ]))
)
