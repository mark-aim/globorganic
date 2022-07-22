$(document).ready(function(){
    $('.drop-down-menu-btn').click(function(){
        $('.sub-menu').toggleClass('active');
        
        if($('.sub-menu').hasClass('active')){
            setTimeout(() => {  
                $('.sub-menu').addClass('out-of-focused'); 
            }, 500);
        }
    });
    $('body').click(function(){
            $('.out-of-focused').removeClass('active out-of-focused');
    });
})