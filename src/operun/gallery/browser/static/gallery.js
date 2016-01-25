if (window.jQuery) {
  define('jquery', [], function() {
    return window.jQuery;
  });
}

require([
  'jquery',
  'hoverintent',
  'lightbox',
], function($) {
  'use strict';

  // Custom variables
  $(document).ready(function() {
    $('.gallery-image').each(function() {
      $(this).delay(Math.floor(Math.random() * 1000)).animate({
        opacity: 1
      }, 250);
    });
    $(".gradient-overlay").css({
      'height': ($(".gallery-image").height() + 'px')
    });
    $('.gallery-image').hoverIntent(function() {
        $(this).find('.title-container').fadeIn(100);
      },
      function() {
        $(".title-container").delay(100).fadeOut(100);
      });
  });
});
