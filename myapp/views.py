from django.shortcuts import render

import random  # 加入 random 套件

from datetime import datetime

# Create your views here.

from django.http import HttpResponse




def sayhello(request):
	return HttpResponse("Hello Django!!")



def hello2(request, username):
	return HttpResponse("Hello!! " + username)


	

def hello3(request, username):
	now=datetime.now() 
	return render(request, "hello3.html" , locals() )	
##                        樣板名稱       傳遞全部區域變數




def hello4(request, username):
	now=datetime.now() 
	return render(request, "hello4.html" , locals() )	
##                        樣板名稱       傳遞全部區域變數


def hello5(request):
	now=datetime.now() 
	emp_no = "63006"
	username = "SAM 謝"
	return render(request, "hello5.html" , locals() )	 ## 變數 才可以用 locals() 
##                        樣板名稱       傳遞全部區域變數



def hello6(request):
  ## dictionary字典是用大括號{}包住內容。  
  ## list串列是用中括號[]包住內容。
	dict = {                           
	  "now":datetime.now()
	  ,"emp_no":"335810"
	  ,"username":"JUDY 胡"
	  }
	
	return render(request, "hello6.html" , dict)        ## 樣板用 {{emp_no}} {{username}}  {{now}}
##	return render(request, "hello6.html" , locals())  ## 樣板用 {{dict.emp_no}} {{dict.username}}  {{dict.now}}  
##                        樣板名稱       傳遞全部區域變數



def hello7(request):
  ## dictionary字典是用大括號{}包住內容。  
  ## list串列是用中括號[]包住內容。
	lst = [
	  datetime.now()
	  ,"335810"
	  ,"JUDY 胡"
	  ]
	
	return render(request, "hello7.html" , locals())  ## 串列 樣板用 {{lst.0}} {{lst.1}}  {{lst.2}}  
##                        樣板名稱       傳遞全部區域變數




def hello8(request, ManagerName):

  
	now=datetime.now() 
	emp_no = "001"
	username = "變數具名"
  
  ## dictionary字典是用大括號{}包住內容。 
	dict = {
	  "now":datetime.now()
	  ,"emp_no":"002"
	  ,"username":"dictionary字典"
	  }
  ## list串列是用中括號[]包住內容。	  
	lst = [
	  datetime.now()
	  ,"003"
	  ,"list串列"
	  ]
	
	return render(request, "hello8.html" , locals())  ## 樣板用 {{lst.0}} {{lst.1}}  {{lst.2}}  
##                        樣板名稱       傳遞全部區域變數



  	                        