$(document).ready(function(){

  /**
   *评论按钮
   */
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
        // componentHandler.upgradeDom();
      });
    });

  /**
   *回复按钮
   */
  $('.comments-content').on('click','.reply-button', function(){

    // 生成评论header '回复 小明： '
    var postId = '' + $(this).attr('data-post-id');
    var commentInput = '#' + postId + ' ' + '.comment-input';
    var authorName = $(this).attr('data-author-name');
    var replyHeader = '回复 ' + authorName + '：  ';
    var textfield = $(commentInput).parent();
    $(commentInput).focus();

    $(commentInput).val(replyHeader);
    $(textfield).get(0).MaterialTextfield.checkDirty();
    // $(textfield).get(0).MaterialTextfield.change(replyHeader);

    // 动态生成评论内容和错误信息
    
  });

  /**
   *Emoji
   */
   $(".comment-input").emojioneArea({
      autoHideFilters: true
    });


});