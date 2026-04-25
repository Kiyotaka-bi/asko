from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Movie
from .forms import MovieForm, RegisterForm, CommentForm


class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'CineBoard/register.html'
    success_url = reverse_lazy('login')


class UserLoginView(LoginView):
    template_name = 'CineBoard/login.html'


class MovieListView(ListView):
    model = Movie
    template_name = 'CineBoard/movie_list.html'
    context_object_name = 'movies'

    def get_queryset(self):
        queryset = Movie.objects.all()

        search = self.request.GET.get('q')
        genre = self.request.GET.get('genre')

        if search:
            queryset = queryset.filter(title__icontains=search)

        if genre:
            queryset = queryset.filter(genre__name=genre)

        return queryset.order_by('-rating')


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'CineBoard/movie_detail.html'

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        movie = self.get_object()
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.movie = movie
            comment.user = request.user
            comment.save()

        return redirect('movie_detail', pk=movie.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


class MovieCreateView(LoginRequiredMixin, CreateView):
    model = Movie
    form_class = MovieForm
    template_name = 'CineBoard/movie_form.html'
    success_url = reverse_lazy('movie_list')


class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    form_class = MovieForm
    template_name = 'CineBoard/movie_form.html'
    success_url = reverse_lazy('movie_list')


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    template_name = 'CineBoard/movie_confirm_delete.html'
    success_url = reverse_lazy('movie_list')