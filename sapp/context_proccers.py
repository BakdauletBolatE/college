from django.utils.translation import gettext

from page.models import Page


def page_category(request):
    pages = Page.objects.all().filter(parent=None).order_by('order')
    return {
        'pages': pages,
        'settings': {
            'footer_text': gettext(
                'Основателем и первым президентом учреждения «Высший Педагогический колледж «Shymkent» является – Юнусов Бахтияр Саидович (1954-2010 г.г.) – профессор, ученый-арабист, член-корреспондент Академии естественных наук РК и Международной Академии наук педагогического образования России'),
            'email': 'ukpk_shym@mail.ru',
            'phone': '+7 7252 506136',
            'address': gettext('г.Шымкент, ул. 8 марта, 22'),
            'work_time_start': '9:00',
            'work_time_end': '18:00',
            'instagram_link': 'link',
            'facebook_link': 'link'
        }
    }
