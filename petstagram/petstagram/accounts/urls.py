from django.urls import path, include

from petstagram.accounts.views import ProfileDetailsView, ProfileEditView, ProfileDeleteView, RegisterUserView, \
    LoginUserView, LogoutUserView

urlpatterns = (
    path('register/', RegisterUserView.as_view(), name='register-user'),
    path('login/', LoginUserView.as_view(), name='login-user'),
    path('logout/', LogoutUserView.as_view(), name='logout-user'),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='profile-details-user'),
        path('edit/', ProfileEditView.as_view(), name='profile-edit-user'),
        path('delete/', ProfileDeleteView.as_view(), name='profile-delete-user'),
    ]))
)
