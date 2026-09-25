# Copyright 2019 ForgeFlow S.L.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

{
    "name": "Base Maintenance",
    'summary': "Base module for maintenance extensions.",
    'description': '''
Base Maintenance
================

    Base module for maintenance extensions.

    Features:

        - UI Integration: Extends 4 view(s) in the Odoo interface.
        - Extends Odoo: Builds on maintenance.team.
    ''',
    "version": "18.0.1.0.0",
    "author": "ForgeFlow, Odoo Community Association (OCA)",
    "development_status": "Beta",
    "website": "https://vertel.se/apps/odoo-oca-maintenance/base_maintenance",
    "category": "Maintenance",
    "license": "LGPL-3",
    "depends": ["maintenance"],
    "data": [
        "views/maintenance_team_views.xml",
        "views/maintenance_request_views.xml",
        "views/maintenance_equipment_views.xml",
        "views/report_maintenance_request.xml",
    ],
    "installable": True,
}
