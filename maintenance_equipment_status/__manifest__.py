# Copyright 2020 ForgeFlow S.L. (https://forgeflow.com)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Maintenance Equipment Status",
    'summary': "Adds a status field to equipment.",
    'description': '''
Maintenance Equipment Status
============================

    Adds a status field to equipment.

    Features:

        - UI Integration: Extends 2 view(s) in the Odoo interface.
        - Extends Odoo: Builds on maintenance.equipment, maintenance.equipment.category, maintenance.equipment.status.
    ''',
    "version": "18.0.1.0.0",
    "category": "",
    "author": "ForgeFlow, Odoo Community Association (OCA)",
    "website": "https://vertel.se/apps/odoo-oca-maintenance/maintenance_equipment_status",
    "license": "LGPL-3",
    "depends": ["base_maintenance"],
    "data": [
        "security/ir.model.access.csv",
        "views/maintenance_equipment_status_views.xml",
        "views/maintenance_equipment_views.xml",
    ],
    "demo": ["data/demo_maintenance_equipment_status.xml"],
    "installable": True,
    "auto_install": False,
    "application": False,
}
