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

     /* --------------------------------------------------------------------------------------------
     -- Rellenar el text area de enfermedad trayendo la descripcion de -----------------------------
     -- un motivo deconsulta           -------------------------------------------------------------
     -----------------------------------------------------------------------------------------------*/
    $("#id_anamnesis-motivo_consulta").on('change', traer_enfermedad);
    function traer_enfermedad() {
        $.ajax({
		data: { 'pk': $(this).val() },
		url: '/motivos/traer/enfermedad/',
		type: 'GET',
		success: function(data){
                       $("#id_anamnesis-enfermedad_actual").val("");
			$("#id_anamnesis-enfermedad_actual").val( data[0].fields.descripcion );
		}
	});
    }

    /* ------------------------------------------
        Escribir en la solapa de 'Planteos' el
        cotenido de diagnostico
    -------------------------------------------- */
    $('#id_diagnostico-descripcion').on('blur', copiar_diagnostico);
    function copiar_diagnostico(){
        diagnostico = 'Diagnóstico: ' + $("#id_diagnostico-tipo_diagnostico option:selected").text();
        $("#id_planteos-planteo").val( diagnostico +'\n'+ $(this).val() );
    }

});
