from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",views.home,name="homepage"),
    path("book_list/",views.book_list,name="book_list"),
    path("account/register/",views.registration,name="registration"),
    path("account/login/",views.user_login,name="login"),
    path("account/logout/",views.user_logout,name="logout"),
    path("add_book/",views.add_book,name="add_book"),
    path("show_book/",views.show_book,name="show_book"),
    path("account/profile",views.profile,name="profile"),
    path("account/profile/edit_book/<int:id>/", views.edit_book, name="edit_book"),
    path("account/profile/delete_book/<int:id>/", views.delete_book, name="delete_book"),
    path("home/search/", views.search_book, name="search_book"),
    path("show_book/pdf/<int:id>/",views.show_pdf,name="show_pdf")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
