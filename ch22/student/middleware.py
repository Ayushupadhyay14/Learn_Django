# here cre a costom middleware in as per your requirment :
# here use to tow way to create a middleware

# 1--> function based middleware
# 2--> class based middleware in python":

# def my_fun_middleware(get_response):
#     print("Middleware initialized (runs once when Django starts)")

#     def middleware(request):
#         print("Before view")
#         response = get_response(request)
#         print("After view")
#         return response

#     return middleware
from django.shortcuts import render


def my_fun_middleware(get_response):
    print("Middleware initialized (runs once when Django starts)")

    def middleware(request):
        print("Before view")
        # Instead of calling the view, always show the under construction page
        response = render(request, 'student/uc.html')
        print("After view")
        return response

    return middleware
