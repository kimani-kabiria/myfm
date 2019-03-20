from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views import generic
from django.views.generic import View
from .models import Station, Show, Episode
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'shows/index.html'
    context_object_name = 'all_shows'

    def get_queryset(self):
        return Show.objects.all()


class DetailView(generic.DetailView):
    model = Show
    template_name = 'shows/details.html'


class RadioView(generic.ListView):
    template_name = 'shows/radio.html'
    context_object_name = 'all_radio'
    pk_url_kwarg = 'Station_id'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Station.objects.all()


class StationView(generic.DetailView):
    model = Station
    template_name = 'shows/station.html'
    pk_url_kwarg = 'Station_id'
    slug_url_kwarg = 'slug'

    def get_queryset(self):
        return Station.objects.all()


class UserRegFormView(View):
    form_class = UserForm
    template_name = 'shows/user_reg.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            # Clean Data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            user.set_password(password)
            user.save()

            # Authenticate User
            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('shows:index')

        return render(request, self.template_name, {'form': form})


