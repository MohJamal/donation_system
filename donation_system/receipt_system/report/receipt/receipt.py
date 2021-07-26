# Copyright (c) 2013, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import flt


def execute(filters=None):
    if not filters:
        filters = {}

    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    return [
        _("Name") + ":Select:200",
        _("Receipt Type") + ":Link/Receipt Type:120",
        _("Donation Classification") + ":Link/Donation Classification:200",
        _("Receipt Date") + ":Date:200",
        _("Branch") + ":Link/Branch:200",
    ]


def get_data(filters):
    conditions = get_conditions(filters)

    return frappe.db.sql("""select naming_series,
    receipt_type,
    donation_classification,
    receipt_date,
    branch from tabReceipt where  branch = 'Branch - A' %s """ % conditions, as_list=1)


def get_conditions(filters):
    conditions = ""

    if filters.get("receipt_type"):
        conditions += "and receipt_type = '%s'" % \
            filters["receipt_type"].replace("'", "\\'")

    if filters.get("donation_classification"):
        conditions += "and donation_classification = '%s'" % \
            filters["donation_classification"].replace("'", "\\'")

    return conditions
