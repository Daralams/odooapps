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
    'website': "https://www.linkedin.com/in/mangandaralam-sakti/",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sport',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'account', 'stock'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/gym_trainer_attendances_views.xml',
        'views/gym_member_attendances_views.xml',
        'views/gym_member_activity_views.xml',
        'views/gym_membership_type_views.xml',
        'views/gym_membership_detail_views.xml',
        'views/gym_workouts_views.xml',
        'views/gym_workouts_line_views.xml',
        'views/gym_workouts_exercise_views.xml',
        'views/gym_workouts_plan_views.xml',
        'views/gym_workout_days_views.xml',
        'views/gym_diet_plan_views.xml',
        'views/product_template_views.xml',
        'views/gym_trainer_skills_views.xml',
        'views/gym_membership_analysis_views.xml',
        'views/gym_member_analysis_views.xml',
        'views/gym_trainer_analysis_views.xml',
        'views/res_partner_views.xml',

        'report/gym_membercard_templates.xml',
        'report/gym_membercard_reports.xml',
        'report/gym_trainercard_templates.xml',
        'report/gym_trainercard_reports.xml',
        'report/gym_workout_templates.xml',
        'report/gym_workout_reports.xml',
        'report/gym_exercise_templates.xml',
        'report/gym_exercise_reports.xml',
        'report/gym_activity_reports.xml', 
        'report/gym_activity_templates.xml',

        'data/ir_cron.xml',
        'data/ir_sequence_data.xml',

        'wizard/gym_activity_report_views.xml',
        'views/gym_menu_views.xml',
        'views/templates.xml',
    ],
    'images': ['gym_management/static/description/icon.png'],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application' : True
}

