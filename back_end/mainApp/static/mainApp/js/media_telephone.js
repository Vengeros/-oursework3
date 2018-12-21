$(document).ready(function() {
  var width = $(window).width();

  $('a.logo').on('click', function() {
    if(width < 625) {
      $('.links').toggleClass('flex');
    } else {
      $('.links').removeClass('flex');
    }
  });

  $(window).on('load resize', function(e) {
    width = $(window).width();
    if(width < 625) {
      $('a.logo').attr('href', '#');
    }
    else {
      $('a.logo').attr('href', '/');
      $('.links').toggleClass('flex');
    }
  })

  $('.section').on('click',function(){
    $
    $('.hiden-part').toggle()
  })

});
