from django.shortcuts import render

def index(request):
	return render(request, 'testapp/index.html', {'greeting': "He jij daar"})