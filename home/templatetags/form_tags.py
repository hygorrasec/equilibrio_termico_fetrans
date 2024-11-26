from django import template

register = template.Library()

@register.filter
def add_class(field, css_class):
    """Adiciona classes CSS a campos de formulário."""
    return field.as_widget(attrs={"class": css_class})
