# -*- coding: utf-8 -*-
{
    'name': "Gym Management",
    'summary': "🚀 Gym Management – A complete system for managing gym memberships, training schedules, trainers, and payments in one platform.",
    'description': """
    🏋️ Gym Management System is a comprehensive solution designed to streamline the operations of gyms, fitness centers, and health clubs. This module enables you to:
        - Membership Management: Register members, manage membership types (monthly/annual), and track their status.
        - Training & Class Scheduling: Organize workout sessions, group classes, and personal trainer bookings.
        - Trainer Management: Store trainer profiles, work schedules, and areas of expertise.
        - Payments & Billing: Monitor membership payments, generate automatic invoices, and track transaction history.
        - Reports & Analytics: Get insights into member statistics, popular classes, and gym revenue.
        - etc
    """,
    'author': "Mangandaralam Sakti",
    'website': "https://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/gym_menu_views.xml',
        'views/res_partner_views.xml',
        'views/gym_membership_type_views.xml',
        'views/templates.xml',
    ],
    'images': ['gym_management/static/description/icon.png'],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application' : True
}

