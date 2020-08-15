# Note: Make sure to create your template tags in a python module called templatetags
from django import template
from jobs.models import CompanyUser
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()


@register.inclusion_tag('jobs/jobs_menu.html')
def get_jobs_sidebar(request, perms):
    return {'request': request,
            'perms': perms,
            }

@register.simple_tag
def get_user_id(request):
    try:
        return request.user.companyuser.client.pk
    except:
        return 0