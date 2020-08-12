window.addEventListener('DOMContentLoaded', () => {
    const widgets = document.querySelectorAll('input[data-custom-widget="InputMaskWidget"]');
    Inputmask().mask(widgets);
});

