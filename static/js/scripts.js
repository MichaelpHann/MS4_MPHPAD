$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.dropdown-button').dropdown();
    $('.materialboxed').materialbox();
    $('.parallax').parallax();
    $('.tabs').tabs();
    $('.scrollspy').scrollSpy();
    $('.slider').slider({
        indicators: false,
        height: 600,
        transition: 500,
        interval: 6000
    });
});