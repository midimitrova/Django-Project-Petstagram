from django.shortcuts import render


def register_user(request):
    return render(request, 'accounts/register-page.html')


def login_user(request):
    return render(request, 'accounts/login-page.html')


def profile_details_user(request, pk):
    return render(request, 'accounts/profile-details-page.html')


def profile_edit_user(request, pk):
    return render(request, 'accounts/profile-edit-page.html')


def profile_delete_user(request, pk):
    return render(request, 'accounts/profile-delete-page.html')
