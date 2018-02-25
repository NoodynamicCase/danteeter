$(document)
  .ready(function() {

    // fix menu when passed
    $('.masthead')
      .visibility({
        once: false,
        onBottomPassed: function() {
          $('.fixed.menu').transition('fade in');
        },
        onBottomPassedReverse: function() {
          $('.fixed.menu').transition('fade out');
        }
      })
    ;

    // create sidebar and attach to menu open
    // $('.ui.sidebar')
    //   .sidebar('attach events', '.toc.item')
    // ;

    $('.ui.sidebar')
      .sidebar('toggle')
    ;

    $('.ui.dimmable')
      .dimmer('show')
    ;

    $('.special.cards .image').dimmer({
      on: 'hover'
    })
    ;

    $('.ui.card .image').dimmer({on: 'hover'});

    $('.image').dimmer({on: 'hover'});

// ACCORDIAN FOR FAQS PAGE DROWPDOWN ON ARROW CLICK
    $('.ui.accordion')
      .accordion()
    ;})

// RADIO BUTTON
    $('.ui.radio.checkbox')
  .checkbox()
    ;

// DELETE PROFILE
    function deleteItem() {
        return confirm("Confirm Delete");
    };

// AUTO FADE-IN IMAGES
    $('.sequenced.images .image')
			.transition({
				animation : 'scale',
				reverse   : 'auto', // default setting
				interval  : 200
			})
		;
    ;
