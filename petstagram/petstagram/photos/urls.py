from django.urls import path, include

from petstagram.photos.views import details_photo, edit_photo, delete_photo, PhotoAddView

urlpatterns = (
    path('add/', PhotoAddView.as_view(), name='add-photo'),
    path('<int:pk>/', include([
        path('', details_photo, name='details-photo'),
        path('edit/', edit_photo, name='edit-photo'),
        path('delete/', delete_photo, name='delete-photo'),
    ]))

)