

// Sticky navbar
// =========================
            $(document).ready(function () {
                // Custom function which toggles between sticky class (is-sticky)
                var stickyToggle = function (sticky, stickyWrapper, scrollElement) {
                    var stickyHeight = sticky.outerHeight();
                    var stickyTop = stickyWrapper.offset().top;
                    if (scrollElement.scrollTop() >= stickyTop) {
                        stickyWrapper.height(stickyHeight);
                        sticky.addClass("is-sticky");
                    }
                    else {
                        sticky.removeClass("is-sticky");
                        stickyWrapper.height('auto');
                    }
                };

                // Find all data-toggle="sticky-onscroll" elements
                $('[data-toggle="sticky-onscroll"]').each(function () {
                    var sticky = $(this);
                    var stickyWrapper = $('<div>').addClass('sticky-wrapper'); // insert hidden element to maintain actual top offset on page
                    sticky.before(stickyWrapper);
                    sticky.addClass('sticky');

                    // Scroll & resize events
                    $(window).on('scroll.sticky-onscroll resize.sticky-onscroll', function () {
                        stickyToggle(sticky, stickyWrapper, $(this));
                    });

                    // On page load
                    stickyToggle(sticky, stickyWrapper, $(window));
                });
            //owl carosel initialization
             $(".owl-carousel").owlCarousel(
                    {
                        autoplay:false,
                        items:6,
                        stagePadding: 10,
                        dots: false,
                        loop:true,
                        responsiveClass: true,
                        navText : ["<i class='fas fa-chevron-left' aria-hidden='true'></i>","<i class='fas fa-chevron-right' aria-hidden='true'></i>"],
                        responsive: {
                    0:{
                        items: 2,
                        nav: true,
                        dots: false,
                        margin: 2,
                        stagePadding: 0,
                    },
                    600:{
                        items: 4,
                        nav: true,
                        dots: false,
                        margin: 25
                    },
                    768: {
                        items: 6,
                        nav: true,
                        dots: false,
                        margin: 25
                    }
                }
                    }
                );
             
             $(".next").click(function(){
    owl.trigger('owl.next');
  })
  $(".prev").click(function(){
    owl.trigger('owl.prev');
  })

            });
