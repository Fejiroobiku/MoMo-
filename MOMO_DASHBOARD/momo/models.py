# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AirtimePayments(models.Model):
    amount = models.IntegerField()
    service_provider = models.CharField(max_length=64)
    fee = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'airtime_payments'


class BankDeposits(models.Model):
    amount = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bank_deposits'


class BundlesAndPacks(models.Model):
    amount = models.IntegerField()
    service_provider = models.CharField(max_length=64)
    fee = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bundles_and_packs'


class CashPowerPayments(models.Model):
    amount = models.IntegerField()
    service_provider = models.CharField(max_length=64)
    fee = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'cash_power_payments'


class MoneyRecieved(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    amount = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'money_recieved'


class PaymentToCode(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    code = models.IntegerField()
    amount = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'payment_to_code'


class PaymentsToThirdParties(models.Model):
    amount = models.IntegerField()
    service_provider = models.CharField(max_length=64)
    fee = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'payments_to_third_parties'


class TransfersToMomo(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    tel = models.IntegerField()
    amount = models.IntegerField()
    fee = models.IntegerField(blank=True, null=True)
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'transfers_to_momo'


class Withdrawals(models.Model):
    agent = models.CharField(max_length=64)
    agent_tel = models.IntegerField()
    amount = models.IntegerField()
    fee = models.IntegerField()
    date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'withdrawals'
