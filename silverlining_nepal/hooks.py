from . import __version__ as app_version

app_name = "silverlining_nepal"
app_title = "Silverlining Nepal"
app_publisher = "Faris"
app_description = "Library"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "nand@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/silverlining_nepal/css/silverlining_nepal.css"
# app_include_js = "/assets/silverlining_nepal/js/silverlining_nepal.js"

# include js, css files in header of web template
# web_include_css = "/assets/silverlining_nepal/css/silverlining_nepal.css"
# web_include_js = "/assets/silverlining_nepal/js/silverlining_nepal.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "silverlining_nepal/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "silverlining_nepal.install.before_install"
# after_install = "silverlining_nepal.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "silverlining_nepal.uninstall.before_uninstall"
# after_uninstall = "silverlining_nepal.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "silverlining_nepal.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"silverlining_nepal.tasks.all"
#	],
#	"daily": [
#		"silverlining_nepal.tasks.daily"
#	],
#	"hourly": [
#		"silverlining_nepal.tasks.hourly"
#	],
#	"weekly": [
#		"silverlining_nepal.tasks.weekly"
#	]
#	"monthly": [
#		"silverlining_nepal.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "silverlining_nepal.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "silverlining_nepal.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "silverlining_nepal.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Request Events
# ----------------
# before_request = ["silverlining_nepal.utils.before_request"]
# after_request = ["silverlining_nepal.utils.after_request"]

# Job Events
# ----------
# before_job = ["silverlining_nepal.utils.before_job"]
# after_job = ["silverlining_nepal.utils.after_job"]

# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"silverlining_nepal.auth.validate"
# ]

