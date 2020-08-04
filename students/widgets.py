from django import forms

class InputMaskWidget(forms.TextInput):
    def get_context(self, name, value, attrs):
        attrs['data-custom-widget'] = self.__class__.__name__
        return super().get_context(name, value, attrs)

    class Media:
        js = ('AdminLTE-3.0.5/plugins/inputmask/inputmask.min.js', 'js/widgets/inputmaskwidget.js')