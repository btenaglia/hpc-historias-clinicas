$(document).ready(function() { 


    /* --------------------------------------------
        Lanzar modal para crear historia clinica
    --------------------------------------------- */
    $('#nueva_historia').click(function(){
        $("#nueva_historia_modal").modal("show");
    });


    /* --------------------------
        Abrir pop-over con info
        del paciente
    ----------------------------- */
    $('.popover_info_paciente').popover({
        animation: true,
        html: true
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
    $('#id_diagnostico-tipo_diagnostico').on('blur', copiar_diagnostico);
    function copiar_diagnostico(){
        diagnostico = $("#id_diagnostico-tipo_diagnostico option:selected").text();
        $("#id_planteos-planteo").val( diagnostico  );
    }


    /* ----------------------------------------
        Impresion historias clinicas
        - grupo de páginas (1, 3, 5 y 7)
    ------------------------------------------- */
    $('#grp1').click(function(e){
        e.preventDefault();
        $('#historia_clinica_p1')[0].click();
        $('#historia_clinica_p3')[0].click();
        $('#historia_clinica_p5')[0].click();
        $('#historia_clinica_p7')[0].click();
    });

    /* ----------------------------------------
        Impresion historias clinicas
        - grupo de páginas (4 y 6)
    ------------------------------------------- */
    $('#grp2').click(function(e){
        e.preventDefault();
        $('#historia_clinica_p4')[0].click();
        $('#historia_clinica_p6')[0].click();
    });



});