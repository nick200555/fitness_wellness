import frappe

def auto_create_membership_invoice(doc, method):
	"""
	doc_events on_submit for Member Subscription
	Auto-creates a Membership Invoice when a Member Subscription is submitted.
	"""
	if doc.status == "Active" and not doc.membership_invoice:
		invoice = frappe.new_doc("Membership Invoice")
		invoice.member = doc.member
		invoice.subscription = doc.name
		invoice.amount = doc.actual_amount
		invoice.insert(ignore_permissions=True)
		invoice.submit()
		frappe.db.set_value("Member Subscription", doc.name, "membership_invoice", invoice.name)

def create_sales_invoice(doc, method):
	"""
	doc_events on_submit for Membership Invoice
	Creates a linked ERPNext Sales Invoice when Membership Invoice is submitted.
	"""
	pass
