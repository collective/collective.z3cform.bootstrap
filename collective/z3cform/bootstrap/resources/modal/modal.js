(function($) {
    "use strict";

    // initialize modal forms
    $.addWidgetInitializer(function(obj) {
        var modals = obj.find('.modal-content');
        modals.each(function() {
            var form = $(this).find('form');
            if (form.length == 0)
                return;

            var options = {
                data: { 'ajax_load': new Date().getTime(), },
                success: function(responseText, statusText, xhr, form) {
                    var modal = form.parents('.modal');
                    var success = statusText === "success" || statusText === "notmodified";

                    if (! success) {
                        // The responseText parameter is actually xhr
                        xhr = responseText;
                        responseText = responseText.responseText;
                    }

                    // check if the form is present in the response
                    var response = $('<div />').html(responseText);
                    if (response.find('#' + form.attr('id')).length == 0) {
                        modal.modal('hide');
                        location.replace(location.href);
                    } else {
                        form.parents('.modal-content').html(response);
                        modal.initializeWidgets();
                    }
                },
            }
            // use the same callback for errors, most "errors" are actually
            // a success (ie. form redirects).
            options.error = options.success;
            form.ajaxForm(options);
        });
    });

    // activate bootstrap components in modals loaded from remote
    $(document).on('loaded.bs.modal', '.modal', {}, function(e) {
        $(this).initializeWidgets();
    });
})(jQuery);