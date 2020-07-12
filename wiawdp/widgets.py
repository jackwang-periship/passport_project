from django import forms


class DatePickerWidget(forms.DateInput):
    template_name = 'wiawdp/widgets/datepickerwidget.html'

    class Media:
        js = ('js/jquery-3.5.1.min.js', 'AdminLTE-3.0.5/plugins/moment/moment.min.js',
              'AdminLTE-3.0.5/plugins/daterangepicker/daterangepicker.js')


class DateTimePickerWidget(forms.DateInput):
    template_name = 'wiawdp/widgets/datetimepickerwidget.html'

    class Media:
        js = ('js/jquery-3.5.1.min.js', 'AdminLTE-3.0.5/plugins/moment/moment.min.js',
              'AdminLTE-3.0.5/plugins/daterangepicker/daterangepicker.js')
