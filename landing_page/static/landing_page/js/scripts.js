$(document).ready(
    function(){

        //---sticky nav
        /*$('.about-section').waypoint(
            function(direction){
                if(direction  == "down"){
                    $('nav').addClass('sticky')
                }
                else{
                    $('nav').removeClass('sticky')
                } 
            }, {
                   offset: '600px'
            }
        )*/

        //---Scroll
        $('a').click(function(event){
            $('html, body').animate({
                scrollTop: $( $.attr(this, 'href') ).offset().top
            }, 500);
            event.preventDefault();
        });


        //--mobile Navigation
        $('.mobile-nav-icon').click(
            function(){                
                if($('.mobile-nav-icon').hasClass('fa-bars')){
                    $('.mobile-nav-icon').removeClass('fa-bars')
                    $('.mobile-nav-icon').addClass('fa-times')
                    $('.nav-bar').css('visibility', 'visible')
                }
                else{
                    $('.mobile-nav-icon').removeClass('fa-times')
                    $('.mobile-nav-icon').addClass('fa-bars')
                    $('.nav-bar').css('visibility', 'hidden')
                }
            }
        )
        
    }
)
