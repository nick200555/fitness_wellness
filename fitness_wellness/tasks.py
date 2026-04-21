"""
Scheduled Tasks
----------------
All scheduler task functions referenced in hooks.py scheduler_events.
"""

import frappe
from frappe.utils import today, add_days

def send_membership_expiry_reminders():
	"""
	Daily: Send membership expiry reminders 7, 3, and 1 days before expiry.
	"""
	try:
		for days in [7, 3, 1]:
			target_date = add_days(today(), days)
			expiring_subs = frappe.get_all(
				"Member Subscription",
				filters={"end_date": target_date, "status": "Active", "docstatus": 1},
				fields=["name", "member", "end_date", "plan"]
			)
			for sub in expiring_subs:
				member_email = frappe.db.get_value("Member", sub.member, "email")
				if member_email:
					frappe.sendmail(
						recipients=[member_email],
						subject=f"Membership Expiry Reminder - {days} Days Left",
						message=f"Dear Member, your subscription {sub.name} ({sub.plan}) will expire on {sub.end_date}. Please renew."
					)
	except Exception as e:
		frappe.log_error(title="send_membership_expiry_reminders Failed", message=frappe.get_traceback())

def auto_generate_monthly_invoices():
	"""
	Daily: Auto generate monthly invoices for recurring plans.
	"""
	pass

def check_equipment_maintenance_due():
	"""
	Daily: Check and alert for equipment maintenance due.
	"""
	pass

def mark_absent_unbooked_members():
	"""
	Daily: Mark members absent if unbooked or no show.
	"""
	pass

def generate_trainer_commission_vouchers():
	"""
	Weekly: Generate trainer commission vouchers.
	"""
	pass

def send_weekly_progress_reports():
	"""
	Weekly: Send weekly progress reports to members.
	"""
	pass

def process_emi_deductions():
	"""
	Monthly: Process EMI deductions.
	"""
	pass
