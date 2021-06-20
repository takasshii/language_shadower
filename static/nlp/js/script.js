$(function() {
    //右上のメニューバーの操作
    $("a[href*=#]").click(function(){
        $('html,body').animate({scrollTop: $($(this).attr("href")).offset().top-70},'slow','swing');
        return false;
})


$(window).load(function() {
        
    var ahash = location.hash;
        
    var gotoNum = $(ahash).offset().top;
        
    $('html,body').animate({ scrollTop: gotoNum }, 0 );
        
    return false;
        
});

/*
$('#js-openC').click(function(){
    $('form').submit(function(event) {
        event.preventDefault();
        $.post('/',$(form).serialize())
        .done(function(data){
            console.log(data.from);
        })
        $('#modal01').fadeIn();
    })  
    return false;
});
*/
/*
$('.close-modal').click(function(){
    $('#modal01').fadeOut();
    window.location.href = "/";
});

$('#js-openE').click(function(){
    ('form').submit(function(event) {
        event.preventDefault();
        $.post('/',$(form).serialize())
        .done(function(data){
            console.log(data.from);
        })
    $('#modal02').fadeIn();
    })  
    return false;
});

$('.close-modal').click(function(){
    $('#modal02').fadeOut();
    window.location.href = "/";
});
*/
});