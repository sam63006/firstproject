from django.shortcuts import render

import random  # �[�J random �M��

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
##                        �˪O�W��       �ǻ������ϰ��ܼ�




def hello4(request, username):
	now=datetime.now() 
	return render(request, "hello4.html" , locals() )	
##                        �˪O�W��       �ǻ������ϰ��ܼ�


def hello5(request):
	now=datetime.now() 
	emp_no = "63006"
	username = "SAM ��"
	return render(request, "hello5.html" , locals() )	 ## �ܼ� �~�i�H�� locals() 
##                        �˪O�W��       �ǻ������ϰ��ܼ�

def hello6(request):

	dict = {
	  "now":datetime.now()
	  ,"emp_no":"335810"
	  ,"username":"JUDY �J"
	  }
	
	return render(request, "hello6.html" , dict)        ## �� dict �N�n��W dict �A�~��ǥX�h�C
##	return render(request, "hello6.html" , locals())      ## �� locals()�A�h�Ǥ��X�h�C
##                        �˪O�W��       �ǻ������ϰ��ܼ�



  	                        