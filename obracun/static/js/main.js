$(document).ready(function() {
	$('.form-select').select2({
		width: '100%'
	});
	$("#backBtn").click(function(event) {
	    event.preventDefault();
	    history.back(1);
	});
});