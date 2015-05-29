$(document).ready(function() {

    $(".evoluciones_fotos").click(openEvolucionFotoModal);


    function openEvolucionFotoModal(ev) {
        ev.preventDefault();
        var url = $(this).data("url");
        $("#evoluciones_fotos_modal").load(url, function() { // load the url into the modal
            $("#evoluciones_fotos_modal").modal('show'); // display the modal on url load
        });
        return false;
    }


});