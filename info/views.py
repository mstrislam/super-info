from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from info.models import Publications, Hashtags, Contacts


class HomeView(TemplateView):
   template_name = 'index.html'
   def get_context_data(self, **kwargs):
        publications = Publications.objects.filter(is_active=True)
        paginator = Paginator(publications, 10)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context = {
            'publication_list': page_obj,
         }
        return context


class ContactView(TemplateView):
   template_name = 'contact.html'

class PublicDetailView(TemplateView):
   template_name = 'publication-detail.html'

   def get_context_data(self, **kwargs):
      publication_pk = kwargs['pk']
      context = {

         'publication': Publications.objects.get(id = publication_pk)

      }
      return context

def client_contact(request):
   print(request.POST)

   name = request.POST['title']
   email = request.POST['email']
   subject = request.POST['subject']
   message = request.POST['message']

   Contacts.objects.create(name=name, email=email, subject=subject, message=message)

   return redirect('contact-list')

class HomeSearchView(TemplateView):
   template_name = 'index.html'

   def get_context_data(self, **kwargs):
      search_word = self.request.GET['search']
      context = {
         'detail-list': Publications.objects.get(
            Q(title__contains=search_word) | Q(description__contains=search_word)
         )
      }
      return context

