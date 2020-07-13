window.addEventListener('DOMContentLoaded', () => {
    $('input[data-custom-widget="DateTimePickerWidget"]').daterangepicker({
        singleDatePicker: true,
        timePicker24Hour: true,
        showDropdowns: true,
        locale: {
            format: 'Y-MM-DD HH:mm:ss'
        }
    });
});
