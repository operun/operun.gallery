if (window.jQuery) {
  define('jquery', [], function() {
    return window.jQuery;
  });
}

require([
  'jquery',
  'lightbox',
  'lazyload',
], function($) {
  'use strict';

  // Custom variables

  $("img.lazy").lazyload({
      threshold: 200,
      effect: "fadeIn",
      skip_invisible: false,
  });

  $('.gallery-image').each(function() {
    $(this).delay(Math.floor(Math.random() * 1000)).animate({
      opacity: 1
    }, 250);
  });

  $('.gallery-image').hover(function() {
      $(this).find('.gallery-image-title').fadeIn('fast');
    },
    function() {
      $(".gallery-image-title").fadeOut('fast');
    });
});
