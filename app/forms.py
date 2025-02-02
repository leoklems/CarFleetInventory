from django import forms
from django.forms import ModelForm, Textarea, TextInput, ClearableFileInput, MultipleChoiceField, \
    CheckboxSelectMultiple, Select, CheckboxInput, DateInput, TimeInput
from django.utils.translation import gettext_lazy as _
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .models import User


class CreateUserForm(UserCreationForm):
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget = forms.CheckboxSelectMultiple,
        required = False,
    )
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # fields = UserCreationForm.Meta.fields + ('first_name', 'last_name',  'username', 'password1', 'password2')
        error_messages = {
            'password1': {
                'required': _("this field is required."),
                'invalid': _("chose a valid password"),
                'validator': _("chose a valid password"),
            },
            'password2': {
                'required': _("this field is required."),
                'invalid': _("chose a valid password"),
                'validator': _("passwords don't match"),
            },
            'username': {
                'required': _("username field required."),
                'invalid': _("username should be less than 10 characters"),
                'validator': _("username should be less than 10 characters"),
            },
            'email': {
                'required': _("email field is required."),
                'invalid': _("please put a valid email address"),
                'validator': _("please put a valid email address"),
            },
        }


class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = ['name']


class StaffProfileForm(ModelForm):
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget = forms.CheckboxSelectMultiple,
        required = False,
    )
    class Meta:
        model = Staff
        field = '__all__'
        exclude = ['user', 'uid', 'date_joined', 'active', 'present', 'last_checkin', 'last_checkout']
        error_messages = {
            'date_joined': {
                'required': _("put a valid image file"),
            },
            'phone': {
                'invalid': _("put in a valid phone number"),
            },

        }
        widgets = {
            'position': Select(attrs={
                'class': 'form-control',
            }),
            'groups': CheckboxInput(attrs={
                'class': 'checkbox-form-control',
            }),

        }


class CarForm(ModelForm):
    class Meta:
        model = Vehicle
        field = '__all__'
        exclude = ['date_recorded']
        error_messages = {
            'year_purchased': {
                'invalid': _("put in a valid year"),
            },


        }
        widgets = {
            'tracker_status': forms.Select(choices=Vehicle.TRACKER_CHOICES),
            'serviceability': forms.Select(choices=Vehicle.SERVICABILITY_CHOICES),
        }


class ServiceRecordForm(forms.ModelForm):
    class Meta:
        model = ServiceRecord
        fields = '__all__'
        exclude = ["next_service_date, next_overnaul_date"]

        widgets = {
            'type': forms.Select(choices=ServiceRecord.TYPE_CHOICES),
            'overnaul_date': forms.DateInput(attrs={'type': 'date'}),
            # 'next_overnaul_date': forms.DateInput(attrs={'type': 'date'}),
            'service_date': forms.DateInput(attrs={'type': 'date'}),
            # 'next_service_date': forms.DateInput(attrs={'type': 'date'}),
        }

# class ServiceRecordForm(ModelForm):
#     class Meta:
#         model = ServiceRecord
#         field = '__all__'
#         error_messages = {
#             'overnaul_date': {
#                 'invalid': _("put in a valid year"),
#             },


#         }
#         widgets = {
#             'type': forms.Select(choices=ServiceRecord.TYPE_CHOICES),
#         }



# class ProjectTypeForm(ModelForm):
#     class Meta:
#         model = ProjectType
#         fields = ['name']



# class TaskForm(ModelForm):
#     class Meta:
#         model =Task
#         field = '__all__'
#         exclude = ['creator', 'completed', 'date_completed', 'duration']
#         widgets = {
#             'project': Select(attrs={
#                 'required': False,
#             }),

#         }


# class IncomeForm(ModelForm):
#     class Meta:
#         model =Income
#         fields = ['title', 'details', 'project', 'amount', 'date']
#         widgets = {
#             'project': Select(attrs={
#                 'type': 'select',
#                 'required': False,
#             }),
#             'date': DateInput(attrs={
#                 'type': 'date',
#             }),
#             'details': Textarea(attrs={
#                 'class': 'form-control',
#             }),
#         }


