import frappe

def handle_subscription_cancel(doc, method):
	"""
	doc_events on_cancel for Member Subscription
	Handles releasing bookings, waitlists, and updating member status on cancel.
	"""
	if doc.member:
		# Check if the member has other active subscriptions
		active_subs = frappe.get_all("Member Subscription",
			filters={"member": doc.member, "status": "Active", "docstatus": 1, "name": ["!=", doc.name]})
		if not active_subs:
			frappe.db.set_value("Member", doc.member, "status", "Cancelled")
