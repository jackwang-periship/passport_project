from django import template

register = template.Library()

@register.inclusion_tag('home/sidebar.html')
def get_home_sidebar(request, perms):
    return {'request': request,
            'perms': perms,
            }