import json
from datetime import datetime

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

from django.http import JsonResponse
from django.template.loader import render_to_string

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


@login_required(login_url='/login/')
def jkobjects_index(request):
    classbuilding = ClassBuilding.objects.all()
    jkobjects = JkObject.objects.all()
    count_jkobjects = jkobjects.filter(is_active='True').count()

    search_query = request.GET.get('jkobject', None)
    search_query2 = request.GET.get('classbuilding', None)

    if any((search_query, search_query2)):
        # posts = Post.objects.filter(title__icontains=search_query, body__icontains=search_query)  # AND

        jk = JkObject.objects.all()

        if search_query is not None and search_query != '':
            # jk = JkObject.objects.filter(Q(name__icontains=search_query))
            jk = jk.filter(Q(name__in=request.GET.getlist('jkobject')))
        if search_query2 is not None and search_query2 != '':
            jk = jk.filter(Q(class_building__in=request.GET.getlist('classbuilding')))

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


def building_search(request):
    classbuilding = ClassBuilding.objects.all()
    jkobjects_all = JkObject.objects.all()
    count_jkobjects = jkobjects_all.filter(is_active='True').count()
    jkobjects = jkobjects_all

    #######
    data = dict()
    if request.method == 'POST':
        # jkobjects = JkObject.objects.all()
        data['is_valid'] = True

        # print('пост')

        # custom_decks = request.POST.dict()
        # print(custom_decks)

        # for key, value in request.POST.items():
        #     print(key, value)

        # received_json_data = json.loads(request.body.decode("utf-8"))
        # received_json_data = json.loads(request.POST['data'])
        # print(received_json_data)

        search_query = request.POST.get('jkobject', None)
        print(search_query)
        search_query2 = request.POST.get('classbuilding', None)

        if any((search_query, search_query2)):
            # posts = Post.objects.filter(title__icontains=search_query, body__icontains=search_query)  # AND

            if search_query is not None and search_query != '':
                # jkobjects = JkObject.objects.filter(Q(name__icontains=search_query))
                # jkobjects = jkobjects.filter(Q(name__in=request.GET.getlist('jkobject')))
                jkobjects = jkobjects.filter(Q(name__in=search_query.split(',')))
                # print(jkobjects)
            if search_query2 is not None and search_query2 != '':
                jkobjects = jkobjects.filter(Q(class_building__in=search_query2.split(',')))

        # else:
        #     jkobjects = JkObject.objects.all()

        data['html'] = render_to_string('jk_objects/includes/jk_ajax_list_card.html', {'jkobjects': jkobjects}, request=request)
        return JsonResponse(data)


    ########

    # search_query = request.GET.get('jkobject', None)
    # search_query2 = request.GET.get('classbuilding', None)

    # if any((search_query, search_query2)):
    #     # posts = Post.objects.filter(title__icontains=search_query, body__icontains=search_query)  # AND
    #
    #     if search_query is not None and search_query != '':
    #         # jk = JkObject.objects.filter(Q(name__icontains=search_query))
    #         jkobjects = jkobjects.filter(Q(name__in=request.GET.getlist('jkobject')))
    #     if search_query2 is not None and search_query2 != '':
    #         jkobjects = jkobjects.filter(Q(class_building__in=request.GET.getlist('classbuilding')))

    if request.method == 'GET':


        context = {
            'classbuilding': classbuilding,
            'count_jkobjects': count_jkobjects,
            'jkobjects_all': jkobjects_all,
            'jkobjects': jkobjects
        }

        return render(request, 'jk_objects/index2.html', context)
        # data['html'] = render_to_string('jk_objects/includes/jk_t.html', {'jkobjects': jkobjects}, request=request)
        # return JsonResponse(data)



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


