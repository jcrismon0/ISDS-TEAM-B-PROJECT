from django.shortcuts import render

# Create your views here.
from .models import Topic
def index(request):
    """home page for todo list"""
    return render(request, 'proj/index.html')
def topics(request):
    """show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'proj/topics.html', context)
def topic(request, topic_id):
    """show a single topic and all its entries"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries' : entries}
    return render(request, 'proj/topic.html',context)