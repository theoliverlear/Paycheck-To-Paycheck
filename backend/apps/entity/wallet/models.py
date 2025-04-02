from django.db import models


class WalletOrmModel(models.Model):
    id = models.AutoField(primary_key=True)
    checking_account = models.OneToOneField('saving.SavingOrmModel',
                                            on_delete=models.CASCADE,
                                            related_name='wallet',
                                            default=None)
