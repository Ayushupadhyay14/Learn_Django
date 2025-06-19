from django import template

register = template.Library()


def myreplace(value, arg):
    return value.replace(arg, "I am")


register.filter('Upadhyay', myreplace)
