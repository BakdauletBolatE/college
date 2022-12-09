from django.core.management import BaseCommand
from page.models import Page, PageType
from news

class Command(BaseCommand):

    def handle(self, *args, **options):
        page_types = [
            PageType(
                id=1,
                name='Статика'
            ),
            PageType(
                id=2,
                name='Ссылка'
            ),
            PageType(
                id=3,
                name='Динамика'
            )
        ]

        PageType.objects.bulk_create(page_types,
                                     unique_fields=['id'],
                                     ignore_conflicts=True)
        pages = [
            Page(
                id=1,
                order=1,
                title="Главная",
                title_kk="Басты бет",
                title_en="Main",
                link="/",
                page_type_id=2
            ),
            Page(
                id=2,
                order=1,
                title="Новости",
                title_kk="Жаңалықтар",
                title_en="News",
                link="newsapp:list_view",
                page_type_id=1
            ),
            Page(
                id=3,
                order=2,
                title="О колледже",
                title_kk="Колледж жайлы",
                title_en="About college",
                link="sapp:about_url",
                page_type_id=1
            ),
            Page(
                id=4,
                order=1,
                title="Администрация",
                title_kk="Администрация",
                title_en="Administration",
                link="employeesapp:list_government_view",
                page_type_id=1,
                parent_id=2
            ),
            Page(
                id=5,
                order=2,
                title="Преподаватели",
                title_kk="Мұғалімдер",
                title_en="Teachers",
                link="employeesapp:list_employees_view",
                page_type_id=1,
                parent_id=2
            ),
            Page(
                id=6,
                order=3,
                title="Кодекс чести",
                title_kk="Ар-намыс кодексі",
                title_en="Сode of honor",
                link="sapp:code_of_honor_url",
                page_type_id=1,
                parent_id=2
            ),
            Page(
                id=7,
                order=4,
                title="Галерея",
                title_kk="Галерея",
                title_en="Gallery",
                link="newsapp:list_gallery_view",
                page_type_id=1,
                parent_id=2
            ),
            Page(
                id=8,
                order=3,
                title="Учебный процесс",
                title_kk="Оқу процесі",
                title_en="Studying proccess",
                link="#",
                page_type_id=2
            ),
            Page(
                id=9,
                order=1,
                title="НОБД",
                title_kk="НОБД",
                title_en="NOBD",
                link="https://nobd.iac.kz/",
                page_type_id=2,
                parent_id=7
            ),
            Page(
                id=10,
                order=2,
                title="Zoom",
                title_kk="Zoom",
                title_en="Zoom",
                link="https://zoom.us/",
                page_type_id=2,
                parent_id=7
            ),
            Page(
                id=11,
                order=3,
                title="College smart nation",
                title_kk="College smart nation",
                title_en="College smart nation",
                link="https://college.snation.kz/kz/tko",
                page_type_id=2,
                parent_id=7
            ),
            Page(
                id=12,
                order=4,
                title="Office 365",
                title_kk="Office 365",
                title_en="Office 365",
                link="https://login.microsoftonline.com/common/oauth2/authorize",
                page_type_id=2,
                parent_id=7
            ),
            Page(
                id=13,
                order=4,
                title="Специальности",
                title_kk="Мамандықтар",
                title_en="Specialties",
                link="specapp:specialties_list_view",
                page_type_id=1,
            ),
            Page(
                id=14,
                order=5,
                title="Silkway Global",
                title_kk="Silkway Global",
                title_en="Silkway Global",
                link="https://silkway-edu.com/",
                page_type_id=2,
            ),
            Page(
                id=15,
                order=5,
                title="Контакты",
                title_kk="Контактілер",
                title_en="Contacts",
                link="sapp:about_url",
                page_type_id=2,
            ),
        ]

        Page.objects.bulk_create(pages,
                                 ignore_conflicts=True,
                                 unique_fields=['id'])
