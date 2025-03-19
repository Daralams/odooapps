from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class GymActivityReport(models.TransientModel):
    _name = 'gym.activity.report'
    _description = 'Gym Activity Report'

    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)


    def action_gym_activity_report_pdf(self):
        """Button action for creating gym activity pdf report"""
        data = { 
            'start_date': self.start_date,
            'end_date': self.end_date,
            'activities': self.generate_data()
        }
        return self.env.ref(
            'gym_management.gym_member_activity_report_action').report_action(self, data=data)
    

    def generate_data(self):
        """Generate data to be printed in the report"""
        domain = []
        if self.start_date and self.end_date:
            if self.start_date > self.end_date:
                raise ValidationError(_("start date should be less than end date"))
            
        if self.start_date:
            domain.append(('date', '>=', self.start_date))
        if self.end_date:
            domain.append(('date', '<=', self.end_date))
        gym_activities = self.env['gym.member.activity'].search_read(domain=domain, fields=['name', 'exercise', 'equipment','sets','repeat', 'weight', 'date'])
        for rec in gym_activities:
            rec['name'] = rec['name'][1]
            rec['exercise'] = rec['exercise'][1]
            rec['equipment'] = rec['equipment'][1]
        return gym_activities