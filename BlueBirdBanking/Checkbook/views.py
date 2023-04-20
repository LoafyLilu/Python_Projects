from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction


# This function will render the Home page when requested
def home(request):
    form = TransactionForm(data=request.POST or None)   # Retrieve Transaction form
    # Checks if request method is POST
    if request.method == 'POST':
        pk = request.POST['account']    # If the form is submitted, retrieve account user wants to view
        return balance(request, pk)     # Call balance function to render that accounts balance sheet
    content = {'form': form}           # Pass content to the template as a dictionary
    #Adds content of form to page
    return render(request, 'checkbook/index.html', content)


# This function will render the Create New Account page when requested
def create_account(request):
    form = AccountForm(data=request.POST or None)  # Retrieve the Account Form
    # Checks if request method is POST
    if request.method == 'POST':
        # returns user to home page
        if form.is_valid():  # Checks to see if the submitted form is valid, and saves if so.
            form.save()
            return redirect('index')  # returns user to home page

    # Saves the content to the template as a dictionary, and adds content of form to page
    content = {'form': form}
    return render(request, 'checkbook/CreateNewAccount.html', content)


# This function will render the Balance page when requested
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk)     # Retrieve the requested account using its pk
    transactions = Transaction.Transactions.filter(account=pk)  # Retrieve all of that accounts transactions
    current_total = account.initial_deposit     #Create account total variable stating with initial deposit value
    table_contents = {}     # Create a dictionary into which transaction info will be placed
    for t in transactions:      # Loop through transactions and determine which is a deposit or withdrawal
        if t.type =='Deposit':
            current_total += t.amount       # If deposit, add amount to balance
            table_contents.update({t: current_total})       # Add transaction to the dictionary
        else:
            current_total -= t.amount       # If withdrawal subtract from amount
            table_contents.update({t: current_total})       # Add transaction to the dictionary

    # Pass account, account total balance, and transaction information to the template
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)


# This function will render the Transaction page when requested
def transaction(request):
    # Retrieves the Transaction form, and checks to see if method is POST
    form = TransactionForm(data=request.POST or None)
    if request.method == 'POST':
        # Checks to see if form is valid, and if so saves the form, redirecting user to home page
        if form.is_valid():
            pk = request.POST['account']    # Retrieves which account the transaction was for
            form.save()
            return balance(request, pk)     #Renders balance of the accounts Balance Sheet
    # Pass content to the template in a dictionary, and adds content of form to page
    content = {'form': form}
    return render(request, 'checkbook/AddTransaction.html', content)
