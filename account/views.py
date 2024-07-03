import json
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from .forms import ImageForm, TaskForm,TaskFullForm
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login,logout

# Create your views here.
from django.http import HttpResponse, JsonResponse
from .models import Image,Task,App
# Create your views here.
from rest_framework import viewsets
from .serializers import AndroidAppSerializer   #, TaskSerializer, ImageSerializer
#from .forms import UserTaskForm
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,ListAPIView
from account import models
User = get_user_model()
def admin_approval(request):
    task_list = Task.objects.all()
    arr=[]
    arr1=[]
    for x in task_list:
        if [x.name,x.user_id] in arr:
            
            continue
        else:
            arr1.append([x.name,x.id,x.is_approved])
            arr.append([x.name,x.user_id])
    
    
  
    print(task_list)
    print(arr)
    print(arr1)
    if request.user.is_admin:
        if request.method == "POST":
            # Get list of checked box id's
            print("iaminpost")
            id_list = request.POST.getlist('boxes')
            print(request.POST.getlist('boxes'))
            # Uncheck all events
            task_list.update(is_approved=False)

            # Update the database
            arr=[]
            for x in id_list:
                
                Task.objects.filter(pk=int(x)).update(is_approved=True)
                spector=Task.objects.filter(pk=int(x))
                for y in spector:
                    arr.append([y.name,y.user_id])
                #arr.append([Task.objects.filter(pk=int(x)).name,Task.objects.filter(pk=int(x)).user_id])
                
                print("getting id_list")
            print(arr)
            for z in arr:
                Task.objects.filter(name=z[0],user_id=z[1]).update(is_approved=True)
            # Show Success Message and Redirect
            messages.success(request, ("Task List Approval Has Been Updated!"))
            return redirect('indexapp')



        else:
            return render(request, 'approval_page.html',{"task": arr1})
    else:
        messages.success(request, ("You aren't authorized to view this page!"))
        return redirect('indexapp')


    return render(request, 'events/admin_approval.html')


def approval(request):
    task=Task.objects.all()
    task_list = Task.objects.all()
    user=User.objects.all()
    arr=[]
    arr1=[]
    for x in task_list:
        if [x.name,x.user_id] in arr:
            
            continue
        else:
            user=User.objects.filter(id=x.user_id)
            for y in user:
              arr1.append([x.name,x.id,x.is_approved,y.username])  
            

            arr.append([x.name,x.user_id])
    if request.user.is_admin:
        return render(request,'approval_page.html',{'task':arr1})
    else:
        messages.success(request,("you aren't authorised"))
        return redirect('')
def logout_view(request):
    logout(request)
    return redirect('indexapp')

class TaskCreate(APIView):
    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            #images will be in request.FILES
            form = TaskFullForm(request.POST or None, request.FILES or None)
            print("line35")
            files = request.FILES.getlist('image')
            print("line37")
            print(files)
            if form.is_valid():
                print("line39")
                user = request.user
                name = form.cleaned_data['name']
                print("line42")
                points = form.cleaned_data['points']
                task_obj = Task.objects.create(user=user,name=name,points=points) #create will create as well as save too in db.
                print("line45")
                for f in files:
                    print("line47")
                    Image.objects.create(task=task_obj,image=f)
                    print("line49")
            else:
                print("Form invalid")
            return render(request, 'apprec.html',{'task':Task.objects.all()})
#     queryset = models.Task.objects.all()
#     serializer_class = TaskSerializer

     #def perform_create(self, serializer):
#     #    print("iamhere")
#     #    serializer.save(app=self.request.name)
    #  def post(self, request, *args, **kwargs):
    #     print("some")
    #     ImageFormSet = modelformset_factory(Image,
    #                                         form=ImageForm)
    #     print("noerror in me")
    #     #'extra' means the number of photos that you can upload   ^
    #     if request.method == 'POST':
    #         print("iaminpost")
    #         taskForm = TaskForm(request.POST)
    #         formset = ImageFormSet(request.POST, request.FILES,
    #                             queryset=Image.objects.none())
        
    #         print(taskForm.is_valid())
    #         print(formset.errors,"line 50")
    #         if taskForm.is_valid() and formset.is_valid():
    #             print("iamhere")
    #             task_form = taskForm.save(commit=False)
    #             task_form.user = request.user
    #             task_form.save()
        
    #             for form in formset.cleaned_data:
    #                 #this helps to not crash if the user   
    #                 #do not upload all the photos
    #                 if form:
    #                     image = form['image']
    #                     photo = Image(task=task_form, image=image)
    #                     photo.save()
    #             # use django messages framework
    #             messages.success(request,
    #                             "Yeeew, check it out on the home page!")
    #             return render(request, 'apprec.html',{'task':Task.objects.all()})
    #             # return HttpResponseRedirect("/")
    #         else:
    #             print(taskForm.errors, formset.errors,"line 70")
    #             return render(request, 'apprec.html',{'task':Task.objects.all()})
    #     else:
    #         taskForm = TaskForm()
    #         formset = ImageFormSet(queryset=Image.objects.none())
    #     return render(request, 'index.html',
    #                 {'taskForm': taskForm, 'formset': formset})
    #  def post(self, request, *args, **kwargs):
    #       my_file=request.FILES.get('file')
    #       print(my_file)
    #       task=Task.objects.create(name=request.data['name'],points=request.data['points'],image=my_file,user=request.user)

    #       task.save()
    #       return render(request, 'apprec.html',{'task':Task.objects.all()})#Response(serializer.data, status=status.HTTP_201_CREATED)
