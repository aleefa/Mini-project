from django.contrib import admin
from django.urls import path

from career_app import views

urlpatterns = [
    path('', views.first, name='first'),
    path('login',views.logins,name='logins'),
    path('add_agency',views.add_agency,name='add_agency'),
    path('editagn/<int:id>',views.editagn,name='editagn'),
    path('deleteag/<int:id>',views.deleteag,name='deleteag'),
    path('editagnpost',views.editagnpost,name='editagnpost'),
    path('deleteexp/<int:id>', views.deleteexp, name='deleteexp'),
    path('add_expert', views.add_expert, name='add_expert'),
    path('editexp/<int:id>', views.editexp, name='editexp'),
    path('editexppost', views.editexppost, name='editexppost'),
    path('add_notification', views.add_notification, name='add_notification'),
    path('admin_home', views.admin_home, name='admin_home'),
    path('block_and_unblock', views.block_and_unblock, name='block_and_unblock'),
    path('manage_agency', views.manage_agency, name='manage_agency'),
    path('manage_expert', views.manage_expert, name='manage_expert'),
    path('view_complaint_and_sendreply', views.view_complaint_and_sendreply, name='view_complaint_and_sendreply'),
    path('reply/<int:id>', views.reply, name='reply'),
    path('view_feedback_and_rating', views.view_feedback_and_rating, name='view_feedback_and_rating'),
    path('view_student', views.view_student, name='view_student'),
    path('add_doubt', views.add_doubt, name='add_doubt'),
    path('chat_with_expert', views.chat_with_expert, name='chat_with_expert'),
    path('doubt_clearance', views.doubt_clearance, name='doubt_clearance'),
    path('send_complaint_and_view_reply1', views.send_complaint_and_view_reply1, name='send_complaint_and_view_reply1'),
    path('send_rating_and_feedback1', views.send_rating_and_feedback1, name='send_rating_and_feedback1'),
    path('student_homepage', views.student_homepage, name='student_homepage'),
    path('upload_resume', views.upload_resume, name='upload_resume'),
    path('view_job_vaccancy_and_apply', views.view_job_vaccancy_and_apply, name='view_job_vaccancy_and_apply'),
    path('view_notification', views.view_notification, name='view_notification'),
    path('view_tips', views.view_tips, name='view_tips'),
    path('sendcomagency', views.sendcomagency, name='sendcomagency'),
    path('sendcomstud', views.sendcomstud, name='sendcomstud'),

    path('view_videos', views.view_videos, name='view_videos'),
    path('add_tip', views.add_tip, name='add_tip'),
    path('chat_with_student', views.chat_with_student, name='chat_with_student'),
    path('expert_homepage', views.expert_homepage, name='expert_homepage'),
    path('manage_tips', views.manage_tips, name='manage_tips'),
    path('send_rating_and_feedback', views.send_rating_and_feedback, name='send_rating_and_feedback'),
    path('view_notifications', views.view_notifications, name='view_notifications'),
    path('add_and_manage_video', views.add_and_manage_video, name='add_and_manage_video'),
    path('add_job', views.add_job, name='add_job'),
    path('add_placed_student', views.add_placed_student, name='add_placed_student'),
    path('add_video', views.add_video, name='add_video'),
    path('add_homepage', views.add_homepage, name='add_homepage'),
    path('doubt_reply', views.doubt_reply, name='doubt_reply'),
    path('doubt', views.doubt, name='doubt'),
    path('manage_job_details', views.manage_job_details, name='manage_job_details'),
    path('send_complaint_and_view_reply', views.send_complaint_and_view_reply, name='send_complaint_and_view_reply'),
    path('send_rating_and_feedback', views.send_rating_and_feedback, name='send_rating_and_feedback'),
    path('view_notification', views.view_notification, name='view_notification'),
    path('view_profile', views.view_profile, name='view_profile'),
    path('logincheck', views.logincheck, name='logincheck'),
    path('addagencypost', views.addagencypost, name='addagencypost'),
    path('addexpertpost', views.addexpertpost, name='addexpertpost'),
    path('addnotification', views.addnotification, name='addnotification'),
    path('replysend', views.replysend, name='replysend'),
    path('add_tips', views.add_tips, name='add_tips'),
    path('addvideo', views.addvideo, name='addvideo'),
    path('add_job1', views.add_job1, name='add_job1'),
    path('agenfeedback', views.agenfeedback, name='agenfeedback'),
    path('reg_index', views.reg_index, name='reg_index'),
    path('s_registration', views.s_registration, name='s_registration'),
    path('s_registration_post', views.s_registration_post, name='s_registration_post'),
    path('japply/<int:id>', views.japply, name='japply'),




path('chat_with_student', views.chat_with_student, name='chat_with_student'),
path('chatview', views.chatview, name='chatview'),
path('coun_msg/<int:id>', views.coun_msg, name='coun_msg'),

path('coun_insert_chat/<str:msg>/<int:id>', views.coun_insert_chat, name='coun_insert_chat'),

path('chat_with_expert', views.chat_with_expert, name='chat_with_expert'),
path('chateview', views.chateview, name='chateview'),
path('coun_msge/<int:id>', views.coun_msge, name='coun_msge'),




path('block_agency/<int:id>', views.block_agency, name='block_agency'),
path('unblock_agency/<int:id>', views.unblock_agency, name='unblock_agency'),
path('dlt_notn/<int:id>', views.dlt_notn, name='dlt_notn'),
path('mng_notn', views.mng_notn, name='mng_notn'),
path('manage_expert_search', views.manage_expert_search, name='manage_expert_search'),
path('manage_agency_search', views.manage_agency_search, name='manage_agency_search'),
path('manage_agency_search1', views.manage_agency_search1, name='manage_agency_search1'),
path('add_notification_search', views.add_notification_search, name='add_notification_search'),
path('student_search1', views.student_search1, name='student_search1'),
path('upres', views.upres, name='upres'),
path('manage_placed_student_details', views.manage_placed_student_details, name='manage_placed_student_details'),
path('view_req_stu', views.view_req_stu, name='view_req_stu'),
path('view_req_stu_search', views.view_req_stu_search, name='view_req_stu_search'),
path('acceptreq/<int:id>', views.acceptreq, name='acceptreq'),
path('rejectreq/<int:id>', views.rejectreq, name='rejectreq'),
path('delete_tips/<int:id>', views.delete_tips, name='delete_tips'),
path('tip_search', views.tip_search, name='tip_search'),
path('logout', views.logout, name='logout'),
path('view_notification2', views.view_notification2, name='view_notification2'),
path('view_stud', views.view_stud, name='view_stud'),
path('profile', views.profile, name='profile'),
path('view_stud_update', views.view_stud_update, name='view_stud_update'),
    path('likepost',views.likepost,name='likepost'),
    path('viewapplicationstts',views.viewapplicationstts,name='viewapplicationstts'),
    path('search_placed_student_details',views.search_placed_student_details,name='search_placed_student_details'),





]