from django.urls import path
from billing import views

app_name = 'billing'

urlpatterns = [
        path('',views.index,name='index'),
        path('verify/',views.verify,name='verify'),
        path('payment/',views.payment,name='payment'),
        path('notice/',views.notice,name='notice'),
        path('report/',views.report,name='report'),
        path('logs/',views.logs,name='logs'),
]