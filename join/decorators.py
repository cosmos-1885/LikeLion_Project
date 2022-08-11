from django.shortcuts import redirect

def login_required(func):
    def wrap(request, *args, **kwargs):
        user = request.session.get('user')
        if user is None or not user:
            return redirect('/login/')
        return func(request, *args, **kwargs)
    return wrap