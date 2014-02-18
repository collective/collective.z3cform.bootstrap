(function($) {
    "use strict";

    // List of initialization functions
    // These functions take a single jQuery object as parameter
    var initializers = []

    $.addWidgetInitializer = function(init) {
        initializers.push(init);
    };

    $.fn.initializeWidgets = function() {
        for (var i=0; i<initializers.length; i++) {
            initializers[i](this);
        }
    };

    // add initializer for widget description popovers
    $.addWidgetInitializer(function(obj) {
        var popovers = $(obj).find('.popover-activate');
        popovers.popover();
    });

    // initialize everything on the body
    $(document).ready(function() {
        $('body').initializeWidgets();
    });

})(jQuery);