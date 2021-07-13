from django.urls import path

from Plaid import views
urlpatterns = [
    path('', views.index, name="index"),
    path('auth', views.get_auth, name="get_auth"),
    path('signup', views.sign_up, name="signup"),
    # path('create_user', views.create_user, name="create_user"),
    path('login', views.log_in, name="login"),
    path('logout', views.log_out, name="logout"),
    path('create-link-token', views.create_link_token, name="create-link-token"),
    path('get-access-token', views.get_access_token, name='get-access-token'),

    path('link-account', views.link_account, name="link-account"),
    path('transactions', views.transactions, name="transactions"),
    path('transactions/get', views.get_transactions, name="get-transaction")
]
