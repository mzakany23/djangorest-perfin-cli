from django import forms
from transaction.models import Transaction

class TransactionForm(forms.Form):
	date = forms.DateField()
	name = forms.CharField(max_length=250)
	amount = forms.DecimalField(decimal_places=2,max_digits=6)

	def clean(self):
		cleaned_data = super(TransactionForm, self).clean()
		name = cleaned_data.get("name")
		amount = cleaned_data.get("amount")

		try:
			transaction = Transaction.objects.get(name=name,amount=amount)
		except:
			transaction = None

		if transaction:
			raise forms.ValidationError('transaction exists')			
