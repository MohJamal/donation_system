// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Receipt"] = {
	"filters": [
		{
			"fieldname":"receipt_type",
			"label": __("Receipt Type"),
			"fieldtype": "Link",
			"options": "Receipt Type",
			
		},
		{
			"fieldname":"donation_classification",
			"label": __("Donation Classification"),
			"fieldtype": "Link",
			"options": "Donation Classification",
			
		}		
	]
};