$(document).ready(function(){

  $('.comment-button').click(function(){
      // if($(this).hasClass('active')){
      //     $(this).removeClass('active');   
      // }else{
      //     $(this).addClass('active');            
      // }

      // 生成评论框
      var thisCommentsDiv = $(this).parent().parent().parent().find('.comments-div');
      thisCommentsDiv.slideToggle('fast'); 

      // 动态生成评论内容
      var data_post_id = $(this).attr('data-post-id');
      $.get('/comments/get_comments/',
        {post_id: data_post_id},
        function(data){
          thisCommentsDiv.find('.comments-content').html(data);
        });
    });

});