$(document).ready(function(){

    $('.ir-arriba').click(function(){
        $('body, html').animate({
            scrollTop: '0px'
        }, 300);
    });

    $(window).scroll(function(){
    	if($(this).scrollTop() > 0){
    	   $('.ir-arriba').slideDown(300);
    	} else {
    	   $('.ir-arriba').slideUp(300);
    	}
    });
});

function boton(){
	window.location="home";

};

function contacto(){
	window.location="contacto";

};