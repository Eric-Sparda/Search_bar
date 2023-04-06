from django.shortcuts import render
from .models import City
from .forms import SearchForm

def search(request):
    form = SearchForm(request.GET)
    query = form.data.get('query', '')

    results = City.objects.filter(name__icontains=query)

    context = {'results': results, 'form': form}
    return render(request, 'search.html', context)

def search_results(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = City.objects.filter(name__icontains=query)
    return render(request, 'searchv2/search_results.html', {'query': query, 'results': results})
