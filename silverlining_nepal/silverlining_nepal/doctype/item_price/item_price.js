// Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
// License: GNU General Public License v3. See license.txt

frappe.ui.form.on("Item Price", {
	setup(frm) {
		frm.set_query("item_code", function() {
			return {
				filters: {
					"disabled": 0,
					"has_variants": 0
				}
			};
		});
	},

	onload(frm) {
		// Fetch price list details
		frm.add_fetch("price_list", "buying", "buying");
		frm.add_fetch("price_list", "selling", "selling");
		frm.add_fetch("price_list", "currency", "currency");

		// Fetch item details
		frm.add_fetch("item_code", "item_name", "item_name");
		frm.add_fetch("item_code", "description", "item_description");
		frm.add_fetch("item_code", "stock_uom", "uom");

		frm.set_df_property("bulk_import_help", "options",
			'<a href="/app/data-import-tool/Item Price">' + __("Import in Bulk") + '</a>');

		frm.set_query('batch_no', function() {
			return {
				filters: {
					'item': frm.doc.item_code
				}
			};
		});
	},
	valid_from: function(frm){
		frappe.call({
			method:"erpnext.nepali_date.get_converted_date",
			args: {
				date: frm.doc.valid_from
			},
			callback: function(resp){
				if(resp.message){
					cur_frm.set_value("valid_fromnepal",resp.message)
				}
			}
		})
	},
	valid_upto: function(frm){
		frappe.call({
			method:"erpnext.nepali_date.get_converted_date",
			args: {
				date: frm.doc.valid_upto
			},
			callback: function(resp){
				if(resp.message){
					cur_frm.set_value("valid_uptonepal",resp.message)
				}
			}
		})
	},
	before_save : function(frm){
		if(frm.is_dirty()){
			frappe.call({
				method: 'update_customer_pricing_rule_item',
				doc: frm.doc,
				callback: function(frm){
					//
				}
			})
		}
	}
});