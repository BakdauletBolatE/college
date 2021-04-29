from django.template import Library

register = Library()

@register.filter_function
def order_bys(queryset, args):
    args = [x.strip() for x in args.split(',')]
    return queryset.order_by(*args)


