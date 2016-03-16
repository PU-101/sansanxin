$(document).ready(function(){
      $('.ui.accordion').accordion();
      // $('.menu .item').tab();
      $('.menu .item').click(function(){
            if($(this).hasClass('active')){
                // $("#comments-div").addClass('hidden-div');
                $(this).removeClass('active');   
            }else{
                $(this).addClass('active');
                // $("#comments-div").removeClass('hidden-div');               
            }
            $("#comments-div").toggle('fast'); 
        });

});