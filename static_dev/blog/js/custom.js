$(document).ready(function(){

  // $(".body-container").height($(window).height());


  /**
   *Dropdown
   */
   $(".dropdown-button").dropdown({
    inDuration: 300,
    outDuration: 225,
    constrain_width: false, // Does not change width of dropdown to that of the activator
    hover: true, // Activate on hover
    gutter: 0, // Spacing from edge
    belowOrigin: false // Displays dropdown below the button
    }
  );

   $('select').material_select();

   $('.destination-card').captionHover({
      fx: 'roxy'
    });

   $('.modal-trigger').leanModal();


   /**
    *图像裁剪
    */
  $('.image-editor').cropit();

  $('#portrait .modal-footer .btn').click(function(){
    // Move cropped image data to hidden input
    var imageData = $('.image-editor').cropit('export');

    $.post('/portrait/set_portrait/',
      {image_data: imageData},
      function(data){
          $('.profile-card .card-protrait_image img').attr('src', data);
      });
  });


  /**
   *评论按钮
   */
  $('.comment-button').click(function(){
    
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

    // 动态生成评论内容和错误信息
    
  });

  $('.comments-content').on('click','.cancel-button', function(){
    var comment_id = $(this).attr('data-comment-id');
    var post_id = $(this).attr('data-post-id');
    var this_comment_div = $(this).parent().parent().parent()

    $.get('/comments/delete_comment/',
      {comment_id: comment_id,
        post_id: post_id},
      function(data){
          $(this_comment_div).fadeOut();
          var comment_button = $("a[class*='comment-button'][data-post-id="+post_id+"]");
          comment_button.find('span').text(data);
          if (data==0) {
            comment_button.removeClass('pink');
            comment_button.addClass('grey');
          };
      });
    
  });


  /**
   *Like按钮
   */
   $('.like-button').click(function(){
      var like_button = $(this)
      var post_id = $(this).attr('data-post-id');
      var user_id = $(this).attr('data-user-id');

      $.get('/posts/like_post/',

        {post_id: post_id,
          user_id: user_id},

        function(data){
          $(like_button).find('span').html(data);
    
          $(like_button).toggleClass("grey");
        });
   });


   /**
   *关注按钮/取消关注按钮
   */
   $('.follow-btn').click(function(){
    var follow_button = $(this)
    var user2_id = $(this).attr('data-ip-id');

      $.get('/follow/',

        {user2_id: user2_id},

        function(data){
          $(follow_button).text(data)
          $(follow_button).toggleClass("grey");
        });
   });

});