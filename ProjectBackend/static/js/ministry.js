$(document).ready(function() {
  $('#display-add-event-modal').click(function () {
    $('input[name=date]').val("");
    //$('input[name=time]').val("");
    $('input[name=title]').val("");
    $('input[name=description]').val("");    
	$('input[name=entity_key]').val("").prop("disabled", true);
    $('#add-event-modal').modal('show');});
  $('#display-add-announcement-modal').click(function () {
	$('input[name=title]').val("");
	$('input[name=description]').val("");    
	$('#add-announcement-modal').modal('show');
	  });
  
  $(".edit-event").click(function() {
		$("#add-event-modal .modal-title").html("Edit this Event");
		$("#add-event-modal button[type=submit]").html("Edit Event");
		
		date = $(this).find(".date").html();
		$("#add-event-modal input[name=date]").val(date);
		//time = $(this).find(".time").html();
		//$("#add-event-modal input[name=time]").val(time);
		title = $(this).find(".title").html();
		$("#add-event-modal input[name=title]").val(title);
		description = $(this).find(".description").html();
		$("#add-event-modal input[name=description]").val(description);
		entityKey = $(this).find(".entity_key").html();
		$("#add-event-modal input[name=entity_key]").val(entityKey).prop("disabled", false);
	});

	$(".delete-event").click(function() {		
		entityKey = $(this).find(".entity_key").html();
		$("#delete-event-modal input[name=entity_key]").val(entityKey).prop("disabled", false);
	});
	
	$(".edit-announcement").click(function() {
		$("#add-announcement-modal .modal-title").html("Edit this Announcement");
		$("#add-announcement-modal button[type=submit]").html("Edit Announcement");
		
		title = $(this).find(".title").html();
		$("#add-announcement-modal input[name=title]").val(title);
		description = $(this).find(".description").html();
		$("#add-announcement-modal input[name=description]").val(description);
		entityKey = $(this).find(".entity_key").html();
		$("#add-announcement-modal input[name=entity_key]").val(entityKey).prop("disabled", false);
	});

	$(".delete-announcement").click(function() {		
		entityKey = $(this).find(".entity_key").html();
		$("#delete-announcement-modal input[name=entity_key]").val(entityKey).prop("disabled", false);
	});


  $('.pin').click(function(){

  });
  rh.mq.enableButtons();

});

//Make a company.project namespace
var rh = rh || {};
rh.mq = rh.mq || {};
// My global variable is now restricted and shouldn't collide.
rh.mq.editing = false;

rh.mq.enableButtons = function() {
	$("#toggle-edit").click(function() {
		if (rh.mq.editing) {
			rh.mq.editing = false;
			$(".edit-actions").addClass("hidden");
			$(this).html("Edit");
		} else {
			rh.mq.editing = true;
			$(".edit-actions").removeClass("hidden");
			$(this).html("Done");
		}
		rh.mq.hideNavbar();
	})};