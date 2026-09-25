# Copyright 2023 Tecnativa - Víctor Martínez
# Copyright 2023 Tecnativa - Pedro M. Baeza
# Copyright 2023 Tecnativa - Carolina Fernandez
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    "name": "Maintenance Security",
    'summary': "Adds security groups for maintenance.",
    'description': '''
Maintenance Security
====================

    Adds security groups for maintenance.

    Features:

        - UI Integration: Extends 1 view(s) in the Odoo interface.
        - Extends Odoo: Builds on mail.followers.
    ''',
    "version": "18.0.2.0.0",
    "category": "Tools",
    "website": "https://vertel.se/apps/odoo-oca-maintenance/maintenance_security",
    "author": "Tecnativa, Odoo Community Association (OCA)",
    "license": "AGPL-3",
    "depends": ["maintenance"],
    "data": [
        "views/maintenance_views.xml",
    ],
    "installable": True,
    "maintainers": ["victoralmau"],
}
