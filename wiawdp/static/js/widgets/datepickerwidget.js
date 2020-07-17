window.addEventListener('DOMContentLoaded', () => {
    $('input[data-custom-widget="DatePickerWidget"]').daterangepicker({
        singleDatePicker: true,
        showDropdowns: true,
        locale: {
            format: 'Y-MM-DD'
        }
    });

    const widgets = document.querySelectorAll('input[data-custom-widget="DatePickerWidget"]');
    Inputmask().mask(widgets);
});