#          print(task)
#         #  print(serializer.is_valid())
#         #  print(serializer.errors)
#         #  if serializer.is_valid():
#         #      print("iaminserializer.valid")
#         #      serializer.save()
#         #      print("iaminserializer.valid and saved")
#         #      task=Task.objects.all()
#         #      print(task)
#          return render(request, 'apprec.html',{'task':Task.objects.all()})
#             # return render(request,"apprec.html") #Response(serializer.data, status=status.HTTP_201_CREATED)
#         # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    

# class PhotoViewSet(ListAPIView):

#     queryset = models.Image.objects.all()
#     serializer_class = ImageSerializer

#     def post(self, request, *args, **kwargs):
        
#         file = request.data.get('image')
#         print(file)
#         image = models.Image.objects.create(image=file)
#         #return render(request,"apprec.html")
#         return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)
    

class AndroidAppViewSet(viewsets.ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AndroidAppSerializer

# class TaskViewSet(viewsets.ModelViewSet):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

def home(request):
    images=Image.objects.all()
    context={
         'images':images
     }
    return render(request, 'image.html',context)

def file_upload(request,id):
    if request.method == 'POST':
        my_file=request.FILES.get('file')
        print(my_file)
        img=Image.objects.create(image=my_file)
        print(img)
        
        return HttpResponse('')
    return JsonResponse({'post':'false'})
def add(request):
    return render(request,'createapp.html')

def addrec(request):
    x=request.POST['name']
    y=request.POST['link']
    z=request.POST['category']
    w=request.POST['subcategory']
    u=request.POST['points']
    mem=App(name=x,link=y,category=z,subcategory=w,points=u,user=request.user)
    mem.save()
    return redirect("/")

import base64
def base64_to_image(base64_string):
    format, imgstr = base64_string.split(';base64,')
    ext = format.split('/')[-1]
    return ContentFile(base64.b64decode(imgstr), name=uuid4().hex + "." + ext)

def taskcreate(request,id):
    
    task=Task(request.POST)
    print(request.POST)
   # task.image=base64_to_two_images(profile_picture_str)
    task.save()
    return redirect("/")    

def individual(request,id):
    task=Task.objects.filter(user=request.user,id=id)
    x=''
    for y in task:
        x=y.name
    print(x)
    rtask=Task.objects.filter(name=x)
    for x in rtask:
       print(x.image)
       print(x.points) 
    print(rtask)
    return render(request, 'individual.html',{'task':rtask})

def profile(request):
   
    task=Task.objects.filter(user=request.user)
    rtask=Task.objects.filter(user=request.user)
    for x in rtask:
        print(x.is_approved)
    print(task)
    arr=[]
    points=0
    for x in task:
        print("here")
        flag=0
        for y in arr:
            if x.name in y:
                flag=1
                break
        if flag==1:           
            continue
        else:
            if x.is_approved:
                points+=x.points
            arr.append([x.name,x.id,x.is_approved])
    # map={}
    # map1={}
    # for x in task:
    #     print(x.name)
    #     if(x.name in map1.keys()):
    #         continue
    #     else:
    #         map1[x.name]=[x.points]
    # for x in task:
    #     print(x.name)
    #     if(x.name in map.keys()):
    #         map[x.name].append(x.image)
    #     else:
    #         map[x.name]=[x.image]
    print(arr)
    return render(request, 'userprofile.html',{'task':arr,'points':points,'rtask':rtask})

def index(request):
    
    return render(request, 'index.html')

def indexapp(request):
    mem=App.objects.all()
    return render(request, 'indexapp.html',{'mem':mem})
def deleteapp(request,id):
    mem=App.objects.get(id=id)
    mem.delete()
    return redirect("/")

def addapp(request,id):
    mem=App.objects.get(id=id)
    try:
        task =Task.objects.filter(user=request.user)
    except Task.DoesNotExist:
        task = None
   # task=Task.objects.get(user=request.user)
    if(task==None):
        return render(request,'addapp.html',{'mem':mem})
    for x in task:
        if(mem.name==x.name):
    #print(task)
    #if(mem.name==task.name):
            return redirect("/")
    #print(mem.name)
    return render(request,'addapp.html',{'mem':mem})
# class TaskCreateView(APIView):
#     def post(self, request, *args, **kwargs):
#         print("intaskcreateview")
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             print("savedid")
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# def apprec(request,id):
#     print(request.POST.get('app'))
#     print(request.POST.get('image'))
#     print(id)
#     my_file=request.FILES.get('file')
#     img=Image.objects.create(image=my_file)
#    # t=request.POST['image']
   
#    # mem=App.objects.get(id=id)
#    # image=Image.objects.get(id=id)
#     task= TaskCreateView.as_view()
#     print(task)
#    # task=Task(app=mem.id,image=img.id)
#    # print(task)
#     #task.app=mem
#     #task.image=img
#    # task.save()
#     #_id=str(id)
#     #print("here")
#     return redirect("/")

def updateapp(request,id):
    mem=App.objects.get(id=id)
    return render(request,'updateapp.html',{'mem':mem})

def uprec(request,id):
    x=request.POST['name']
    y=request.POST['link']
    z=request.POST['category']
    w=request.POST['subcategory']
    u=request.POST['points']
    mem=App.objects.get(id=id)
    mem.name=x
    mem.link=y
    mem.category=z
    mem.subcategory=w
    mem.points=u
    mem.save()
    return redirect("/")

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            print("are we here")
            user = form.save()
            print(user.is_admin)
            print(user.is_customer)
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('indexapp')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('indexapp')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})

def admin(request):
    return render(request,'admin.html')


def customer(request):
    return render(request,'customer.html')

def tasks(request,id):
  
    task=Task.objects.filter(user=request.user)
    return  render(request, 'apprec.html',{'task':task})
