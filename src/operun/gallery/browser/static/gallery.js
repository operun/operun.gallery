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
  $('.gallery-image').each(function() {
    $(this).delay(Math.floor(Math.random() * 1000)).animate({
      opacity: 1
    }, 250);
  });
  $(window).on("load resize", function() {
    $(".gradient-overlay").css({
      'height': ($(".gallery-image").height() + 'px')
    });
  });
  $('.gallery-image').hover(function() {
      $(this).find('.title-container').fadeIn(100);
    },
    function() {
      $(".title-container").fadeOut(80);
    });});
