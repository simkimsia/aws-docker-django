import logging

logger = logging.getLogger('reports.admin')

from django.contrib import admin

# Register your models here.
from reports.models import Report, ReportTemplate

from jinja2 import Template

import json

from weasyprint import HTML, CSS

from django.http import HttpResponse

class ReportAdmin(admin.ModelAdmin):
    fields = ['commodity', 
    'date',
    'trade_period',
    'quantity_cutoff',
    'data',
    'template',
    'title']

    actions = ['print_as_pdf']

    def print_as_pdf(self, request, queryset):
        # logger.debug('anything')
        for report in queryset:
            markup = report.template.markup
            css = report.template.styles
            template = Template(markup)

            trades = json.loads(report.data)
            # logger.debug('see trades')
            # logger.debug(trades)
            final_markup = template.render(trades=trades)
            # logger.debug('see final markup')
            # logger.debug(final_markup)
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="somefilename.pdf"'
            HTML(string=final_markup).write_pdf(response, stylesheets=[CSS(string=css)])
            return response
        return
    print_as_pdf.short_description = 'Generate as pdf'

admin.site.register(Report, ReportAdmin)
admin.site.register(ReportTemplate)
