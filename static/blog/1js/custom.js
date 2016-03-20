$(document).ready(function(){
      // $('.ui.accordion').accordion();
      // $('.menu .item').tab();

      $('.comment-menu .item').click(function(){
          if($(this).hasClass('active')){
              $(this).removeClass('active');   
          }else{
              $(this).addClass('active');            
          }

          // 生成评论框
          var thisCommentsDiv = $(this).parent().parent().find('.comments-div');
          thisCommentsDiv.toggle('fast'); 

          // 动态生成评论内容
          var data_post_id = $(this).attr('data-post-id');
          $.get('/comments/get_comments/',
            {post_id: data_post_id},
            function(data){
              thisCommentsDiv.find('.comments').html(data);
            });
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