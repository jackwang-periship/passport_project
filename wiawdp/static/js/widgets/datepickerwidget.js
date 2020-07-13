window.addEventListener('DOMContentLoaded', () => {
    $('input[data-custom-widget="DatePickerWidget"]').daterangepicker({
        singleDatePicker: true,
        showDropdowns: true,
        locale: {
            format: 'Y-MM-DD'
        }
    });
});
