// Copyright (c) 2016, MohJamal and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Cash Receipt"] = {
	"filters": [
		{
			"fieldname":"receipt_type",
			"label": __("Receipt Type"),
			"fieldtype": "Link",
			"options": "Cash Receipt Type",
			
		},
		{
			"fieldname":"cash_classification",
			"label": __("Cash Classification"),
			"fieldtype": "Link",
			"options": "Cash Classification",
			
		}		
	]
};
