# Copyright 2022 Tecnativa - Víctor Martínez
# Copyright 2024 Tecnativa - Carolina Fernandez
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Maintenance Product",
    'summary': "Links products to maintenance requests.",
    'description': '''
Maintenance Product
===================

    Links products to maintenance requests.

    Features:

        - UI Integration: Extends 2 view(s) in the Odoo interface.
        - Extends Odoo: Builds on maintenance.equipment, maintenance.equipment.category, product.category, product.product.
    ''',
    "version": "18.0.1.0.1",
    "category": "Maintenance",
    "website": "https://vertel.se/apps/odoo-oca-maintenance/maintenance_product",
    "author": "Tecnativa, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": ["maintenance", "product"],
    "installable": True,
    "data": [
        "views/maintenance_equipment_view.xml",
        "views/product_template_view.xml",
    ],
    "maintainers": ["victoralmau"],
}
