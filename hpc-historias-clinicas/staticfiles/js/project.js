$(document).ready(function() {
    /* ---------------------
     -- common datepicker --
     ----------------------- */
    $('.dateinput').datepicker({
        format: 'dd/mm/yyyy'
    }).on('changeDate', function(ev){
        // -- hide dropdown when change dates
        $('.dropdown-menu').hide();
    });
});
