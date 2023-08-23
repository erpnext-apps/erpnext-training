import frappe
from frappe.model.mapper import get_mapped_doc


































# @frappe.whitelist()
# def make_advance_shipment_note(source_name, target_doc=None):
# 	def update_item(source, taget, source_parent):
# 		pass

# 	doclist = get_mapped_doc(
# 		"Purchase Order",
# 		source_name,
# 		{
# 			"Purchase Order": {
# 				"doctype": "Advance Shipment Note",
# 				"validation": {"docstatus": ["=", 1]},
# 			},
# 			"Purchase Order Item": {
# 				"doctype": "Advance Shipment Note Item",
# 				"field_map": [
# 					["name", "purchase_order_item"],
# 					["parent", "purchase_order"],
# 				],
# 				"postprocess": update_item,
# 			},
# 		},
# 		target_doc,
# 	)

# 	return doclist