



















































// frappe.ui.form.on("Purchase Order", {
// 	refresh(frm) {
// 		frm.trigger("prepare_custom_button");
// 	},

// 	prepare_custom_button(frm) {
// 		frm.add_custom_button(__("Make Advance Shipment Note"), () => {
// 			frappe.model.open_mapped_doc({
// 				method: "erpnext_training_app.custom_folder.purchase_order.purchase_order.make_advance_shipment_note",
// 				frm: cur_frm,
// 				freeze_message: __("Creating Advance Shipment Note ...")
// 			})
// 		});
// 	}
// });