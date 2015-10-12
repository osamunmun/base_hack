from django.shortcuts import render
from offence import scraping
from django.http import HttpResponse
import json

def batters(self):
    data = {'batters': scraping.scrape_batters()}
    return HttpResponse(json.dumps(data, ensure_ascii=False),
                                            content_type='application/json; charset=utf-8')
