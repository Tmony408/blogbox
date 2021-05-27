setTimeout(
    function(){
        $('#message').fadeOut('slow')
    },3000
)
$(document).ready(function() {
	$('.popup-youtube').magnificPopup({
    type: 'iframe'
  });
});