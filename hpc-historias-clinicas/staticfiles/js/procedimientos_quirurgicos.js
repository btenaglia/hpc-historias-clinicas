  $(document).ready(function() {
    /* --------------------------------------------
     -- Rellenar el text area de descripcion de ---
     -- de un procedimiento quirurgico           --
     ----------------------------------------------*/
    $("#id_procedimiento_quirurgico").on('change', traer_descripcion_proc_quirurgico);
    function traer_descripcion_proc_quirurgico() {
        $.ajax({
            data: { 'pk': $(this).val() },
            url: '/procedimientos/quirurgicos/traer/descripcion/',
            type: 'GET',
            success: function(data){
                $("#id_descripcion").val("");
                $("#id_descripcion").val( data[0].fields.descripcion );
            }
        });
    }

});