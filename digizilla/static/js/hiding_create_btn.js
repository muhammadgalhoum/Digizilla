// Note: This is my try to hide the create button using JS but I already hid it using Python
// by using the 'create' attribute in the form view

odoo.define('your_module_name.your_module_name', function (require) {
    "use strict";

    var core = require('web.core');
    var FormView = require('web.FormView');

    FormView.include({
        render_buttons: function($node) {
            this._super.apply(this, arguments);
            if (this.$buttons) {
                // Hide the Create button
                this.$buttons.find('.o_form_button_create').hide();
            }
        },
    });
});