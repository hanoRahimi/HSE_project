from django.urls import path
from . import views

urlpatterns = [
    path('incidents/', views.IncidentListView.as_view(), name='incident-list'),
    path('incident/<int:pk>/', views.IncidentDetailView.as_view(), name='incident-detail'),
    path('incident/create/', views.IncidentCreateView.as_view(), name='incident-create'),
    path('incident/<int:pk>/update/', views.IncidentUpdateView.as_view(), name='incident-update'),
    path('incident/<int:pk>/delete/', views.IncidentDeleteView.as_view(), name='incident-delete'),

    path('riskassessments/', views.RiskAssessmentListView.as_view(), name='riskassessment-list'),
    path('riskassessment/<int:pk>/', views.RiskAssessmentDetailView.as_view(), name='riskassessment-detail'),
    path('riskassessment/create/', views.RiskAssessmentCreateView.as_view(), name='riskassessment-create'),
    path('riskassessment/<int:pk>/update/', views.RiskAssessmentUpdateView.as_view(), name='riskassessment-update'),
    path('riskassessment/<int:pk>/delete/', views.RiskAssessmentDeleteView.as_view(), name='riskassessment-delete'),

    path('hsereports/', views.HSEReportListView.as_view(), name='hsereport-list'),
    path('hsereport/<int:pk>/', views.HSEReportDetailView.as_view(), name='hsereport-detail'),
    path('hsereport/create/', views.HSEReportCreateView.as_view(), name='hsereport-create'),
    path('hsereport/<int:pk>/update/', views.HSEReportUpdateView.as_view(), name= ''),
]