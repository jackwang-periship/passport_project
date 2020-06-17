from django.shortcuts import render
from django.http import HttpResponse
from .models import Transaction, VerifiedId, Report
from .forms import TransactionForm, VerifiedIdForm, ReportForm

# Create your views here.

def index(request):
    return render(request, "billing/index.html", {})

def verify(request):
    form = VerifiedIdForm(request.POST or None)
    if form.is_valid():
        # VerifiedId.objects.create(**form.cleaned_data)
        form.save()
        return home(request)
    else:
        print(form.errors)
    return render(request, "billing/verify.html", {'form': form})

def payment(request):
    form = TransactionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return notice(request)
    else:
        print(form.errors)
    return render(request, "billing/payment.html", {'form': form})

def notice(request):
    # Add [:x] index value to change number of transactions in list
    # verifiedId = VerifiedId.objects.get(studentId=studentId)
    # transactions = Transaction.objects.filter(verifiedId=verifiedId).order_by('-date')
    transactions = Transaction.objects.order_by('-date')
    return render(request, "billing/notice.html", {'transactions': transactions})


def report(request):
    form = ReportForm()
    if request.method == 'POST':
        form = ReportForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return logs(request)
        else:
            print(form.errors)
    return render(request, "billing/report.html", {'form': form})

def logs(request):
    return render(request, "billing/index.html", {'page': 'Sales Logs'})
