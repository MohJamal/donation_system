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
        _("Receipt Number") + ":select:200",
        _("Receipt Type") + ":Link/Receipt Type:200",
        _("Cash Classification") + ":Link/Cash Classification:200",
        _("Date Created") + ":Date:200",
        _("Branch") + ":Link/Branch:200",
    ]


def get_data(filters):
    conditions = get_conditions(filters)

    return frappe.db.sql("""select naming_series, 
    receipt_type,
    cash_classification,
    date_created,
    branch from `tabCash Receipt` where  branch = 'Branch - A' %s """ % conditions, as_list=1)


def get_conditions(filters):
    conditions = ""

    if filters.get("receipt_type"):
        conditions += "and receipt_type = '%s'" % \
            filters["receipt_type"].replace("'", "\\'")

    if filters.get("cash_classification"):
        conditions += "and cash_classification = '%s'" % \
            filters["cash_classification"].replace("'", "\\'")

    return conditions
