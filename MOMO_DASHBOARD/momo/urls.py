from django.urls import path

from . import views

app_name = "momo"
urlpatterns = [
    path("", views.home, name="home"),
    path("airtime", views.airtime, name="airtime"),
    path("momotransfer", views.transfers_to_momo, name="transferstomomo"),
    path("paymenttocode", views.payment_to_code, name="paymenttocode"),
    path("cashpower", views.cashpower_payments, name="cashpower"),
    path("transactions", views.payments_to_third_parties, name="transactions"),
    path("withdrawals", views.withdrawals, name="withdrawals"),
    path("data", views.bundles_and_packs, name="data"),
    path("incomingmoney", views.moneyreceived, name="moneyrecieved"),
    path("bankdepo", views.bankdeposits, name="bankdepo"),
    path('api/transaction-data/', views.get_transaction_data, name='transaction_data'),
]