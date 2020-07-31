from django.shortcuts import render, redirect
from django.http import HttpResponse
from students.models import Student
from .models import Transaction, VerifiedId, Report
from .forms import TransactionForm, VerifiedIdForm, ReportForm
from django_tables2 import SingleTableView
from django.views.generic.base import TemplateView
from .tables import Notice, Logs
import home


# Create your views here.


def index(request):
    return render(request, "billing/index.html", {})


def verify(request):
    form = VerifiedIdForm(request.POST or None)
    if form.is_valid():
        # VerifiedId.objects.create(**form.cleaned_data)
        form.save()
        return payment(request)
    else:
        print(form.errors)
    return render(request, "billing/verify.html", {'form': form})


def payment(request):
    formPay = TransactionForm(request.POST or None)
    if formPay.is_valid():
        formPay.save()
        return redirect('billing:notice')
    else:
        print(formPay.errors)
    return render(request, "billing/payment.html", {'form': formPay})


def notice(request):
    # Add [:x] index value to change number of transactions in list
    # verifiedId = VerifiedId.objects.get(studentId)
    # transactions = Transaction.objects.filter(verifiedId=verifiedId).order_by('-date')
    transactions = Transaction.objects.order_by('-date')
    table = Notice(transactions)
    context = {'table': table, 'transactions': transactions}
    return render(request, "billing/notice.html", context)


def report(request):
    formReport = ReportForm()
    if request.method == 'POST':
        formReport = ReportForm(request.POST)
        if formReport.is_valid():
            formReport.save(commit=True)
            return logs(request)
        else:
            print(formReport.errors)
    return render(request, "billing/report.html", {'form': formReport})


def logs(request):
    reports = Report.objects.order_by('-type')
    table = Logs(reports)
    context = {'table': table, 'report': reports}
    return render(request, "billing/logs.html", context)

