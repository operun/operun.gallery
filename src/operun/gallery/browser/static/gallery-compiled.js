window.jQuery&&define("jquery",[],function(){return window.jQuery}),require(["jquery"],function(a){"use strict";a(".gallery-image").each(function(){a(this).delay(Math.floor(1e3*Math.random())).animate({opacity:1},250)}),a(".gallery-image").hover(function(){a(this).find(".gallery-image-title").fadeIn("fast")},function(){a(".gallery-image-title").fadeOut("fast")})}),define("/home/jesse/Development/operun/operun.gallery/src/operun/gallery/browser/static/gallery.js",function(){});
//# sourceMappingURL=gallery-compiled.js.map