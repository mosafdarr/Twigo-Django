from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css):
    # Ensure `field` is a form field instance
    if hasattr(field, 'as_widget'):
        return field.as_widget(attrs={"class": css})
    return field
