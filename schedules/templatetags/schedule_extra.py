from django import template

register = template.Library()

@register.inclusion_tag('schedules/schedule_menu.html')
def get_schedule_sidebar(request, perms):
    return {'request': request,
            'perms': perms,
            }