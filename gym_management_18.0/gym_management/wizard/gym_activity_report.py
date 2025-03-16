from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class GymActivityReport(models.TransientModel):
    _name = 'gym.activity.report'
    _description = 'Gym Activity Report'

    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)


    # development
    def action_gym_activity_report_pdf(self):
        if self.start_date > self.end_date:
            raise ValidationError(_("start date should be less than end date"))
        # Filter data berdasarkan rentang tanggal
        activities = self.env['gym.member.activity'].search([
            ('date', '>=', self.start_date),
            ('date', '<=', self.end_date)
        ])
        # Kirim data yang sudah difilter ke laporan
        data = {
            'start_date': self.start_date,
            'end_date': self.end_date,
            'activities': activities.ids  
        }
        return self.env.ref('gym_management.gym_member_activity_report_action').report_action(self, data=data)

        # print(activities.ids)
        # print(type(activities.ids))
        # print("======================= FOR BIASA =================================")
        # for record in activities:
        #     print(type(record))
        #     print(type(record.name.name))
        #     print(type(record.exercise.name))
        #     print(type(record.equipment.name))
        #     print(type(record.sets))
        #     print(type(record.repeat))
        # print("======================= FOR BIASA =================================")
        