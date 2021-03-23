from django import template
from django.utils.safestring import mark_safe
from django.urls import reverse

register = template.Library()

url = reverse('examapp:addAnswer')
@register.simple_tag
def anser_check(qs,arg,arg2,csrf_token):
    form = f"""
 <form  class="answer row form-group table-hover"  enctype="multipart/form-data" action="{url}" method="POST">
                            <label class="col-8 form-label mb-1 mx-auto d-block">Задания еще не загружено загрузить задания</label>
                            <input class="col-8 form-control mb-1 mx-auto d-block" type="text" name="name" id="">
                            <input  type="hidden" name="csrfmiddlewaretoken" value="{csrf_token}">
                            <input  type="hidden" name="user" value="{arg}">
                            <input type="hidden" name="task" value="{arg2}">
                            <input class="col-8 form-control mx-auto d-block mb-1" type="file" name="files">

                             <button class="btn d-block col-8 btn-primary mb-1 mx-auto">Добавить задания</button>  
</form>
"""
    check = False
    for answer in qs:
        if answer.user.id == arg:
            check = True
            ans = f'Задания уже загружено <a href="{answer.files.url}">{answer}</a>'
            break
    
    if check == False:
        return mark_safe(form)
    else:

        return mark_safe(ans)

