from django import template

register = template.Library()


@register.simple_tag(name='user_value')
def user_value(user, value) -> None:
    label = value.name
    
    attrs = {
        'username': user.username,
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'password': ''
    }

    return attrs[label]