# class ExpensesForm(ModelForm):
#     class Meta:
#         model =Expenses
#         fields = ['title', 'details', 'project', 'amount', 'date']
#         widgets = {
#             'project': Select(attrs={
#                 'type': 'select',
#                 'required': False,
#             }),
#             'date': DateInput(attrs={
#                 'type': 'date',
#             }),
#             'details': Textarea(attrs={
#                 'class': 'form-control',
#             }),
#         }

# class VisitorForm(ModelForm):
#     class Meta:
#         model =Visitor
#         field = '__all__'
#         exclude = []


# class StaffNameChangeForm(ModelForm):
#     class Meta:
#         model = Staff
#         fields = ['name']
#         # exclude = ['email', 'last_name', 'username', 'password1', 'password2']


# # class SurnameChangeForm(ModelForm):
# #     class Meta:
# #         model = User
# #         fields = ['last_name']

# class EmailChangeForm(ModelForm):
#     class Meta:
#         model = User
#         fields = ['email']

# class StaffGenderChangeForm(ModelForm):
#     class Meta:
#         model = Staff
#         fields = ['gender']
#         widgets = {
#             'gender': Select(attrs={
#                 'class': 'form-control',
#             }),

#         }


# class StaffPositionChangeForm(ModelForm):
#     class Meta:
#         model = Staff
#         fields = ['position']
#         widgets = {
#             'position': Select(attrs={
#                 'class': 'form-control',
#             }),

#         }



# class StaffPhoneNoChangeForm(ModelForm):
#     class Meta:
#         model = Staff
#         fields = ['phone']

# class StaffAddressChangeForm(ModelForm):
#     class Meta:
#         model = Staff
#         fields = ['address']

# class StaffProfilePixChangeForm(ModelForm):
#     class Meta:
#         model = Staff
#         fields = ['display_image']

# class ProjectTitleChangeForm(ModelForm):
#     class Meta:
#         model = Project
#         fields = ['title']

# class ProjectClientChangeForm(ModelForm):
#     class Meta:
#         model = Project
#         fields = ['client']

# class ProjectDescriptionChangeForm(ModelForm):
#     class Meta:
#         model = Project
#         fields = ['description']

# class ProjectLeadChangeForm(ModelForm):
#     class Meta:
#         model = Project
#         fields = ['lead']
#         widgets = {
#             'lead': Select(attrs={
#                 'class': 'form-control',
#             }),

#         }

# class ProjectTeamChangeForm(ModelForm):
#     class Meta:
#         model = Project
#         fields = ['team']
#         widgets = {
#             'team': CheckboxSelectMultiple(attrs={
#                 'type': 'checkbox',
#             }),

#         }

# class ProjectTypeChangeForm(ModelForm):
#     class Meta:
#         model = Project
#         fields = ['type']
#         widgets = {
#             'type': Select(),

#         }

# class ProjectCostChangeForm(ModelForm):
#     class Meta:
#         model = Project
#         fields = ['cost']


# class ProjectStatusChangeForm(ModelForm):
#     class Meta:
#         model = Project
#         fields = ['status']
#         # widgets = {
#         #     'lead': Select(),

#         # }


# class ProjectStartDateChangeForm(ModelForm):
#     class Meta:
#         model = Project
#         fields = ['date_started']
#         widgets = {
#             'date_started': DateInput(attrs={
#                 'type': 'date',
#             }),

#         }

# class ProjectCompletedChangeForm(ModelForm):
#     class Meta:
#         model = Project
#         fields = ['completed']
#         widgets = {
#             'completed': CheckboxInput(attrs={
#                 'type': 'checkbox',
#             }),

#         }

# class ProjectCompletionDateChangeForm(ModelForm):
#     class Meta:
#         model = Project
#         fields = ['completion_date']
#         widgets = {
#             'completion_date': DateInput(attrs={
#                 'type': 'date',
#             }),

#         }

# class ProjectCompletedDateChangeForm(ModelForm):
#     class Meta:
#         model = Project
#         fields = ['date_completed']
#         widgets = {
#             'date_completed': DateInput(attrs={
#                 'type': 'date',
#                 'required': False,
#             }),

