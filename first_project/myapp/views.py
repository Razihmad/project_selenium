from django import http
from django.http import response
from django.shortcuts import render,HttpResponse
from selenium import webdriver 
from openpyxl import workbook
from selenium import webdriver
import pandas as pd
import xlwt
import os
from .models import FilesUpload
from django.conf import settings
# Create your views here.
def home(request):
    driver = webdriver.Chrome()


    driver.get('http://check-host.net/ip-info?host=anybunny.pro/top/whore')
    wb = xlwt.Workbook()
    ws = wb.add_sheet('sheet1')

    row = len(driver.find_elements_by_xpath('//*[@id="ip_info_inside-dbip"]/table/tbody/tr[1]/td[1]/table/tbody/tr'))

    # data = []
    for i in range(1,row+1):
        value1 = driver.find_element_by_xpath('//*[@id="ip_info_inside-dbip"]/table/tbody/tr[1]/td[1]/table/tbody/tr[{}]/td[1]'.format(i)).text
        value2 =  driver.find_element_by_xpath('//*[@id="ip_info_inside-dbip"]/table/tbody/tr[1]/td[1]/table/tbody/tr[{}]/td[2]'.format(i)).text

        ws.write(i-1,0,value1)
        ws.write(i-1,1,value2)

    wb.save('C:\\Users\\mail2\\Desktop\\first_project\\media\\media\\hello.xls')

    if FilesUpload.objects.filter(file = 'C:\\Users\\mail2\\Desktop\\first_project\\media\\media\\hello.xls').exists():
        pass
    else:
        document = FilesUpload.objects.create(file = 'C:\\Users\\mail2\\Desktop\\first_project\\media\\media\\hello.xls')
        document.save()
    driver.quit()


    context = {'files':FilesUpload.objects.all()}
    return render(request,'home.html',context)




def download(request,path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response = HttpResponse(fh.read(),content_type="application/file")
            response['Content-Disposition'] = 'inline;filename='+os.path.basename(file_path)
            return response
    raise Http404


    