$(document).ready(function() {
    $("#loader").fadeOut(
        1000, function(){$(this).fadeIn(
            1000, function(){$(this).fadeOut(
                1000,function(){$(".board").show()}
            )})});
})