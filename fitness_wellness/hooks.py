app_name = "fitness_wellness"
app_title = "fitness Wellness"
app_publisher = "Your Organization"
app_description = "Fitness and Wellness Management System for ERPNext v15+"
app_email = "admin@example.com"
app_license = "mit"
app_include_js = "/assets/fitness_wellness/js/fitness_wellness.js"

scheduler_events = {
	"daily": [
		"fitness_wellness.tasks.send_membership_expiry_reminders",
		"fitness_wellness.tasks.auto_generate_monthly_invoices",
		"fitness_wellness.tasks.check_equipment_maintenance_due",
		"fitness_wellness.tasks.mark_absent_unbooked_members",
	],
	"weekly": [
		"fitness_wellness.tasks.generate_trainer_commission_vouchers",
		"fitness_wellness.tasks.send_weekly_progress_reports",
	],
	"monthly": [
		"fitness_wellness.tasks.process_emi_deductions",
	]
}

roles = [
	"Fitness Manager", "Front Desk Executive", "Trainer",
	"Dietitian", "Member", "Accounts Executive", "Facility Supervisor"
]

doc_events = {
	"Member Subscription": {
		"on_submit": "fitness_wellness.billing.auto_create_membership_invoice",
		"on_cancel": "fitness_wellness.member_management.handle_subscription_cancel"
	},
	"Class Enrollment": {
		"on_submit": "fitness_wellness.class_management.update_class_capacity"
	},
	"Membership Invoice": {
		"on_submit": "fitness_wellness.billing.create_sales_invoice"
	}
}
