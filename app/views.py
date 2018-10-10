from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import School, Student

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['injectme'] = "Basic Injection!"
        return context


class SchoolListView(ListView):
    model = School
    context_object_name = 'school_list'
    template_name = 'app/school_list.html'


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail'
    model = School
    template_name = 'app/school_detail.html'


class SchoolCreateView(CreateView):
    fields = ['name', 'principal', 'location']
    model = School
    # if you dont give template name its is by default school_form.html but i give template name
    template_name = 'app/school_create.html'

class SchoolUpdateView(UpdateView):
    fields = ['name','principal']
    model = School
    # if you dont give template name its is by default school_form.html but i give template name
    template_name = 'app/school_create.html'


class SchoolDeleteView(DeleteView):
    #default context is school but i give name
    context_object_name = 'school_detail'
    model = School
    success_url = reverse_lazy("list")
    template_name = 'app/school_delete.html'
