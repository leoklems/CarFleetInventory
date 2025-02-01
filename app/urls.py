from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *
app_name = 'app'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', loginPage, name='login'),
    # path('logout-request/', logout_request, name='logout_request'),
    path('logout/', logoutUser, name='logout'),
    # path('dashboard/<uid>/', MyDashboardView.as_view(), name='dashboard'),
    # path('my-profile/<uid>/', MyProfileView.as_view(), name='my_profile'),
    
    
    # # path('staff-file/<uid>/', view_file, name='staff_file'),
    
    # # path('my-profile/<uid>/', MyProfileView.as_view(), name='my_profile'),
    
    path('staff/', StaffView.as_view(), name='staff'),
    # path('new-position/', AddPosition.as_view(), name='new_position'),
    path('staff/new-staff/', Registration.as_view(), name='new_staff'),
    path('staff/staff-profile/<uid>/', StaffProfileView.as_view(), name='staff_profile'),
    # path('validate-email/', validate_email, name='email_validation'),
    # path('finance/', Finance.as_view(), name='finance'),
    # path('staff/staff-check-in/', CheckInStaff.as_view(), name='staff_checkin'),
    # path('staff-check-out/<a_id>/', check_out_staff, name='staff_checkout'),
    # path('staff-check-out-confirm/<a_id>/', confirm_check_out_staff, name='staff_checkout_confirm'),
    
    # # path('workers/', Workers.as_view(), name='workers'),
    # path('new-expenses/', AddExpenses.as_view(), name='add_expenses'),
    # path('new-income/', AddIncome.as_view(), name='add_income'),
    # path('income-detail/<pk>/', IncomeDetailView.as_view(), name='income_detail'),
    # path('income-change/<pk>/', UpdateIncome.as_view(), name='change_income'),
    # path('expenses-detail/<pk>/', ExpensesDetailView.as_view(), name='expenses_detail'),
    # path('expenses-change/<pk>/', UpdateExpenses.as_view(), name='change_expenses'),
    # # path('worker-check-in/', CheckInWorker.as_view(), name='worker_checkin'),
    # # path('worker-check-out/<a_id>/', check_out_worker, name='worker_checkout'),
    # # path('worker-check-out-confirm/<a_id>/', confirm_check_out_worker, name='worker_checkout_confirm'),
    
    # path('visitors/', Visitors.as_view(), name='visitors'),
    # path('new-visitor/', AddVisitor.as_view(), name='add_visitor'),
    # path('visit-detail/<pk>/', VisitDetailView.as_view(), name='visit_detail'),
    # path('change/<pk>/visitor-name/', VisitorNameUpdate.as_view(), name='change_visitor_name'),
    # path('change/<pk>/visitor-gender/', VisitorGenderUpdate.as_view(), name='change_visitor_gender'),
    # path('change/<pk>/visitor-phone-number/', VisitorPhoneNoUpdate.as_view(), name='change_visitor_phone_no'),
    # path('change/<pk>/visitor-address/', VisitorAddressUpdate.as_view(), name='visitor_change_address'),
    # path('change/<pk>/visit-purpose/', VisitPurposeUpdate.as_view(), name='visit_purpose_change'),
    # path('change/<pk>/visit-date/', VisitDateUpdate.as_view(), name='visit_date_change'),
    # path('change/<pk>/visit-time/', VisitTimeUpdate.as_view(), name='visit_time_change'),

    # path('projects/', ProjectsView.as_view(), name='projects'),
    path('new-car/', AddCar.as_view(), name='add_car'),
    path('cars/detail/<pk>/', CarDetailView.as_view(), name='car_detail'),
    # path('project-change/<pk>/title/', ProjectTitleUpdate.as_view(), name='change_project_title'),
    # path('project-change/<pk>/client/', ProjectClientUpdate.as_view(), name='change_project_client'),
    # path('project-change/<pk>/description/', ProjectDescriptionUpdate.as_view(), name='change_project_description'),
    # path('project-change/<pk>/lead/', ProjectLeadUpdate.as_view(), name='change_project_lead'),
    # path('project-change/<pk>/team/', ProjectTeamUpdate.as_view(), name='change_project_team'),
    # path('project-change/<pk>/type/', ProjectTypeUpdate.as_view(), name='change_project_type'),
    # path('project-change/<pk>/cost/', ProjectCostUpdate.as_view(), name='change_project_cost'),
    # path('project-change/<pk>/status/', ProjectStatusUpdate.as_view(), name='change_project_status'),
    # path('project-change/<pk>/start-date/', ProjectStartDateUpdate.as_view(), name='change_project_start_date'),
    # path('project-change/<pk>/completed/', ProjectCompletedUpdate.as_view(), name='change_project_completed'),
    # path('project-change/<pk>/completion-date/', ProjectCompletionDateUpdate.as_view(), name='change_project_completion_date'),
    # path('project-change/<pk>/completed-date/', ProjectCompletedDateUpdate.as_view(), name='change_project_completed_date'),



    path('services/', ServiceRecordView.as_view(), name='services'),
    path('new-service/', AddServiceRecord.as_view(), name='add_service'),
    path('service/detail/<pk>/', ServiceRecordDetailView.as_view(), name='service_detail'),
    # path('task-change/<pk>/title/', TaskTitleUpdate.as_view(), name='change_task_title'),
    # path('task-change/<pk>/staff/', TaskStaffUpdate.as_view(), name='change_task_staff'),
    # path('task-change/<pk>/description/', TaskDescriptionUpdate.as_view(), name='change_task_description'),
    # path('task-change/<pk>/creator/', TaskCreatorUpdate.as_view(), name='change_task_creator'),
    # path('task-change/<pk>/project/', TaskProjectUpdate.as_view(), name='change_task_project'),
    # path('task-change/<pk>/status/', TaskStatusUpdate.as_view(), name='change_task_status'),
    # path('task-change/<pk>/start-date/', TaskStartDateUpdate.as_view(), name='change_task_start_date'),
    # path('task-change/<pk>/completed/', TaskCompletedUpdate.as_view(), name='change_task_completed'),
    # path('task-change/<pk>/completion-date/', TaskCompletionDateUpdate.as_view(), name='change_task_completion_date'),
    # path('task-change/<pk>/completed-date/', TaskCompletedDateUpdate.as_view(), name='change_task_completed_date'),
    
    # # path('items/', Items.as_view(), name='items'),
    # # path('items/eatery/', EateryItems.as_view(), name='eitems'),
    # # path('create/position/', AddPosition.as_view(), name='new_position'),
    
    # path('change/<uid>/name/', StaffNameUpdate.as_view(), name='change_staff_name'),
    # path('change/<pk>/email/', EmailUpdate.as_view(), name='change_email'),
    # path('change/<uid>/gender/', StaffGenderUpdate.as_view(), name='change_gender'),
    # path('change/<uid>/position/', StaffPositionUpdate.as_view(), name='change_position'),
    # path('change/<uid>/address/', StaffAddressUpdate.as_view(), name='change_address'),
    # path('change/<uid>/phone-number/', StaffPhoneNoUpdate.as_view(), name='change_phone_no'),
    # # path('change/<pk>/profile-pic/', StaffProfilePixUpdate.as_view(), name='change_profile_pic'),
    # # path('change/<pk>/file/', StaffFileUpdate.as_view(), name='change_file'),
    
    # # path('delete-position/<pk>/', DeletePosition.as_view(), name='delete_position'),
    
    # # path('worker/change/<pk>/firstname/', WorkerFirstnameUpdate.as_view(), name='worker_change_firstname'),
    # # path('worker/change/<pk>/email/', WorkerEmailUpdate.as_view(), name='worker_update_email'),
    # # path('worker/change/<pk>/lastname/', WorkerSurnameUpdate.as_view(), name='worker_change_lastname'),
    # # path('worker/change/<pk>/gender/', WorkerGenderUpdate.as_view(), name='worker_change_gender'),
    # # path('worker/change/<pk>/title/', WorkerTitleUpdate.as_view(), name='worker_change_title'),
    # # path('worker/change/<pk>/address/', WorkerAddressUpdate.as_view(), name='worker_change_address'),
    # # path('worker/change/<pk>/phone-number/', WorkerPhoneNoUpdate.as_view(), name='worker_change_phone_no'),
    
    # path('info/', IgorithmInfo.as_view(), name='igorithm_info'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