#         }


# class TaskTitleChangeForm(ModelForm):
#     class Meta:
#         model = Task
#         fields = ['title']

# class TaskDescriptionChangeForm(ModelForm):
#     class Meta:
#         model = Task
#         fields = ['description']
#         widgets = {
#             'staff': Textarea(attrs={
#                 'class': 'form-control',
#             }),

#         }

# class TaskStaffChangeForm(ModelForm):
#     class Meta:
#         model = Task
#         fields = ['staff']
#         widgets = {
#             'staff': Select(attrs={
#                 'class': 'form-control',
#             }),

#         }

# class TaskCreatorChangeForm(ModelForm):
#     class Meta:
#         model = Task
#         fields = ['creator']
#         widgets = {
#             'creator': Select(),

#         }


# class TaskProjectChangeForm(ModelForm):
#     class Meta:
#         model = Task
#         fields = ['project']
#         widgets = {
#             'project': Select(attrs={
#                 'type': 'select',
#                 'required': False,
#             }),
#         }


# class TaskStatusChangeForm(ModelForm):
#     class Meta:
#         model = Task
#         fields = ['status']
#         # widgets = {
#         #     'lead': Select(),

#         # }


# class TaskStartDateChangeForm(ModelForm):
#     class Meta:
#         model = Task
#         fields = ['date_started']
#         widgets = {
#             'date_started': DateInput(attrs={
#                 'type': 'date',
#             }),

#         }

# class TaskCompletedChangeForm(ModelForm):
#     class Meta:
#         model = Task
#         fields = ['completed']
#         widgets = {
#             'completed': CheckboxInput(attrs={
#                 'type': 'checkbox',
#             }),

#         }

# class TaskCompletionDateChangeForm(ModelForm):
#     class Meta:
#         model = Task
#         fields = ['completion_date']
#         widgets = {
#             'completion_date': DateInput(attrs={
#                 'type': 'date',
#             }),

#         }

# class TaskCompletedDateChangeForm(ModelForm):
#     class Meta:
#         model = Task
#         fields = ['date_completed']
#         widgets = {
#             'date_completed': DateInput(attrs={
#                 'type': 'date',
#                 'required': False,
#             }),

#         }


# class IncomeChangeForm(ModelForm):
#     class Meta:
#         model =Income
#         fields = ['title', 'details', 'project', 'amount', 'date']
#         widgets = {
#             'project': Select(attrs={
#                 'type': 'select',
#                 'required': False,
#             }),
#             'date': DateInput(attrs={
#                 'type': 'date',
#             }),
#             'details': Textarea(attrs={
#                 'class': 'form-control',
#             }),
#         }

# class VisitorNameChangeForm(ModelForm):
#     class Meta:
#         model = Visitor
#         fields = ['name']


# class VisitorGenderChangeForm(ModelForm):
#     class Meta:
#         model = Visitor
#         fields = ['gender']
#         widgets = {
#             'gender': Select(attrs={
#                 'class': 'form-control',
#             }),

#         }


# class VisitorPhoneNoChangeForm(ModelForm):
#     class Meta:
#         model = Visitor
#         fields = ['phone']

# class VisitorAddressChangeForm(ModelForm):
#     class Meta:
#         model = Visitor
#         fields = ['address']


# class VisitorPositionChangeForm(ModelForm):
#     class Meta:
#         model = Visitor
#         fields = ['purpose']
#         widgets = {
#             'purpose': Textarea(attrs={
#                 'class': 'form-control',
#             }),

#         }


# class VisitDateChangeForm(ModelForm):
#     class Meta:
#         model = Visitor
#         fields = ['date']
#         widgets = {
#             'date': DateInput(attrs={
#                 'type': 'date',
#             }),

#         }


# class VisitTimeChangeForm(ModelForm):
#     class Meta:
#         model = Visitor
#         fields = ['time']
#         widgets = {
#             'time': TimeInput(attrs={
#                 'type': 'time',
#             }),

#         }




