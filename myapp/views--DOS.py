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

	dict = {
	  "now":datetime.now()
	  ,"emp_no":"335810"
	  ,"username":"JUDY 胡"
	  }
	
	return render(request, "hello6.html" , dict)        ## 用 dict 就要具名 dict ，才能傳出去。
##	return render(request, "hello6.html" , locals())      ## 用 locals()，則傳不出去。
##                        樣板名稱       傳遞全部區域變數



  	                        