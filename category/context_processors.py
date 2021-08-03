from .models import Category

'''
Context_preprocessors
It is a python function.
It takes a request as an argument and it will return the dictionary of data as a context.
'''

def menu_links(request):
    links = Category.objects.all()        # WE will fetch all the categories from the database
    return dict(links=links)              # store links in dictionary.