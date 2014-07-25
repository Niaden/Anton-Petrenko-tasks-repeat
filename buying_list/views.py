# coding: utf8
from django.shortcuts import render
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from buying_list.models import Item
from .forms import ItemForm

# Create your views here.
def showlist(request):
 	return render(request,'showlist.html', {'items': Item.objects.all()})

def additem(request):
	return render(request,'additem.html', {'form': ItemForm})

def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ItemForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            form.save()
            # import pdb; pdb.set_trace()
            return HttpResponse('thanks') # Redirect after POST
    else:
        form = ItemForm() # An unbound form

	return HttpResponse("somth wrong. it's not a post request or form isn't valid")


# def showlist(request):
# 	view = 'basic_one'
# 	html = "<html><body>THis is %s view </body></html>" % view
# 	return HttpResponse(html)

# def showlist(request):
# 	view = "template_two"
# 	t = get_template('myview.html')
# 	html = t.render(Context({'name': view}))
# 	return HttpResponse(html)

# def template_three_simple(request):
# 	view = "template_three"
# 	return render_to_response('myview.html', {'name': view})

# def articles(request):
# 	return render_to_response('articles.html', {'articles': Article.objects.all()})

# def article(request, article_id=1):
# 	#objects.get - юзать только, когда 1 объект(в нашем случае, запись) возвращаешь(если признаку в get будут удовлетворять более, чем 1 объект, будет ошибка). objects.filter - то же самое, только возвращается несколько объектов по признаку возвращаешь.
# 	return render_to_response('article.html', {'article': Article.objects.get(id=article_id), 'comments': Comments.objects.filter(comments_article_id=article_id)})