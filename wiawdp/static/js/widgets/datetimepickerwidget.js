window.addEventListener('DOMContentLoaded', () => {
    $('input[data-custom-widget="DateTimePickerWidget"]').daterangepicker({
        singleDatePicker: true,
        timePicker: true,
        timePicker24Hour: true,
        showDropdowns: true,
        locale: {
            format: 'YYYY-MM-DD hh:mm:ss'
        }
    });

    const widgets = document.querySelectorAll('input[data-custom-widget="DateTimePickerWidget"]');
    Inputmask().mask(widgets);
});
