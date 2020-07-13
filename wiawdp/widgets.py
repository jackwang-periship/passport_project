from django import forms


class DatePickerWidget(forms.DateInput):
    def get_context(self, name, value, attrs):
        attrs['data-custom-widget'] = self.__class__.__name__
        context = super().get_context(name, value, attrs)
        return context

    class Media:
        js = ('js/jquery-3.5.1.min.js', 'AdminLTE-3.0.5/plugins/moment/moment.min.js',
              'AdminLTE-3.0.5/plugins/daterangepicker/daterangepicker.js', 'js/widgets/datepickerwidget.js')


class DateTimePickerWidget(forms.DateInput):
    template_name = 'wiawdp/widgets/datetimepickerwidget.html'

    class Media:
        js = ('js/jquery-3.5.1.min.js', 'AdminLTE-3.0.5/plugins/moment/moment.min.js',
              'AdminLTE-3.0.5/plugins/daterangepicker/daterangepicker.js', 'js/widgets/datetimepickerwidget.js')
