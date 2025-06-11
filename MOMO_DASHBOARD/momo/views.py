from django.shortcuts import render
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from datetime import datetime, timedelta
from django.http import JsonResponse
from .models import (
    AirtimePayments,
    MoneyRecieved,
    TransfersToMomo,
    BankDeposits,
    PaymentToCode,
    CashPowerPayments,
    Withdrawals,
    PaymentsToThirdParties,
    BundlesAndPacks,
)
import json


# Create your views here.
def home(request):
    # retrieving transaction counts for each model
    transaction_counts = {
        "airtime": AirtimePayments.objects.count(),
        "bank_deposits": BankDeposits.objects.count(),
        "bundles_packs": BundlesAndPacks.objects.count(),
        "cash_power": CashPowerPayments.objects.count(),
        "money_received": MoneyRecieved.objects.count(),
        "payments_code": PaymentToCode.objects.count(),
        "third_party": PaymentsToThirdParties.objects.count(),
        "momo_transfers": TransfersToMomo.objects.count(),
        "withdrawals": Withdrawals.objects.count(),
    }

    # Calculating total number of transactions of all models
    total_transactions = sum(transaction_counts.values())

    # Avoiding ZeroDivisionError
    if total_transactions == 0:
        percentages = {key: 0 for key in transaction_counts}
    else:
        percentages = {key: (count / total_transactions) * 100 for key, count in transaction_counts.items()}

    # adding percentages to the template
    context = {
        "airtime_percentage": percentages["airtime"],
        "bank_deposits_percentage": percentages["bank_deposits"],
        "bundles_packs_percentage": percentages["bundles_packs"],
        "cash_power_percentage": percentages["cash_power"],
        "money_received_percentage": percentages["money_received"],
        "payments_code_percentage": percentages["payments_code"],
        "third_party_percentage": percentages["third_party"],
        "momo_transfers_percentage": percentages["momo_transfers"],
        "withdrawals_percentage": percentages["withdrawals"],
    }

    return render(request, "momo/index.html", context)


def airtime(request):
    return render(
        request, "momo/airtime.html", {"airtime": AirtimePayments.objects.all()}
    )


def transfers_to_momo(request):
    return render(
        request,
        "momo/momotransfer.html",
        {"momotransfers": TransfersToMomo.objects.all(),
         },
    )


def bankdeposits(request):
    return render(
        request, "momo/bankdepo.html", {"bankdepo": BankDeposits.objects.all()}
    )


def payment_to_code(request):
    return render(
        request,
        "momo/paymenttocode.html",
        {"paymenttocode": PaymentToCode.objects.all()},
    )


def cashpower_payments(request):
    return render(
        request, "momo/cashpower.html", {"cashpower": CashPowerPayments.objects.all()}
    )


def payments_to_third_parties(request):
    return render(
        request,
        "momo/transactions.html",
        {"transactions": PaymentsToThirdParties.objects.all()},
    )


def withdrawals(request):
    return render(
        request, "momo/withdrawals.html", {"withdrawals": Withdrawals.objects.all()}
    )


def bundles_and_packs(request):
    return render(request, "momo/data.html", {"data": BundlesAndPacks.objects.all()})


def moneyreceived(request):
    return render(
        request,
        "momo/incomingmoney.html",
        {"moneyrecieved": MoneyRecieved.objects.all()},
    )


def get_transaction_data(request):
    # Getting data for the last 12 months
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)

    # Total transaction volume by type
    transaction_volumes = {
        "Airtime": AirtimePayments.objects.filter(
            date__range=[start_date, end_date]
        ).aggregate(total=Sum("amount"))["total"]
        or 0,
        "Bank Deposits": BankDeposits.objects.filter(
            date__range=[start_date, end_date]
        ).aggregate(total=Sum("amount"))["total"]
        or 0,
        "Bundles": BundlesAndPacks.objects.filter(
            date__range=[start_date, end_date]
        ).aggregate(total=Sum("amount"))["total"]
        or 0,
        "Cash Power": CashPowerPayments.objects.filter(
            date__range=[start_date, end_date]
        ).aggregate(total=Sum("amount"))["total"]
        or 0,
        "Money Received": MoneyRecieved.objects.filter(
            date__range=[start_date, end_date]
        ).aggregate(total=Sum("amount"))["total"]
        or 0,
        "Code Payments": PaymentToCode.objects.filter(
            date__range=[start_date, end_date]
        ).aggregate(total=Sum("amount"))["total"]
        or 0,
        "Third Party": PaymentsToThirdParties.objects.filter(
            date__range=[start_date, end_date]
        ).aggregate(total=Sum("amount"))["total"]
        or 0,
        "MOMO Transfers": TransfersToMomo.objects.filter(
            date__range=[start_date, end_date]
        ).aggregate(total=Sum("amount"))["total"]
        or 0,
        "Withdrawals": Withdrawals.objects.filter(
            date__range=[start_date, end_date]
        ).aggregate(total=Sum("amount"))["total"]
        or 0,
    }

    # Monthly transaction totals
    monthly_data = {}
    for model in [
        AirtimePayments,
        BankDeposits,
        BundlesAndPacks,
        CashPowerPayments,
        MoneyRecieved,
        PaymentToCode,
        PaymentsToThirdParties,
        TransfersToMomo,
        Withdrawals,
    ]:
        monthly_totals = (
            model.objects.filter(date__range=[start_date, end_date])
            .annotate(month=TruncMonth("date"))
            .values("month")
            .annotate(total=Sum("amount"))
            .order_by("month")
        )

        for entry in monthly_totals:
            month_str = entry["month"].strftime("%Y-%m")
            if month_str not in monthly_data:
                monthly_data[month_str] = 0
            monthly_data[month_str] += entry["total"]

    # Service provider distribution
    provider_data = {}
    for model in [
        AirtimePayments,
        BundlesAndPacks,
        CashPowerPayments,
        PaymentsToThirdParties,
    ]:
        provider_totals = (
            model.objects.filter(date__range=[start_date, end_date])
            .values("service_provider")
            .annotate(total=Sum("amount"))
        )

        for entry in provider_totals:
            provider = entry["service_provider"]
            if provider not in provider_data:
                provider_data[provider] = 0
            provider_data[provider] += entry["total"]

    return JsonResponse(
        {
            "transaction_volumes": transaction_volumes,
            "monthly_data": monthly_data,
            "provider_data": provider_data,
        }
    )
