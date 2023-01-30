	
//=== Switcher panal slide function	=====================//

	jQuery(window).load(function(){
		jQuery('.styleswitcher').animate({
					'left': '-170px'
				});
		jQuery('.switch-btn').addClass('closed');
	});
	
	jQuery(document).ready(function () {		
		jQuery('.switch-btn').on('click', function () {	
			if (jQuery(this).hasClass('open')) {
				jQuery(this).addClass('closed');
				jQuery(this).removeClass('open');
				jQuery('.styleswitcher').animate({
					'left': '-170px'
				});
			} else {
				if (jQuery(this).hasClass('closed')) {
				jQuery(this).addClass('open');
				jQuery(this).removeClass('closed');
				jQuery('.styleswitcher').animate({
					'left': '0'
				});
				}
			}	
		});
	});
	
//=== Switcher panal slide function END	=====================//


//=== Color css change function	=====================//

jQuery( document ).ready(function() {
	
    // Color changer
    jQuery(".skin-1").on('click', function(){
        jQuery(".skin").attr("href", "css/skin/skin-1.css");
		jQuery(".logo-header img").attr("src", "images/logo-1.png");
		jQuery(".footer-light .logo-footer img").attr("src", "images/logo-l-1.png");
		jQuery(".footer-dark .logo-footer img").attr("src", "images/logo-1.png");
        return false;
    });
    
    jQuery(".skin-2").on('click', function(){
        jQuery(".skin").attr("href", "css/skin/skin-2.css");
		jQuery(".logo-header img").attr("src", "images/logo-2.png");
		jQuery(".footer-light .logo-footer img").attr("src", "images/logo-l-2.png");
		jQuery(".footer-dark .logo-footer img").attr("src", "images/logo-2.png");
        return false;
    });
    
    jQuery(".skin-3").on('click', function(){
        jQuery(".skin").attr("href", "css/skin/skin-3.css");
		jQuery(".logo-header img").attr("src", "images/logo-3.png");
		jQuery(".footer-light .logo-footer img").attr("src", "images/logo-l-3.png");
		jQuery(".footer-dark .logo-footer img").attr("src", "images/logo-3.png");
        return false;
    });
	
    jQuery(".skin-4").on('click', function(){
        jQuery(".skin").attr("href", "css/skin/skin-4.css");
		jQuery(".logo-header img").attr("src", "images/logo-4.png");
		jQuery(".footer-light .logo-footer img").attr("src", "images/logo-l-4.png");
		jQuery(".footer-dark .logo-footer img").attr("src", "images/logo-4.png");
        return false;
    });
	
    jQuery(".skin-5").on('click', function(){
        jQuery(".skin").attr("href", "css/skin/skin-5.css");
		jQuery(".logo-header img").attr("src", "images/logo-5.png");
		jQuery(".footer-light .logo-footer img").attr("src", "images/logo-l-5.png");
		jQuery(".footer-dark .logo-footer img").attr("src", "images/logo-5.png");
        return false;
    });	
	
    jQuery(".skin-6").on('click', function(){
        jQuery(".skin").attr("href", "css/skin/skin-6.css");
		jQuery(".logo-header img").attr("src", "images/logo-6.png");
		jQuery(".footer-light .logo-footer img").attr("src", "images/logo-l-6.png");
		jQuery(".footer-dark .logo-footer img").attr("src", "images/logo-6.png");
        return false;
    });		
		
		
});


