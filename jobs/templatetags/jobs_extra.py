# Note: Make sure to create your template tags in a python module called templatetags
from django import template

register = template.Library()


@register.inclusion_tag('jobs/jobs_menu.html')
def get_jobs_sidebar(request, perms):
    return {'request': request,
            'perms': perms,
            }