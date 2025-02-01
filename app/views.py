from random import randint
from time import timezone

from django.core.paginator import Paginator
from django.http import JsonResponse, FileResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, View
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic.detail import BaseDetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from itertools import chain
from django.core.mail import send_mail

from .forms import *
from .models import *
from django.db.models import Count
from django.db.models import Q
from django.utils import timezone
from datetime import date, datetime

def random_int():
    random_ref = randint(0, 9999999999)
    uid = random_ref
    return uid


def random_int_short():
    random_ref = randint(0, 9999)
    uid = random_ref
    return uid

def loginPage(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        user = authenticate(request, username=username,
                            password=password)
        print(user)
        # try:
        #     username = User.objects.get(email=email)
            

        # except:
        #     user = None
        
        if user is not None:
            login(request, user)
            # staff = Staff.objects.get(user=request.user)
            # act = Activity(actor=staff, action='Login')
            # act.save()
            # if user.is_superuser:
            #     return redirect('app:home')
            # else:
            #     return redirect('app:dashboard', uid = staff.uid)
                # return reverse('app:dashboard', kwargs={'uid': })
            #     return redirect('app:management_home')
            # if user.has_perm("app.add_task"):
            #     # login(request, user)
            #     return redirect('bar:barman_home')
            # elif user.has_perm("bar.view_tableorder"):
            #     # login(request, user)
            #     return redirect('bar:home')
            # else:
            #     messages.warning(request, 'You have to be checked in first')
            return redirect('app:home')
        else:
            messages.info(request, 'username or password is incorrect')
            # print(User.objects.get(email=email, password = password))

    return render(request, 'forms/login.html')


def logoutUser(request):
    # user = request.user
    # print(user)
    # staff = Staff.objects.get(user=user)
    # act = Activity(actor=staff, action='Logout')
    # act.save()
    logout(request)
    return redirect('app:login')

class Registration(LoginRequiredMixin, View):
    # permission_required = 'users.add_user'

    def get(self, request):
        form = CreateUserForm()
        staff_profile_form = StaffProfileForm()

        context = {
            'form': form,
            'staff_info': staff_profile_form,
        }
        return render(request, 'forms/staff.html', context)

    def post(self, request, *args, **kwargs):
        # print(request.POST)
        form = CreateUserForm(request.POST)
        staff_profile_form = StaffProfileForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            # email = form.cleaned_data.get('email')
            exists = False
            groups = form.cleaned_data.get("groups")
            try:
                has = User.objects.get(email=email)
                exists = True
            except ObjectDoesNotExist:
                pass
            if exists:
                messages.warning(request, 'This email has already been registered, try another email')
                context = {
                    'form': form,
                }
                return render(request, 'forms/staff.html', context)
            else:
                # user.active = False
                
                print(staff_profile_form.errors)
                gender = staff_profile_form.cleaned_data.get('gender')
                name = staff_profile_form.cleaned_data.get('name')
                position = staff_profile_form.cleaned_data.get('position')
                phone_number = staff_profile_form.cleaned_data.get('phone')
                address = staff_profile_form.cleaned_data.get('address')
                uid = random_int_short()
                # user.username = uid
                user.save()
                if groups:
                    user.groups.set(groups)
                
                staff = Staff.objects.create(user=user, uid=uid, gender=gender, name=name, position=position, phone=phone_number, address=address)
                
                staff.save()
                return redirect('app:staff_profile', uid = uid)

        else:
            messages.warning(request, 'Fill out all the necessary details')
            context = {
                'form': form,
            }
            return render(request, 'forms/staff.html', context)



# class Home(LoginRequiredMixin, View):
class Home(View):

    def get(self, *args, **kwargs):
        today = datetime.today()
        day = today.day
        print(day)
        vehicles = Vehicle.objects.all()
        number_of_cars = vehicles.count()
        # tasks = Task.objects.all()
        # staffs = Staff.objects.all()
        # completed_projects = len([i for i in projects if i.status == "COMPLETED"])
        # active_projects = len([i for i in projects if i.status not in ["COMPLETED",  "CANCLED", "SUSPENDED"]])
        # overdue_projects = len([i for i in projects if date.today() > i.completion_date])
        # completed_tasks = len([i for i in tasks if i.status == "COMPLETED"])
        # active_tasks = len([i for i in tasks if i.status not in ["COMPLETED",  "CANCLED", "SUSPENDED"]])
        # overdue_tasks = len([i for i in tasks if date.today() > i.completion_date and i.status != "COMPLETED"])

        context = {
            'vehicles': vehicles,
            'number_of_cars': number_of_cars,
            # 'active_projects': active_projects,
            # 'overdue_projects': overdue_projects,
            # 'tasks': tasks,
            # 'completed_tasks': completed_tasks,
            # 'active_tasks': active_tasks,
            # 'overdue_tasks': overdue_tasks,
            # 'staffs': staffs,
            # 'product_images': product_images,
        }
        # orders_ = TableOrder.objects.filter(paid=True, date__month=timezone.now().month).values()
        # incomes = Income.objects.filter(date__month=timezone.now().month)
        # expences = Expenses.objects.filter(date__month=timezone.now().month)
        # print("current month :", timezone.now().month)
        # print(orders_)
        
        # context['expenses_data'] = expenses_data
        # print(alt_data_labels)
        # print(expenses_data)
        # To display the day of the week from a Django DateField in a template, you can use the date template filter along with the D
        # format specifier for the day of the week
        #If you want to display the full (long) day of the week in Django template, 
        # you can use the format specifier "l" with the date filter
        # return render(self.request, 'management/management-home.html', context)
        
        # print([x.product for x in product_images])

        return render(self.request, 'home.html', context)

class StaffView(LoginRequiredMixin, View):
    
    def get(self, *args, **kwargs):
        # active_staff = Attendance.objects.filter(checked_in=True).order_by('-check_in_time')
        # others_staff = Staff.objects.all().exclude(present=True)
        staff = Staff.objects.all()
        # positions = Position.objects.all()
        # product_images = ProductImage.objects.filter(lead=True)

        context = {
            'staff': staff,
            # 'others_staff': others_staff,
            # 'positions': positions,
        }
        # print([x.product for x in product_images])

        return render(self.request, 'staff.html', context)



class StaffProfileView(LoginRequiredMixin, DetailView):
    # permission_required = 'app.view_staff'
    model = Staff
    template_name = 'staff_profile.html'
    slug_field = 'uid'
    slug_url_kwarg = 'uid'



class CarDetailView(LoginRequiredMixin, DetailView):
    # permission_required = 'app.view_vehicle'
    model = Vehicle
    template_name = 'car-details.html'

# class AddCar(LoginRequiredMixin, CreateView):
#     # permission_required = 'app.add_vehicle'
#     model = Vehicle
#     form_class = CarForm
#     template_name = 'forms/car.html'
#     success_url = reverse_lazy('app:home')


class AddCar(LoginRequiredMixin, CreateView):
    model = Vehicle
    form_class = CarForm
    template_name = 'forms/car.html'
    success_url = reverse_lazy('app:home')

    def form_valid(self, form):
        # Get the submitted form values
        submitted_values = form.cleaned_data
        print("Form submitted successfully with values:", submitted_values)

        # Perform any additional actions with the submitted values
        # For example, you can log them or send an email notification

        return super().form_valid(form)

    def form_invalid(self, form):
        # Handle form errors
        errors = form.errors
        print("Form submission failed with errors:", errors)

        # Perform any additional actions with the errors
        # For example, you can log them or display custom error messages

        return super().form_invalid(form)


class AddServiceRecord(LoginRequiredMixin, CreateView):
    model = ServiceRecord
    form_class = ServiceRecordForm
    template_name = 'forms/sevice.html'
    success_url = reverse_lazy('app:home')

    def form_valid(self, form):
        # Get the submitted form values
        submitted_values = form.cleaned_data
        print("Form submitted successfully with values:", submitted_values)

        # Perform any additional actions with the submitted values
        # For example, you can log them or send an email notification

        return super().form_valid(form)

    def form_invalid(self, form):
        # Handle form errors
        errors = form.errors
        print("Form submission failed with errors:", errors)

        # Perform any additional actions with the errors
        # For example, you can log them or display custom error messages

        return super().form_invalid(form)


class ServiceRecordView(LoginRequiredMixin, View):
    
    def get(self, *args, **kwargs):
        services = ServiceRecord.objects.all()
        # product_images = ProductImage.objects.filter(lead=True)

        context = {
            'services': services,
            # 'product_images': product_images,
        }
        # print([x.product for x in product_images])

        return render(self.request, 'services.html', context)

class ServiceRecordDetailView(LoginRequiredMixin, DetailView):
    # permission_required = 'app.view_project'
    model = ServiceRecord
    template_name = 'service-details.html'

# class AddCar(LoginRequiredMixin, View):
#     # permission_required = 'users.add_user'

#     def get(self, request):
#         form = CarForm()

#         context = {
#             'form': form,
#         }
#         return render(request, 'forms/car.html', context)

#     def post(self, request, *args, **kwargs):
#         # print(request.POST)
#         form = CarForm(request.POST)
#         print(request.POST)

#         if form.is_valid():
#             user = form.save(commit=False)
#             name = form.cleaned_data.get('name')
#             serial_number = form.cleaned_data.get('serial_number')
#             year_purchased = form.cleaned_data.get('year_purchased')
#             year_alloted = form.cleaned_data.get('year_alloted')
#             agency = form.cleaned_data.get("agency")
#             location_of_deployment = form.cleaned_data.get('location_of_deployment')
#             description = form.cleaned_data.get('description')
#             tracker_status = form.cleaned_data.get('tracker_status')
#             serviceability = form.cleaned_data.get('serviceability')
            
#             exists = False
#             try:
#                 Vehicle.objects.get(serial_number=serial_number)
#                 exists = True
#             except ObjectDoesNotExist:
#                 pass
#             if exists:
#                 messages.warning(request, 'This serial_number has already been registered, try another serial_number')
#                 context = {
#                     'form': form,
#                 }
#                 return render(request, 'forms/car.html', context)
#             else:
                
#                 car = Vehicle.objects.create(
#                     name=name, 
#                     serial_number=serial_number, 
#                     year_purchased=year_purchased, 
#                     year_alloted=year_alloted, 
#                     agency=agency, 
#                     location_of_deployment=location_of_deployment, 
#                     description=description,
#                     # tracker_status=tracker_status,
#                     # serviceability=serviceability
#                     )
                
#                 car.save()
#                 return redirect('app:car_detail', pk = car.id)

#         else:
#             messages.warning(request, 'Fill out all the necessary details')
#             print(form.errors)
#             context = {
#                 'form': form,
#             }
#             return render(request, 'forms/car.html', context)

