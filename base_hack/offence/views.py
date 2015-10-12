from django.shortcuts import render
from offence import scraping
from django.http import HttpResponse
from django.template.loader import render_to_string
import json

def batters(self):
    data = {'batters': scraping.scrape_batters()}
    return HttpResponse(render_to_string('index.html', data))
                                         # json.dumps(data, ensure_ascii=False),
                                         #    content_type='application/json; charset=utf-8')
