from django.forms import Form
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView
from django.views.generic.detail import DetailView
from django.views.generic.edit import ProcessFormView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import JkObject, HouseOfObject, PaymentМethod, ClassBuilding

from django.core.mail import EmailMessage
from django.conf import settings

from gen_notices.forms import NoticeForm
from gen_notices.models import NoticeTemplate
# from gen_notices.views import FieldsNoticeView
# from gen_notices.views import fields_notice
from test_sendmail.forms import EmailForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


@login_required(login_url='/login/')
def jkobjects_index(request):

    if request.method == 'POST':
        not_n = request.POST['search']
        print('привет')

    search_query = request.GET.get('search', None)
    # print(search_query)
    search_query2 = request.GET.get('classbuilding', None)
    # if search_query == '':
    #     search_query = None
    # if search_query2 == '':
    #     search_query2 = None

    classbuilding = ClassBuilding.objects.all()
    jkobjects = JkObject.objects.all()
    count_jkobjects = jkobjects.filter(is_active='True').count()

    if any((search_query, search_query2)):
        # posts = Post.objects.filter(title__icontains=search_query, body__icontains=search_query)  # AND

        jk = JkObject.objects.all()

        if search_query is not None and search_query != '':
            # jk = JkObject.objects.filter(Q(name__icontains=search_query))
            jk = jk.filter(Q(name__in=request.GET.getlist('search')))
        if search_query2 is not None and search_query2 != '':
            jk = jk.filter(Q(class_building__in=request.GET.getlist('classbuilding')))

        # print(request.GET.getlist('classbuilding'))
        # for value in request.GET.getlist('classbuilding'):
        #     print(value)
        #
        #     if value is not None and value != '':
        #         jk = jk.filter(Q(class_building=value))

    else:
        jk = jkobjects

    page_number = request.GET.get('page', 1)  # this is the page number of page whose data you want to retrieve, you need to pass page value as query params

    paginator = Paginator(jk, 50)  # this will paginate the full queryset in pages of 10 objects
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'classbuilding': classbuilding,
        'count_jkobjects': count_jkobjects,
        'jkobjects': jkobjects,
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url
    }

    # print(classbuilding.name)

    return render(request, 'jk_objects/index.html', context)


# class JkobjectsDetailView(FormView, DetailView):
#     queryset = JkObject.objects.all()
#     context_object_name = 'object'
#     template_name = 'jk_objects/detail.html'
#     # success_url = reverse_lazy('jk_objects:detail', kwargs={'pk': object.pk})
#     success_url = '/?send_form'
#     # success_url = reverse_lazy('jk_objects:detail', kwargs={'pk': })
#     form_class = NoticeForm
#
#     def get_context_data(self, **kwargs):
#         context = super(JkobjectsDetailView, self).get_context_data(**kwargs)
#         context['house_objects'] = HouseOfObject.objects.all()
#         context['notice_templates'] = NoticeTemplate.objects.all()
#         context['notice_form'] = self.get_form()
#         # context['payment_methods'] = PaymentМethod.objects.all()
#         # context['festival_list'] = Festival.objects.all()
#         # And so on for more models
#         # print(context['notice_form'])
#
#         return context
#
#     def post(self, request, *args, **kwargs):
#
#         if request.method == "POST":
#             form = NoticeForm(request.POST, request.FILES)
#             if form.is_valid():
#                 notice = form.save(commit=False)
#                 notice.save()
#
#                 from_email = form.cleaned_data['email_agent']
#                 to_email = form.cleaned_data['office']
#                 subject = '2Привет!'
#                 message = form.cleaned_data['sum_of_rooms']
#                 try:
#                     attach = request.FILES['attach']
#                 except:
#                     attach = None
#
#                 # try:
#                 mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [to_email],
#                                     headers={
#                                         # 'From': from_email,
#                                         'Reply-to': from_email})
#
#                 if attach is not None:
#                     mail.attach(attach.name, attach.read(), attach.content_type)
#
#                 mail.content_subtype = 'html'
#                 mail.send()
#
#                 # return render(request, 'gen_notices/form1.html', context={'message': 'Sent email to %s' % to_email})
#
#                 # except (ValueError, TypeError, AttributeError, KeyError):
#                 #     print('Ошибка1')
#                 #
#                 # except:
#                 #     print('Ошибка2')
#                 #     # return render(request, 'admin/Error.html', {'message': 'Either the attachment is too  big or corrupt'})
#
#         else:
#             form = NoticeForm()
#
#         return FormView.post(self, request, context={'notice_form': form}, *args, **kwargs)
#
#     # def get_success_url(self, *args, **kwargs):
#     #     location = HttpRequest.build_absolute_uri(self.request)
#     #     print(location)
#     #     # return reverse('/buildings/detail/{}/'.format(self.kwargs['pk']))
#     #     return HttpResponseRedirect(location)
#     # #     return render(request, template_name=self.template_name)


# class HouseOfObjectDetailView(DetailView):
#     queryset = HouseOfObject.objects.all()
#     context_object_name = 'house_object'
#     template_name = 'jk_objects/detail.html'


class JkobjectsDetailView(LoginRequiredMixin, DetailView):
    login_url = '/login/'

    model = JkObject

    queryset = JkObject.objects.all()
    context_object_name = 'object'
    template_name = 'jk_objects/detail.html'

    def get_context_data(self, **kwargs):
        context = super(JkobjectsDetailView, self).get_context_data(**kwargs)
        context['house_objects'] = HouseOfObject.objects.all()
        context['notice_templates'] = NoticeTemplate.objects.all()
        # context['payment_methods'] = PaymentМethod.objects.all()
        # context['festival_list'] = Festival.objects.all()
        # And so on for more models
        # print(context['notice_form'])

        return context


