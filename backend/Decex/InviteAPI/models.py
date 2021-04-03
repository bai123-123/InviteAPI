from django.db import models


# Create your models here.

class Test(models.Model):
    name = models.CharField(max_length=20)


class InviteRelationship(models.Model):
    TransactionReceipt = models.CharField(max_length=66, null=False, primary_key=True)
    Inviter = models.CharField(max_length=42, null=False)
    Invitee = models.CharField(max_length=42, null=False)
    TransactionReceiptJson = models.TextField(null=False)


class InviteReward(models.Model):
    Account = models.CharField(max_length=42, primary_key=True)
    RewardBalance = models.FloatField(null=False)

