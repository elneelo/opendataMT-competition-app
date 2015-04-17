#
#   author: Neil Barry-Murphy
#
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from comp_entries.models import Competition

def entries_home(request):
    latest_comp_list = Competition.objects.order_by('-deadline_date')[:5]
    context = {'latest_comp_list': latest_comp_list, 'entries_home':Competition.objects.all()}
    return render(request, 'comp_entries/entries_home.html', context)

def entries_detail(request, comp_id):
    query = get_object_or_404(Competition, pk=comp_id)
    context = {'query':query}
    return render(request, 'comp_entries/entries_detail.html', context)

def search_titles(request):
    if request.method == "POST":
        search_text = request.POST['search_text']
    else:
        search_text = ''
    comp_entries = Competition.objects.filter(name__contains=search_text)
    context = {'comp_entries':comp_entries}
    return render(request, 'comp_entries/ajax_search.html', context)