/* **********************************************************************************

    Abri modal con la url que se pasa en el elemento <a>
    Ej:

    <a data-url="<url>" class="evoluciones_fotos_link">
        XXXX
    </a>

************************************************************************************* */
$(".evoluciones_fotos_link").click(function(ev){
            ev.preventDefault();
            var url = $(this).data("url");
            $("#evoluciones_fotos_modal").load(url, function() { // load the url into the modal
                $("#evoluciones_fotos_modal").modal('show'); // display the modal on url load
            });
            return false;
});

/* **********************************************************************************
   Link volver, dentro del pop-up
************************************************************************************* */
$(".back").click(function(ev){
    ev.preventDefault();
    var url = $(this).data("url");
    $("#evoluciones_fotos_modal").load(url, function() { // load the url into the modal
        $("#evoluciones_fotos_modal").modal('show'); // display the modal on url load
    });
    return false;
});

/* **********************************************************************************
   Submit del formulario
************************************************************************************* */
$('#foto_evoluciones_form').on('submit', function(e) {

    e.preventDefault();

    var formData = new FormData($(this)[0]);

    $.ajax({
        type: $(this).attr('method'),
        url: this.action,
        data: formData,
        processData: false,
        contentType: false,
        type: 'POST',
        async: false,
        cache: false,
        success: function(data, status) {
            $("#evoluciones_fotos_modal").html( data )
        }
    });

    return false;

});