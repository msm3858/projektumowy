from django.urls import include,path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


from django.contrib.auth.decorators import login_required

app_name = 'umowy'

urlpatterns = [
    # ex: /
    path('',login_required(views.IndexView.as_view()),name='index'),
    path('login/',auth_views.login,name='login'),
    path('logout/',auth_views.logout,{'next_page':'umowy:login'},name='logout'),

    # /register
    path('register/', views.UserFormView.as_view(),name='user_register'),

    # ex: /systemy/
    path('systemy-lista/',login_required(views.SystemListView.as_view()),name='systemy_list'),
    # ex: /systemy/5/
    path ('systemy/<int:pk>/', login_required(views.SystemDetailView.as_view()),name='systemy_detail'),
    # ex: /systemy/add/
    path ('systemy/add/',login_required(views.SystemCreateView.as_view()),name='systemy_add'),
    # ex: /systemy/12/edit
    path('systemy/<int:pk>/edit/',login_required(views.SystemUpdateView.as_view()),name='systemy_update'),
    # ex: /systemy/12/delete
    path('systemy/<int:pk>/delete/',login_required(views.SystemDeleteView.as_view()),name='systemy_delete'),

    # ex: /umowy/
    path('umowy/',login_required(views.UmowyListView.as_view()),name='umowy_list'),
    # ex: /systemy/5/
    path('umowy/<int:pk>/', login_required(views.UmowyDetailView.as_view()),name='umowy_detail'),
    # ex: /umowy/add/
    path('umowy/add/', login_required(views.UmowyCreateView.as_view()), name='umowy_add'),
    # ex: /umowy/12/edit
    path('umowy/<int:pk>/edit/',login_required(views.UmowyUpdateView.as_view()),name='umowy_update'),
    # ex: /umowy/12/delete
    path('umowy/<int:pk>/delete/',login_required(views.UmowyDeleteView.as_view()),name='umowy_delete'),

    # ex: administracja/bazy/
    path('administracja/bazy/',login_required(views.BazyDanychListView.as_view()),name='bazy_list'),
    # ex: administracja/bazy/1/
    path('administracja/bazy/<int:pk>/',login_required(views.BazyDanychDetailView.as_view()),name='bazy_detail'),
    # ex: administracja/bazy/add
    path('administracja/bazy/add/',login_required(views.BazyDanychCreateView.as_view()),name='bazy_add'),
    # ex: administracja/baze/124/edit/
    path('administracja/bazy/<int:pk>/edit',login_required(views.BazyDanychUpdateView.as_view()),name='bazy_update'),
    # ex: administracja/bazy/12/delete
    path('administracja/bazy/<int:pk>/delete',login_required(views.BazyDanychDeleteView.as_view()),name='bazy_delete'),

    # ex: administracja/administratorzy/
    path('administracja/administratorzy/',login_required(views.AdministratorzyListView.as_view()),name='administratorzy_list'),
    # ex: administracja/administratorzy/1/
    path('administracja/administratorzy/<int:pk>/',login_required(views.AdministratorzyDetailView.as_view()),name='administratorzy_detail'),
    # ex: administracja/administratorzy/add
    path('administracja/administratorzy/add/',login_required(views.AdministratorzyCreateView.as_view()),name='administratorzy_add'),
    # ex: administracja/administratorzy/124/edit/
    path('administracja/administratorzy/<int:pk>/edit',login_required(views.AdministratorzyUpdateView.as_view()),name='administratorzy_update'),
    # ex: administracja/administratorzy/12/delete
    path('administracja/administratorzy/<int:pk>/delete',login_required(views.AdministratorzyDeleteView.as_view()),name='administratorzy_delete'),
    
    # ex: administracja/serwery/
    path('administracja/serwery/',login_required(views.SerweryListView.as_view()),name='serwery_list'),
    # ex: administracja/serwery/1/
    path('administracja/serwery/<int:pk>/',login_required(views.SerweryDetailView.as_view()),name='serwery_detail'),
    # ex: administracja/serwery/add
    path('administracja/serwery/add/',login_required(views.SerweryCreateView.as_view()),name='serwery_add'),
    # ex: administracja/serwery/124/edit/
    path('administracja/serwery/<int:pk>/edit',login_required(views.SerweryUpdateView.as_view()),name='serwery_update'),
    # ex: administracja/serwery/12/delete
    path('administracja/serwery/<int:pk>/delete',login_required(views.SerweryDeleteView.as_view()),name='serwery_delete'),
    
    # ex: administracja/serwerysystemow/
    path('administracja/serwerysystemow/',login_required(views.SerwerySystemowListView.as_view()),name='serwerysystemow_list'),
    # ex: administracja/serwerysystemow/1/
    path('administracja/serwerysystemow/<int:pk>/',login_required(views.SerwerySystemowDetailView.as_view()),name='serwerysystemow_detail'),
    # ex: administracja/serwerysystemow/add
    path('administracja/serwerysystemow/add/',login_required(views.SerwerySystemowCreateView.as_view()),name='serwerysystemow_add'),
    # ex: administracja/serwerysystemow/124/edit/
    path('administracja/serwerysystemow/<int:pk>/edit',login_required(views.SerwerySystemowUpdateView.as_view()),name='serwerysystemow_update'),
    # ex: administracja/serwerysystemow/12/delete
    path('administracja/serwerysystemow/<int:pk>/delete',login_required(views.SerwerySystemowDeleteView.as_view()),name='serwerysystemow_delete'),



]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
