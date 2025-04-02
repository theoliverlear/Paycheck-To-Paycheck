from django.db import models

class SafePasswordOrmModel(models.Model):
    id = models.AutoField(primary_key=True)
    encoded_password = models.CharField(max_length=100)
    class Meta:
        db_table = 'passwords'

class UserOrmModel(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100, default="")
    last_name = models.CharField(max_length=100, default="")
    email = models.EmailField(max_length=150, default="")
    username = models.CharField(max_length=100, default="")
    password = models.ForeignKey(SafePasswordOrmModel,
                                 on_delete=models.CASCADE)
    income_history = models.OneToOneField('income.IncomeHistoryOrmModel',
                                          on_delete=models.CASCADE,
                                          related_name='income_history_user',
                                          default=None)
    bill_history = models.OneToOneField('bill.BillHistoryOrmModel',
                                        on_delete=models.CASCADE,
                                        related_name='bill_history_user',
                                        default=None)
    wallet = models.OneToOneField('wallet.WalletOrmModel',
                                    on_delete=models.CASCADE,
                                    related_name='user_wallet',
                                    default=None)
    class Meta:
        db_table = 'users'
        abstract = False