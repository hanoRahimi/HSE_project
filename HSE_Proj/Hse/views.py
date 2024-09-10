from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Incident, RiskAssessment, HSEReport

# Incident
class IncidentListView(LoginRequiredMixin, ListView):
    model = Incident
    template_name = 'incident_list.html'
    context_object_name = 'incidents'
    paginate_by = 10  # در صورت نیاز به صفحه‌بندی

# Incident
class IncidentDetailView(LoginRequiredMixin, DetailView):
    model = Incident
    template_name = 'incident_detail.html'
    context_object_name = 'incident'

# ایجاد حادثه جدید
class IncidentCreateView(LoginRequiredMixin, CreateView):
    model = Incident
    fields = ['title', 'description', 'incident_type', 'date_reported', 'location', 'risk_level', 'corrective_action']
    template_name = 'incident_form.html'
    success_url = reverse_lazy('incident-list')

    def form_valid(self, form):
        form.instance.reported_by = self.request.user  # ثبت کاربر گزارش‌دهنده
        return super().form_valid(form)

# ویرایش حادثه
class IncidentUpdateView(LoginRequiredMixin, UpdateView):
    model = Incident
    fields = ['title', 'description', 'incident_type', 'date_reported', 'location', 'risk_level', 'corrective_action']
    template_name = 'incident_form.html'
    success_url = reverse_lazy('incident-list')

#  حذف حادثه
class IncidentDeleteView(LoginRequiredMixin, DeleteView):
    model = Incident
    template_name = 'incident_confirm_delete.html'
    success_url = reverse_lazy('incident-list')

# RiskAssessment
class RiskAssessmentListView(LoginRequiredMixin, ListView):
    model = RiskAssessment
    template_name = 'riskassessment_list.html'
    context_object_name = 'risk_assessments'
    paginate_by = 10

# نمایش جزئیات ارزیابی ریسک
class RiskAssessmentDetailView(LoginRequiredMixin, DetailView):
    model = RiskAssessment
    template_name = 'riskassessment_detail.html'
    context_object_name = 'risk_assessment'

# ایجاد ارزیابی ریسک
class RiskAssessmentCreateView(LoginRequiredMixin, CreateView):
    model = RiskAssessment
    fields = ['risk_title', 'description', 'date_assessed', 'risk_level_before', 'risk_level_after', 'mitigation_plan']
    template_name = 'riskassessment_form.html'
    success_url = reverse_lazy('riskassessment-list')

    def form_valid(self, form):
        form.instance.assessed_by = self.request.user  # ثبت کاربر ارزیابی‌کننده
        return super().form_valid(form)

#  ویرایش ارزیابی ریسک
class RiskAssessmentUpdateView(LoginRequiredMixin, UpdateView):
    model = RiskAssessment
    fields = ['risk_title', 'description', 'date_assessed', 'risk_level_before', 'risk_level_after', 'mitigation_plan']
    template_name = 'riskassessment_form.html'
    success_url = reverse_lazy('riskassessment-list')

#  حذف ارزیابی ریسک
class RiskAssessmentDeleteView(LoginRequiredMixin, DeleteView):
    model = RiskAssessment
    template_name = 'riskassessment_confirm_delete.html'
    success_url = reverse_lazy('riskassessment-list')

# HSEReport
class HSEReportListView(LoginRequiredMixin, ListView):
    model = HSEReport
    template_name = 'hsereport_list.html'
    context_object_name = 'reports'
    paginate_by = 10

# برای نمایش جزئیات گزارش HSE
class HSEReportDetailView(LoginRequiredMixin, DetailView):
    model = HSEReport
    template_name = 'hsereport_detail.html'
    context_object_name = 'report'

# برای ایجاد گزارش HSE
class HSEReportCreateView(LoginRequiredMixin, CreateView):
    model = HSEReport
    fields = ['title', 'description', 'report_date', 'incident', 'risk_assessment']
    template_name = 'hsereport_form.html'
    success_url = reverse_lazy('hsereport-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user  # ثبت کاربر ایجاد‌کننده گزارش
        return super().form_valid(form)

#  برای ویرایش گزارش HSE
class HSEReportUpdateView(LoginRequiredMixin, UpdateView):
    model = HSEReport
    fields = ['title', 'description', 'report_date', 'incident', 'risk_assessment']
    template_name = 'hsereport_form.html'
    success_url = reverse_lazy('hsereport-list')

# حذف گزارش HSE
class HSEReportDeleteView(LoginRequiredMixin, DeleteView):
    model = HSEReport
    template_name = 'hsereport_confirm_delete.html'
    success_url = reverse_lazy('hsereport-list')
