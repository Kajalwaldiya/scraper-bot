from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# import lxml.html as lh
from lxml.html import fromstring

import requests

from scrapy.http import FormRequest
# from scrapy.http import Request

import mechanize

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

import lassie
from itertools import cycle
import traceback

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os
import re



class Dashboard(TemplateView):
	template_name = "bot_app/dashboard.html"

	def get_context_data(self, **kwargs):
		context = super(Dashboard, self).get_context_data(**kwargs)
		# import pdb; pdb.set_trace()
		url = 'https://weleakinfo.com/'
		driver = webdriver.Chrome('/usr/bin/chromedriver')  #path of chromedriver .exe 
		driver.get(url)
		sleep(7)
		form_query = self.request.GET.get('form_query',None)
		form_type = self.request.GET.get('form_type',None)

		print(form_query, " *****form_query*****")
		print(form_type, "  @@@@@form_type@@@@@")

		

		if form_query and form_type:
			query  = driver.find_element_by_name('query')
			type_q = driver.find_element_by_name('type')

			if form_query:
				query.send_keys(form_query)

			if form_type:
				type_q.send_keys(form_type)

			driver.find_element_by_name('search').click()
			sleep(5)
			res = driver.find_element_by_id('result')
			res_txt = res.text

			res1 = driver.find_element_by_css_selector('.poorfag')
			res1_txt = res1.text
			res_err = None
			if res1_txt:
				result = { 
						"query_time": res_txt,
					 	"database"  : res1_txt,
					 }
			else:
				res_err = driver.find_element_by_css_selector('.alert.alert-danger.warning')
				res_err_txt  = res_err.text
				result = None
			
			print(result)
			if result:
				save_output(result,form_query,form_type)
		
		return context



def save_output(result,query_term,query_type):
	
	file_name = "output.txt"
	is_exists = os.path.exists(file_name)
	query_time = re.findall(r'Query Time: ([0-9]+(?:\.[0-9]+)?)(?:\s)',result["query_time"])
	total_hits = re.findall(r"Total: ([0-9]+(?:\.[0-9]+)?)(?:\s)", result["query_time"])
	website_no = re.findall(r"([0-9]+) Website",result["query_time"])
	no_of_results = re.findall(r"Found ([0-9]+)", result["database"])
	database = re.findall(r"results in (.+)", result["database"])

	if len(database)<=0:
		database = re.findall(r"result in (.+)", result["database"])


	if is_exists:
		with open(file_name,'a') as fp:
			data = query_term+"\t"+query_type+"\t"+str(query_time[0])+"\t"+str(total_hits[0])+"\t"+str(website_no[0])+"\t"+str(no_of_results[0])+"\t"+str(database[0])+"\n"
			print("data ", data)
			fp.write(data)

	else:
		with open(file_name, 'w+') as fp:
			column_names = "query_term\tquery_type\tquery_time\ttotal_hits\twebsite_no\tno_of_results\tdatabase\n"
			data = query_term+"\t"+query_type+"\t"+str(query_time[0])+"\t"+str(total_hits[0])+"\t"+str(website_no[0])+"\t"+str(no_of_results[0])+"\t"+str(database[0])+"\n"
			fp.write(column_names)
			fp.write(data)





	