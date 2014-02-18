(function($) {
    // add initialization routine for datetimepickers
    $.addWidgetInitializer(function(obj) {

        // Activate datetimepickers
        datetimepickers = obj.find('.bootstrap-datetimepicker');
        datetimepickers.datetimepicker();

        // set initial datetimepicker value
        datetimepickers.each(function() {
            var obj = $(this);
            var id  = "#" + obj.data("widgetid");
            var year = 0, month = 0, day = 0, hour = 0, minute = 0;

            if (obj.data("pickdate")) {
                year   = $(id + "-year").val();
                month  = $(id + "-month").val();
                day    = $(id + "-day").val();
            }
            if (obj.data("picktime")) {
                hour   = $(id + "-hour").val();
                minute = $(id + "-min").val();
            }
            obj.data("DateTimePicker").setDate(month + "/" + day + "/" + year + " " + hour + ":" + hour)
        });

        // event handler for datetimepickers to copy values to the
        // individual hidden value inputs
        datetimepickers.on("change.dp", function(e) {
            var obj    = $(e.target);
            var date   = obj.data("DateTimePicker").getDate();
            var id     = "#" + obj.data("widgetid");
            var fields = [];

            if (obj.data("pickdate")) {
                $(id + "-year").val(date.get("year"));
                // Some very stupid programmer decided that it's a good
                // idea to index months from 0 !?! wtf.
                $(id + "-month").val(date.get("month")+1);
                $(id + "-day").val(date.get("date"));
            }
            if (obj.data("picktime")) {
                $(id + "-hour").val(date.get("hour"));
                $(id + "-min").val(date.get("minute"));
            }
        });
    });
})(jQuery);
