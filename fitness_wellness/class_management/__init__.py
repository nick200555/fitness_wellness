import frappe

def update_class_capacity(doc, method):
	"""
	doc_events on_submit for Class Enrollment
	Updates the current capacity / enrollment count on the Class Schedule.
	"""
	if doc.class_schedule:
		frappe.db.sql("""
			UPDATE `tabClass Schedule` 
			SET current_enrollment = current_enrollment + 1
			WHERE name = %s
		""", doc.class_schedule)
