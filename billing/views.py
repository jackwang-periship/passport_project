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
    # form = LogFilterForm()
    form = ReportForm()
    if request.method == 'POST' and request.POST != {}:
        formReport = ReportForm(request.POST)
        if formReport.is_valid():
            # If the "save" button is clicked, the save the formReport data
            if request.POST['submit'] == 'Save as a report':
                formReport.save(commit=True)
            startDate = formReport.cleaned_data['startD']
            endDate = formReport.cleaned_data['endD']
            type = formReport.cleaned_data['type']
            if type == "all":   # Cheek the type, if it is "all" then no need to add "order by" clause
                results = Transaction.objects.filter(date__range=[startDate, endDate])
            else:   # order by is similar to group.
                results = Transaction.objects.filter(date__range=[startDate, endDate]).order_by('-' + type)
            table = Notice(results)
            RequestConfig(request, paginate={"per_page": 10}).configure(table)
            context = {'table': table, 'form': formReport}
            return render(request, "billing/logs.html", context)
    results = Transaction.objects.all()
    table = Notice(results)
    RequestConfig(request, paginate={"per_page": 10}).configure(table)
    context = {'table': table, 'form': form}
    return render(request, "billing/logs.html", context)


