from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.base import View
from .models import News

class NewsList(ListView):
    template_name = 'news_list.html'
    model = News
    paginate_by = 10

class SearchSubmitView(View):
    template = 'search_submit.html'

    def post(self, request):
        template = loader.get_template(self.template)
        query = request.POST.get('search', '')

        items = News.objects.filter(title__icontains=query).order_by('-sentiment_score')

        context = {'query': query, 'items': items}

        rendered_template = template.render(context, request)
        return HttpResponse(rendered_template, content_type='text/html')
    def get(self,request):
    	template = loader.get_template(self.template)
    	return render(request, 'search_submit.html', content_type='text/html')

class SearchAjaxSubmitView(SearchSubmitView):
    template = 'search_results.html'