/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { FormController } from "@web/views/form/form_controller";
import { onMounted } from "@odoo/owl";


patch(FormController.prototype, {
    setup() {
        super.setup(...arguments);

        onMounted(() => {
            const resModel =
                this.props.resModel ||
                (this.model && this.model.resModel) ||
                "";

            if (resModel !== "digizilla.digizilla") {
                return;
            }

            // Target the primary action button(s) in the control panel
            const controlPanel = document.querySelector(".o_control_panel");
            if (!controlPanel) {
                return;
            }

            const buttons = controlPanel.querySelectorAll(
                "button.o_form_button_create, " +
                "button[name='create'], " +
                ".o_cp_buttons .btn-primary"
            );

            buttons.forEach((btn) => {
                const label = btn.textContent.trim().toLowerCase();
                if (label === "new" || label === "create") {
                    btn.style.display = "none";
                }
            });
        });
    },
});
