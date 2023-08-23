import frappe

def on_submit(doc, method):
	pass

def on_cancel(doc, method):
	pass




































































'''
def on_submit(doc, method):
	make_purchase_order(doc)

def on_cancel(doc, method):
	pass

def make_purchase_order(doc):
	po_doc = frappe.new_doc("Purchase Order")
	po_doc.supplier = doc.supplier
	po_doc.company = doc.company
	po_doc.currency = doc.currency
	add_purchase_order_item(doc, po_doc)

	if len(po_doc.items) > 0:
		po_doc.save(ignore_permissions=True)

def add_purchase_order_item(doc, po_doc):
	item_wh_stock = get_available_stock(doc)
	for item in doc.items:
		if item.qty > item_wh_stock.get((item.item_code, item.warehouse), 0):
			po_doc.append("items", {
				"item_code": item.item_code,
				"item_name": item.item_name,
				"description": item.description,
				"item_group": item.item_group,
				"qty": item.qty - item_wh_stock.get((item.item_code, item.warehouse), 0),
				"warehouse": item.warehouse,
				"uom": item.uom,
				"conversion_factor": 1.0,
				"stock_uom": item.stock_uom,
				"schedule_date": add_days(nowdate(), 1),
				"sales_order": doc.name,
				"sales_order_item": item.name,
			})

def get_available_stock(doc):
	item_wh_stock = {}
	bin_data = frappe.get_all(
		"Bin",
		fields=["actual_qty", "item_code", "warehouse"],
		filters={
			"item_code": ("in", [item.item_code for item in doc.items]),
			"warehouse": ("in", [item.warehouse for item in doc.items])
		},
	)

	for d in bin_data:
		if d.actual_qty <=0:
			item_wh_stock.setdefault((d.item_code, d.warehouse), d.actual_qty)

	return item_wh_stock
'''