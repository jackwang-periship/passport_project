from django import forms


class DatePickerWidget(forms.DateInput):
    def get_context(self, name, value, attrs):
        attrs['data-custom-widget'] = self.__class__.__name__
        context = super().get_context(name, value, attrs)
        return context

    class Media:
        js = ('AdminLTE-3.0.5/plugins/jquery/jquery.min.js', 'AdminLTE-3.0.5/plugins/moment/moment.min.js',
              'AdminLTE-3.0.5/plugins/daterangepicker/daterangepicker.js', 'js/widgets/datepickerwidget.js')


class DateTimePickerWidget(forms.DateInput):
    template_name = 'wiawdp/widgets/datetimepickerwidget.html'

    class Media:
        js = ('AdminLTE-3.0.5/plugins/jquery/jquery.min.js', 'AdminLTE-3.0.5/plugins/moment/moment.min.js',
              'AdminLTE-3.0.5/plugins/daterangepicker/daterangepicker.js', 'js/widgets/datetimepickerwidget.js')


class InputMaskWidget(forms.TextInput):
    def __init__(self, attrs=None, input_mask={}):
        self.input_mask = input_mask
        super().__init__(attrs)

    def mask_dict_to_string(self):
        pairs = (f"'{key}': '{value}'" for key, value in self.input_mask.items())
        return ','.join(pairs)

    def get_context(self, name, value, attrs):
        attrs['data-inputmask'] = self.mask_dict_to_string()
        attrs['data-custom-widget'] = self.__class__.__name__
        return super().get_context(name, value, attrs)

    class Media:
        js = ('AdminLTE-3.0.5/plugins/inputmask/inputmask.min.js', 'js/widgets/inputmaskwidget.js')
