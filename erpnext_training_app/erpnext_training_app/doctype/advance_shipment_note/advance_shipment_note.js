frappe.provide("erpnext.buying");
frappe.provide("erpnext.accounts.dimensions");

erpnext.buying.setup_buying_controller();

erpnext.buying.AdvanceShipmentNoteController = class AdvanceShipmentNoteController extends erpnext.buying.BuyingController {
	setup() {
		super.setup();
	}

	refresh(doc, cdt, cdn) {
		var me = this;
		super.refresh();
	}
};

// for backward compatibility: combine new and previous states
extend_cscript(cur_frm.cscript, new erpnext.buying.AdvanceShipmentNoteController({frm: cur_frm}));

frappe.ui.form.on("Advance Shipment Note", {
    refresh(frm) {
        frm.trigger("set_defualt_values");
    },

    set_defualt_values(frm) {
        if (!frm.doc.posting_date) {
            frm.set_value("posting_date", frappe.datetime.get_today());
        }
    }
});