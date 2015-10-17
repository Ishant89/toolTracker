from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import  *
from django.views.decorators.csrf import csrf_exempt
from .models import *

import os

def index(request):
    return render(request,'User/index.html')

@csrf_exempt
def formTest(request):
    if request.method == 'POST':
        form1 = ToolForm(request.POST,request.FILES)
        data = ''
        if form1.is_valid():
            for x in request.FILES['name']:
                data = data + x
            return HttpResponse(data)

    else:
        form1 = ToolForm()
    return render(request,'User/formTest.html',{'form':form1})


@csrf_exempt
def viewTool(request):
    if request.method == 'GET':
        tool_name_list = []
        tools = Tool.objects.all()
        for tool in tools:
            tool_name_list.append(tool)
        return render(request,"User/viewTool.html",{'tool_name':tool_name_list})

@csrf_exempt
def toolDetail(request,pk):
    if request.method == 'GET':
        fields_list = []
        tool = Tool.objects.get(id=pk)
        for field in tool.fields_set.all():
            fields_list.append(field)
        return render(request,"User/toolDetails.html",{'tool':tool,'fields':fields_list})


@csrf_exempt
def runTool(request):
    if request.method == 'GET':
        tool_name_list = []
        tools = Tool.objects.all()
        for tool in tools:
            tool_name_list.append(tool)
        return render(request,"User/runTool.html",{'tool_name':tool_name_list})

@csrf_exempt
def runToolDetail(request,pk):
    tool = Tool.objects.get(id=pk)
    fields = tool.fields_set.all()
    name_of_exec = tool.name
    file_exec = tool.file
    exec_str = './' + name_of_exec
    args = []

    if request.method == 'POST':
        form_list = []

        for field in fields:
            if field.type == 'FT':
                form1 = FileForm(request.POST,request.FILES)
                if form1.is_valid():
                    form_list.append((field.name,form1))
                    with open('temp','wb+') as arg1_file:
                        for chunk in request.FILES['file']:
                            arg1_file.write(chunk)
                    args.append('temp')

            if field.type == 'INT':
                form1 = IntForm(request.POST)
                if form1.is_valid():
                    form_list.append((field.name,form1))
                    int_value = form1.cleaned_data['int_field']
                    args.append(int_value)
            if field.type == 'FLT':
                form1 = FloatForm(request.POST)
                if form1.is_valid():
                    form_list.append((field.name,form1))
                    float_value = form1.cleaned_data['float_field']
                    args.append(float_value)
            if field.type == 'STR':
                form1 = StringForm(request.POST)
                if form1.is_valid():
                    form_list.append((field.name,form1))
                    string_value = form1.cleaned_data['string_field']
                    args.append(string_value)
        k = os.popen('chmod 777 ' + name_of_exec)
        data = k.read()
        print data
        for arg in args:
            exec_str = exec_str + " " + str(arg)
        print(exec_str)
        f = os.popen(exec_str)
        data = f.read()
        print data
        log1 = logs(user=request.user,log_data=data)
        log1.save()
        return render(request,"User/statusRedirect.html",{"id":log1.id})
    else:
        form_list = []

        for field in fields:
            if field.type == 'FT':
                form1 = FileForm()
                form_list.append((field.name,form1))
            if field.type == 'INT':
                form1 = IntForm()
                form_list.append((field.name,form1))

            if field.type == 'FLT':
                form1 = FloatForm()
                form_list.append((field.name,form1))

            if field.type == 'STR':
                form1 = StringForm()
                form_list.append((field.name,form1))
        print form_list

    return render(request,"User/runToolDetail.html",{'tool':tool,'forms':form_list})


@csrf_exempt
def viewLogs(request):
    log_objs = logs.objects.all()
    return render(request,"User/log.html",{'logs':log_objs})

@csrf_exempt
def logDetail(request,pk):
    log = logs.objects.get(id=pk)
    return render(request,'User/logDetail.html',{'data':log.log_data})