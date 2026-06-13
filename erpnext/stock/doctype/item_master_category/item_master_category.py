# Copyright (c) 2024, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ItemMasterCategory(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		is_group: DF.Check
		item_master_category: DF.Data | None
		lft: DF.Int
		old_parent: DF.Link | None
		parent_item_master_category: DF.Link | None
		rgt: DF.Int
	# end: auto-generated types
	pass
