$(document).ready(function() { 

   /* -------------------------------------------------
        Ubicaciones - mostrar/ocultar el campo Otros
    --------------------------------------------------- */
    if ($('#id_cama ').val()!='Otros'){
        $('#ubicaciones_form ').children("#div_id_comentario").hide();
    }
    $('#id_cama ').on('change', mostrar_comentario_ubicacion);
    function mostrar_comentario_ubicacion(){
        if ($('#id_cama ').val() == 'Otros'){
            $('#ubicaciones_form ').children("#div_id_comentario").show();
        } else {
            $('#ubicaciones_form [name="comentario"]').val("");
            $('#ubicaciones_form').children("#div_id_comentario").hide();
        }
    }

});