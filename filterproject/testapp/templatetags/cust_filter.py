from django import template
register=template.Library()
def trancate3(value):
    result=value[0:3]
    return result
@register.filter(name='t_n')
def trancaten(value,n):
    result=value[0:n]
    return result

register.filter('t_3',trancate3)
