(function ($) {
  $(document).ready(function () {

     // sticky header active
     if ($("#header").length > 0) {
      $(window).on("scroll", function (event) {
        var scroll = $(window).scrollTop();
        if (scroll < 1) {
          $("#header").removeClass("sticky");
        } else {
          $("#header").addClass("sticky");
        }
      });
    }

        // pricing-plan-tab
        $("#ce-toggle").click(function (event) {
          $(".plan-toggle-wrap").toggleClass("active");
        });
    
        $("#ce-toggle").change(function () {
          if ($(this).is(":checked")) {
            $(".tab-content #yearly").hide();
            $(".tab-content #monthly").show();
          } else {
            $(".tab-content #yearly").show();
            $(".tab-content #monthly").hide();
          }
        });


                //testimonial 1
                $(".tes1-big-slider").slick({
                  slidesToShow: 1,
                  slidesToScroll: 1,
                  arrows: true,
                  loop: true,
                  focusOnSelect: true,
                  asNavFor: ".tes1-big-slider",
                  prevArrow: $(".testimonial-prev-arrow"),
                  nextArrow: $(".testimonial-next-arrow"),
                  rtl: true,
                  responsive: [
                    {
                      breakpoint: 769,
                      settings: {
                        arrows: false,
                        centerMode: true,
                        centerPadding: "40px",
                        slidesToShow: 1,
                      },
                    },
                    {
                      breakpoint: 480,
                      settings: {
                        arrows: false,
                        centerMode: true,
                        centerPadding: "40px",
                        slidesToShow: 1,
                      },
                    },
                  ],
                });

                $(".tes1-brads-slider").slick({
                  slidesToShow: 5,
                  slidesToScroll: 1,
                  arrows: true,
                  loop: true,
                  focusOnSelect: true,
                  asNavFor: ".tes1-big-slider",
                  prevArrow: $(".testimonial-prev-arrow"),
                  nextArrow: $(".testimonial-next-arrow"),
                  rtl: true,
                  responsive: [
                    {
                      breakpoint: 769,
                      settings: {
                        arrows: false,
                        centerMode: true,
                        centerPadding: "40px",
                        slidesToShow: 3,
                      },
                    },
                    {
                      breakpoint: 480,
                      settings: {
                        arrows: false,
                        centerMode: true,
                        centerPadding: "40px",
                        slidesToShow: 2,
                      },
                    },
                  ],

                });



                $(".tes2-slider-all").slick({
                  slidesToShow: 2,
                  margin: 30,
                  slidesToScroll: 1,
                  dots: true,
                  arrows: true,
                  loop: true,
                  centerPadding: "40px",
                  prevArrow: $(".testimonial-prev-arrow2"),
                  nextArrow: $(".testimonial-next-arrow2"),
                  rtl: true,
                  responsive: [
                    {
                      breakpoint: 769,
                      settings: {
                        arrows: false,
                        centerMode: true,
                        centerPadding: "40px",
                        slidesToShow: 1,
                      },
                    },
                    {
                      breakpoint: 480,
                      settings: {
                        arrows: false,
                        centerMode: true,
                        centerPadding: "40px",
                        slidesToShow: 1,
                      },
                    },
                  ],

                });

                $(".tes2-slider-all-ltr").slick({
                  slidesToShow: 2,
                  margin: 30,
                  slidesToScroll: 1,
                  dots: true,
                  arrows: true,
                  loop: true,
                  centerPadding: "40px",
                  prevArrow: $(".testimonial-prev-arrow2"),
                  nextArrow: $(".testimonial-next-arrow2"),

                  responsive: [
                    {
                      breakpoint: 769,
                      settings: {
                        arrows: false,
                        centerMode: true,
                        centerPadding: "40px",
                        slidesToShow: 1,
                      },
                    },
                    {
                      breakpoint: 480,
                      settings: {
                        arrows: false,
                        centerMode: true,
                        centerPadding: "40px",
                        slidesToShow: 1,
                      },
                    },
                  ],

                });

                $(".tes4-logo-slider1").slick({
                  slidesToShow: 5,
                  margin: 30,
                  slidesToScroll: 1,
                  dots: false,
                  arrows: false,
                  loop: true,
                  centerPadding: "40px",
                  autoplay: true,
                  autoplaySpeed: 1000,
                  speed: 2000,
                  cssEase: 'linear',
                  rtl: true,
                  responsive: [
                    {
                      breakpoint: 769,
                      settings: {
                        arrows: false,
                        centerMode: true,
                        centerPadding: "40px",
                        slidesToShow: 3,
                      },
                    },
                    {
                      breakpoint: 480,
                      settings: {
                        arrows: false,
                        centerMode: true,
                        centerPadding: "40px",
                        slidesToShow: 2,
                      },
                    },
                  ],

                });

                $(".tes4-logo-slider2").slick({
                  slidesToShow: 5,
                  margin: 30,
                  slidesToScroll: 1,
                  dots: false,
                  arrows: false,
                  loop: true,
                  centerPadding: "40px",
                  autoplay: true,
                  autoplaySpeed: 1000,
                  speed: 1000,
                  cssEase: 'linear',

                  responsive: [
                    {
                      breakpoint: 769,
                      settings: {
                        arrows: false,
                        centerMode: true,
                        centerPadding: "40px",
                        slidesToShow: 3,
                      },
                    },
                    {
                      breakpoint: 480,
                      settings: {
                        arrows: false,
                        centerMode: true,
                        centerPadding: "40px",
                        slidesToShow: 2,
                      },
                    },
                  ],

                });

                $(".hero5-slider-all").slick({
                  slidesToShow: 5,
                  margin: 30,
                  slidesToScroll: 1,
                  dots: false,
                  arrows: false,
                  loop: true,
                  centerPadding: "40px",
                  autoplay: true,
                  autoplaySpeed: 1000,
                  speed: 1000,
                  cssEase: 'linear',
                  rtl: true,
                  responsive: [
                    {
                      breakpoint: 769,
                      settings: {
                        arrows: false,
                        centerMode: true,
                        centerPadding: "40px",
                        slidesToShow: 2,
                      },
                    },
                    {
                      breakpoint: 480,
                      settings: {
                        arrows: false,
                        centerMode: true,
                        centerPadding: "40px",
                        slidesToShow: 1,
                      },
                    },
                  ],

                });


                $('.js-tilt').tilt({
                  
                });


                //testimonial 4
                $(".tes4-big-slider").slick({
                  margin: "30",
                  slidesToShow: 1,
                  arrows: true,
                  centerMode: false,
                  loop: true,
                  centerMode: false,
                  prevArrow: $(".testimonial-prev-arrow"),
                  nextArrow: $(".testimonial-next-arrow"),
                  draggable: true,
                  fade: false,
                  rtl: true,
                  responsive: [
                    {
                      breakpoint: 769,
                      settings: {
                        arrows: false,
                        centerMode: false,
                        centerPadding: "40px",
                        slidesToShow: 1,
                      },
                    },
                    {
                      breakpoint: 480,
                      settings: {
                        arrows: false,
                        centerMode: false,
                        centerPadding: "40px",
                        slidesToShow: 1,
                      },
                    },
                  ],
                });

                 //testimonial 7
                 $(".tes7-slider").slick({
                  margin: "30",
                  slidesToShow: 1,
                  arrows: true,
                  centerMode: false,
                  loop: true,
                  centerMode: false,
                  prevArrow: $(".testimonial7-prev-arrow"),
                  nextArrow: $(".testimonial7-next-arrow"),
                  draggable: true,
                  fade: false,
                  rtl: true,
                  responsive: [
                    {
                      breakpoint: 769,
                      settings: {
                        arrows: false,
                        centerMode: false,
                        centerPadding: "40px",
                        slidesToShow: 1,
                      },
                    },
                    {
                      breakpoint: 480,
                      settings: {
                        arrows: false,
                        centerMode: false,
                        centerPadding: "40px",
                        slidesToShow: 1,
                      },
                    },
                  ],
                });


  //Aos animation active

    AOS.init({
      offset: 100,
      duration: 400,
      easing: "ease-in-out",
      anchorPlacement: "top-bottom",
      disable: "mobile",
    });


    //Video poppup
    if ($(".play-btn").length > 0) {
      $(".play-btn").magnificPopup({
        type: "iframe",
      });
    }



        // page-progress
        var progressPath = document.querySelector(".progress-wrap path");
        var pathLength = progressPath.getTotalLength();
        progressPath.style.transition = progressPath.style.WebkitTransition =
          "none";
        progressPath.style.strokeDasharray = pathLength + " " + pathLength;
        progressPath.style.strokeDashoffset = pathLength;
        progressPath.getBoundingClientRect();
        progressPath.style.transition = progressPath.style.WebkitTransition =
          "stroke-dashoffset 10ms linear";
        var updateProgress = function () {
          var scroll = $(window).scrollTop();
          var height = $(document).height() - $(window).height();
          var progress = pathLength - (scroll * pathLength) / height;
          progressPath.style.strokeDashoffset = progress;
        };
        updateProgress();
        $(window).scroll(updateProgress);
        var offset = 50;
        var duration = 550;
        jQuery(window).on("scroll", function () {
          if (jQuery(this).scrollTop() > offset) {
            jQuery(".progress-wrap").addClass("active-progress");
          } else {
            jQuery(".progress-wrap").removeClass("active-progress");
          }
        });
        jQuery(".progress-wrap").on("click", function (event) {
          event.preventDefault();
          jQuery("html, body").animate({ scrollTop: 0 }, duration);
          return false;
        });
        



    //product colors
    const colors = $(".accordion1 .accordion-item");

    colors.on("click", function () {
      $(".accordion1 .accordion-item").removeClass("active");
      $(this).addClass("active");
    });


  });


    //preloader
    $(window).on("load", function (event) {
      setTimeout(function () {
        $(".preloader-parent").fadeToggle();
      }, 500);
    });

        	/* Text Effect Animation */
          if ($('.text-anime-style-1').length) {
            let staggerAmount = 0.05,
                delayValue    = 0.5,
                animatedTextElements = document.querySelectorAll('.text-anime-style-1');
          
            animatedTextElements.forEach((element) => {
              if (element.animation) {
                element.animation.progress(1).kill();
                if (element.split && typeof element.split.revert === 'function') {
                  element.split.revert();
                }
              }
          
              element.split = new SplitText(element, {
                type: "lines,words",
                linesClass: "split-line",
                wordsClass: "split-word"
              });
          
              let targets = element.split.words?.length ? element.split.words : element.split.lines;
          
              targets.forEach(t => {
                t.style.display = "inline-block";
                t.style.whiteSpace = "nowrap";
              });
          
              gsap.set(targets, { opacity: 0, y: "90%", rotateX: "-40deg" });
          
              element.animation = gsap.to(targets, {
                scrollTrigger: { trigger: element, start: "top 85%" },
                y: "0",
                rotateX: "0",
                opacity: 1,
                duration: 1,
                ease: "back.out(1.7)",
                stagger: staggerAmount
              });
            });
          }
          
          if ($('.text-anime-style-2').length) {
            let staggerAmount = 0.05,
                delayValue    = 0.5,
                easeType      = "power2.out",
                animatedTextElements = document.querySelectorAll('.text-anime-style-2');
          
            animatedTextElements.forEach((element) => {
              if (element.animation) {
                element.animation.progress(1).kill();
                if (element.split && typeof element.split.revert === 'function') {
                  element.split.revert();
                }
              }
          
              element.split = new SplitText(element, {
                type: "lines,words",
                linesClass: "split-line",
                wordsClass: "split-word"
              });
          
              let targets = element.split.words?.length ? element.split.words : element.split.lines;
          
              targets.forEach(t => {
                t.style.display = "inline-block";
                t.style.whiteSpace = "nowrap";
              });
          
              gsap.set(targets, { opacity: 0, x: 50 });
          
              element.animation = gsap.to(targets, {
                scrollTrigger: { trigger: element, start: "top 85%" },
                x: "0",
                opacity: 1,
                duration: 1,
                ease: easeType,
                stagger: staggerAmount
              });
            });
          }
          
          if ($('.text-anime-style-3').length) {
            let animatedTextElements = document.querySelectorAll('.text-anime-style-3');
          
            animatedTextElements.forEach((element) => {
              if (element.animation) {
                element.animation.progress(1).kill();
                if (element.split && typeof element.split.revert === 'function') {
                  element.split.revert();
                }
              }
          
              element.split = new SplitText(element, {
                type: "lines,words",
                linesClass: "split-line",
                wordsClass: "split-word"
              });
          
              let targets = element.split.words?.length ? element.split.words : element.split.lines;
          
              targets.forEach(t => {
                t.style.display = "inline-block";
                t.style.whiteSpace = "nowrap";
              });
          
              gsap.set(targets, { opacity: 0, x: 50 });
          
              element.animation = gsap.to(targets, {
                scrollTrigger: { trigger: element, start: "top 95%" },
                x: "0",
                y: "0",
                rotateX: "0",
                opacity: 1,
                duration: 1,
                ease: "back.out(1.7)",
                stagger: 0.02
              });
            });
          }          

})(jQuery);


const rippleBtns = document.getElementsByClassName("ripple");
  
function createRipple(event) {
  // Create the ripple span element
  let ripples = document.createElement("span");
  
  // Calculate the position relative to the button element
  let x = event.clientX - event.target.getBoundingClientRect().left;
  let y = event.clientY - event.target.getBoundingClientRect().top;
  
  // Set the position of the ripple within the button element
  ripples.style.left = x + "px";
  ripples.style.top = y + "px";
  
  // Append the ripple to the button
  event.target.appendChild(ripples);
  
  // Set a timeout to remove the ripple after 1000 milliseconds
  let clearTimeoutHandle = setTimeout(() => {
    ripples.remove();
  }, 1000);

  // Remove the ripple immediately if the mouse leaves the button
  event.target.addEventListener("mouseout", function () {
    clearTimeout(clearTimeoutHandle);
    ripples.remove();
  });
}

// Attach the createRipple function to each button
for (let i = 0; i < rippleBtns.length; i++) {
  const rippleBtn = rippleBtns[i];
  rippleBtn.addEventListener("mouseover", createRipple);
}
