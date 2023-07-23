from django.contrib import admin
from django.urls import path, include  # Import the 'include' function
from myapp import views  # Import views from the app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='index')  # For /index/ URL, mapped to index_view
    # path('', views.plot_timeseries, name='plot_timeseries'),  # Route to plot_timeseries view
    # path('public_profile/', views.view_profile, name='public_profile'),  # Route to view_profile view
    # path('edit_profile/', views.edit_profile, name='edit_profile'),  # Route to edit_profile view
    # path('plot.png/', views.serve_plot, name='serve_plot'),  # Route to serve_plot view
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),  # Route to login_view
    path('forgot_password/', views.forgot_password, name='forgot_password'),  # Route to forgot_password view
    path('logout/', views.logout, name='logout'),  # Route to logout view
    path('about_us/', views.about_us, name='about_us'),  # Route to about_us view


]


