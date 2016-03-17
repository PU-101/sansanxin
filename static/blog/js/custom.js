$(document).ready(function(){
      // $('.ui.accordion').accordion();
      // $('.menu .item').tab();
      $('.pointing.secondary.menu .item').click(function(){
            if($(this).hasClass('active')){
                // $("#comments-div").addClass('hidden-div');
                $(this).removeClass('active');   
            }else{
                $(this).addClass('active');
                // $("#comments-div").removeClass('hidden-div');               
            }
            var thisCommentsDiv = $(this).parent().parent().find('.comments-div');
            thisCommentsDiv.toggle('fast'); 
        });

      // fix main menu to page on passing
      $('.navbar.menu').visibility({
        type: 'fixed'
      });

      // lazy load images
      $('.image').visibility({
        type: 'image',
        transition: 'vertical flip in',
        duration: 500
      });

      // show dropdown on hover
      $('.navbar.menu  .ui.dropdown').dropdown({
        on: 'hover'
      });

});