if (window.jQuery) {
  define('jquery', [], function() {
    return window.jQuery;
  });
}

require([
  'jquery',
  'lightbox',
], function($) {
  'use strict';

  // Custom variables
<<<<<<< HEAD
  
=======

>>>>>>> 752877b1d801612ea7283ee17507ce4fd1d2db1d
  $('.gallery-image').each(function() {
    $(this).delay(Math.floor(Math.random() * 1000)).animate({opacity: 1}, 250);
  });

  $('.gallery-image').hover(function() {
      $(this).find('.gallery-image-title').fadeIn('fast');
    },
    function() {
      $(".gallery-image-title").fadeOut('fast');
    });
});
