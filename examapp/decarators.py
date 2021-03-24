from django.core.exceptions import PermissionDenied


def role_reqiured():

    def decorator(view_func):

        def wrap(request,*args,**kwargs):

            if request.POST.get('group'):
                g_id = request.POST.get('group')
            else:
                g_id = request.user.teacher.groups.first().id

            groups = []
            # subjects = []

            for group in request.user.teacher.groups.all():
                groups.append(group.id)
    
            
            # for subject in request.user.teacher.subject.all():
            #     subjects.append(subject.id)

            if int(g_id) in groups:
                return view_func(request,*args,**kwargs)
            else:
                raise PermissionDenied
        
        return wrap

    return decorator


def addTaskDecarator():
    def decorator(view_func):

        def wrap(request,*args,**kwargs):
            if request.POST.get('group'):
                g_id = request.POST.get('group')
            else:
                g_id = request.user.teacher.groups.first().id

            if request.POST.get('subject'):
                s_id = request.POST.get('subject')
            else:
                s_id = request.user.teacher.subject.first().id
            
            
            groups = []
            subjects = []

            for group in request.user.teacher.groups.all():
                groups.append(group.id)
    
            
            for subject in request.user.teacher.subject.all():
                subjects.append(subject.id)

            if int(g_id) in groups and int(s_id) in subjects:
                return view_func(request,*args,**kwargs)
            else:
                raise PermissionDenied
        
        return wrap

    return decorator
