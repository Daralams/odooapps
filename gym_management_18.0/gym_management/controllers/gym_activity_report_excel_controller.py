from odoo import http
from odoo.exceptions import ValidationError
from odoo.http import request, content_disposition
import io
import xlsxwriter

class GymActivityReportExcelController(http.Controller):
    @http.route('/gym/activity_report/download_excel', type='http', auth='user')
    def download_excel(self, start_date=None, end_date=None, **kwargs):
        response = request.make_response(
            None,
            headers=[
                ('Content-type', 'application/vnd.ms-excel'),
                ('Content-Disposition', content_disposition(f'Gym Activity Report ({start_date} - {end_date}).xlsx'))
            ]
        )

        # Ambil data dari database
        domain = []
        if start_date:
            domain.append(('date', '>=', start_date))
        if end_date:
            domain.append(('date', '<=', end_date))
        print("=====================================")
        print(domain)
        print("=====================================")

        activities = request.env['gym.member.activity'].sudo().search(domain)
        if not activities:
            raise ValidationError(f'No activity available from {start_date} - {end_date} periode.')
        
        # Siapkan Excel di memory
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output, {'in_memory': True})
        sheet = workbook.add_worksheet('Activity Report')

        # Define formats
        title_format = workbook.add_format({
            'bold': True,
            'font_size': 16,
            'align': 'center',
            'valign': 'vcenter'
        })
        period_format = workbook.add_format({
            'italic': True,
            'font_size': 10,
            'align': 'center',
            'valign': 'vcenter'
        })
        header_format = workbook.add_format({
            'bold': True,
            'text_wrap': True,
            'valign': 'vcenter',
            'align': 'center',
            'fg_color': '#1465B5',
            'font_color': 'white',
            'border': 1
        })
        cell_format = workbook.add_format({
            'text_wrap': True,
            'valign': 'top',
            'border': 1
        })

        # Merge cells for title
        sheet.merge_range('A1:G1', 'Gym Member Activity Report', title_format)
        sheet.merge_range('A2:G2', f'Period: {start_date} - {end_date}', period_format)

        # Adjust column widths
        sheet.set_column('A:A', 20)  # Member
        sheet.set_column('B:B', 20)  # Exercise
        sheet.set_column('C:C', 20)  # Equipment
        sheet.set_column('D:D', 10)  # Sets
        sheet.set_column('E:E', 10)  # Repeat
        sheet.set_column('F:F', 10)  # Weight
        sheet.set_column('G:G', 15)  # Date

        # Header
        headers = ['Member', 'Exercise', 'Equipment', 'Sets', 'Repeat', 'Weight', 'Date']
        for col_num, header in enumerate(headers):
                sheet.write(2, col_num, header, header_format)

        # Data
        for row_num, activity in enumerate(activities, start=3):
            sheet.write(row_num, 0, activity.name.name, cell_format if activity.name else '')
            sheet.write(row_num, 1, activity.exercise.name, cell_format if activity.exercise else '')
            sheet.write(row_num, 2, activity.equipment.name, cell_format if activity.equipment else '')
            sheet.write(row_num, 3, activity.sets, cell_format)
            sheet.write(row_num, 4, activity.repeat, cell_format)
            sheet.write(row_num, 5, activity.weight, cell_format)
            sheet.write(row_num, 6, activity.date.strftime('%Y-%m-%d'), cell_format if activity.date else '')

        response.stream.write(output.read())
        workbook.close()
        output.seek(0)
        # return sebagai file excel
        return response
