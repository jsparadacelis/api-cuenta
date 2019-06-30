# DRF utilities
from rest_framework import serializers

# Django Utilities
from django.db import transaction

# local apps
from .models import Account, Profile, Client, Transaction


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name', 'last_name', 'identification')


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'bank', 'create_date', 'balance')


class TransListSerializer(serializers.ListSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'commerce', 'profile', 'value')


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        list_serializer_class = TransListSerializer
        fields = ('id', 'commerce', 'profile', 'value')

    
    def create(self, validated_data):
        with transaction.atomic():
            profile = validated_data["profile"]
            account = Profile.account
            if Account.balance <= 0:
                raise serializers.ValidationError("Fondos insuficientes")
            account.balance = account.balance - validated_data["valor"]
            account.save()
            Transaction = Transaction(
                commerce = validated_data['commerce'], 
                profile = profile,
                value = validated_data["value"]
            )
            Transaction.save()
        return Transaction


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'account', 'client', 'role')