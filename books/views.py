import json
import urllib
from django.template import RequestContext
from django.shortcuts import render, render_to_response
from django.http import HttpResponse

# Create your views here.

def welcome(request):
    return render_to_response("welcome.html", {}, context_instance=RequestContext(request))


def master(request):
    return render_to_response("master.html", {})

def getData(request):

    keyword = None
    if request.method == "POST":
        keyword = request.POST["keyword"]

    print keyword

    response_data = {}

    if keyword == None :
        response_data['result'] = 'failed'
        response_data['message'] = 'You messed up'
    else :
        url = "http://www.baidu.com/s?wd=" + keyword

        content = getHtml(url)

        response_data['result'] = 'Success'
        response_data['message'] = 'Result is : ' + content

    return HttpResponse(json.dumps(response_data), content_type="application/json")

def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html