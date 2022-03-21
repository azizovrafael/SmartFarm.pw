(function ($) {
    "use strict";
  
    if ($(".scroll-to-target").length) {
      $(".scroll-to-target").on("click", function (e) {
        e.preventDefault();
        var target = $(this).attr("data-target");
        // animate
        $("html, body").animate({
            scrollTop: $(target).offset().top,
          },
          1000
        );
      });
    }
  
    if ($(".contact-form-validated").length) {
      $(".contact-form-validated").validate({
        // initialize the plugin
        rules: {
          name: {
            required: true,
          },
          email: {
            required: true,
            email: true,
          },
          message: {
            required: true,
          },
          subject: {
            required: true,
          },
        },
        submitHandler: function (form) {
          // sending value with ajax request
          $.post(
            $(form).attr("action"),
            $(form).serialize(),
            function (response) {
              $(form).parent().find(".result").append(response);
              $(form).find('input[type="text"]').val("");
              $(form).find('input[type="email"]').val("");
              $(form).find("textarea").val("");
            }
          );
          return false;
        },
      });
    }

    function dynamicCurrentMenuClass(selector) {
      let FileName = window.location.href.split("/").reverse()[0];
  
      selector.find("li").each(function () {
        let anchor = $(this).find("a");
        if ($(anchor).attr("href") == FileName) {
          $(this).addClass("current");
        }
      });
      // if any li has .current elmnt add class
      selector.children("li").each(function () {
        if ($(this).find(".current").length) {
          $(this).addClass("current");
        }
      });
      // if no file name return
      if ("" == FileName) {
        selector.find("li").eq(0).addClass("current");
      }
    }
  
    if ($(".main-menu__list").length) {
      // dynamic current class
      let mainNavUL = $(".main-menu__list");
      dynamicCurrentMenuClass(mainNavUL);
    }
  
    if ($(".services-details__sidebar-single-services ul").length) {
      // dynamic current class
      let mainNavUL = $(".services-details__sidebar-single-services ul");
      dynamicCurrentMenuClass(mainNavUL);
    }
  
  
    if ($(".main-menu__list").length && $(".mobile-nav__container").length) {
      let navContent = document.querySelector(".main-menu__list").outerHTML;
      let mobileNavContainer = document.querySelector(".mobile-nav__container");
      mobileNavContainer.innerHTML = navContent;
    }
  
  
  
    if ($(".sticky-header__content").length) {
      let navContent = document.querySelector(".main-menu").innerHTML;
      let mobileNavContainer = document.querySelector(".sticky-header__content");
      mobileNavContainer.innerHTML = navContent;
    }
  
    if ($(".mobile-nav__toggler").length) {
      $(".mobile-nav__toggler").on("click", function (e) {
        e.preventDefault();
        $(".mobile-nav__wrapper").toggleClass("expanded");
        $("body").toggleClass("locked");
      });
    }

    // window scroll event
  
    $(window).on("scroll", function () {
      if ($(".stricked-menu").length) {
        var headerScrollPos = 130;
        var stricky = $(".stricked-menu");
        if ($(window).scrollTop() > headerScrollPos) {
          stricky.addClass("stricky-fixed");
        } else if ($(this).scrollTop() <= headerScrollPos) {
          stricky.removeClass("stricky-fixed");
        }
      }
      if ($(".scroll-to-top").length) {
        var strickyScrollPos = 100;
        if ($(window).scrollTop() > strickyScrollPos) {
          $(".scroll-to-top").fadeIn(500);
        } else if ($(this).scrollTop() <= strickyScrollPos) {
          $(".scroll-to-top").fadeOut(500);
        }
      }
    });
  
  })(jQuery);