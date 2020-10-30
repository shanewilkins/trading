from django.db import models

# Create your models here.


class JournalEntries(models.Model):
    id = models.AutoField(primary_key=True)
    entry_date = models.DateField("Journal Entry Date")
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.description


class Accounts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)
    type = models.ForeignKey('AccountTypes', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AccountTypes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name


class Debits(models.Model):
    id = models.AutoField(primary_key=True)
    journal_entry_id = models.ForeignKey('JournalEntries', on_delete=models.CASCADE)
    account_id = models.ForeignKey("Accounts", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=11, decimal_places=2)

    def __str__(self):
        return self.id


class Credits(models.Model):
    id = models.AutoField(primary_key=True)
    journal_entry_id = models.ForeignKey('JournalEntries', on_delete=models.CASCADE)
    account_id = models.ForeignKey("Accounts", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=11, decimal_places=2)

    def __str__(self):
        return self.id
