from django.shortcuts import render, redirect

from myapp.models import Movie

from django.views.generic import View

from myapp.forms import MovieForm

# Create your views here.


# view for listing all movies

# url:  localhost:8000/movies/all

# method: get()

# def movie_list_view(request, *args, **kwargs):

#     qs = Movie.objects.all()

#     return render(request, 'movie_list.html', {'data': qs})

class MovieListView(View):

    def get(self, request, *args, **kwargs):

        qs = Movie.objects.all()

        return render(request, 'movie_list.html', {'data': qs})
    

# url: localhost:8000/myapp/movies/add/
# method: get, post
    
class MovieCreateView(View):

    def get(self, request, *args, **kwargs):

        form = MovieForm()

        return render(request, 'movie_add.html', {'form':form})
    
    def post(self, request, *args, **kwargs):

        form = MovieForm(request.POST, files=request.FILES)
        
        if form.is_valid():

            # form.save()

            data = form.cleaned_data

            Movie.objects.create(**data)

            return redirect('movie-list')

        return render(request, 'movie_add.html', {'form': form})



# url: localhost:8000/myapp/movies/{id}/
# method: get()

class MovieDetailView(View):

    def get(self, request, *args, **kwargs):
        
        # print(kwargs) # kwargs = {'pk': 4}

        id = kwargs.get('pk')

        qs = Movie.objects.get(id=id)

        return render(request, 'movie_detail.html', {'data': qs})



# Movie delete view
# url: localhost:8000/myapp/movies/{id}/remove
# method: get()
    
class MovieDeleteView(View):

    def get(self, request, *args, **kwargs):

        id = kwargs.get('pk')

        Movie.objects.get(id=id).delete()

        return redirect('movie-list')
     

# Movie update view
# url: localhost:8000/myapp/movies/{id}/change/    
# method: get, post
    
class MovieUpdateView(View):

    def get(self, request, *args, **kwargs):

        id = kwargs.get('pk')

        movie_object = Movie.objects.get(id=id)

        form = MovieForm(instance=movie_object)   # inorder to use 'instance' we should be using ModelForm of Django

        # print(form)

        return render(request, 'movie_edit.html', {'form':form})
    

    def post(self, request, *args, **kwargs):

        id = kwargs.get('pk')

        movie_object = Movie.objects.get(id=id)

        form = MovieForm(request.POST, files=request.FILES, instance=movie_object)

        

        if form.is_valid():

            form.save()

            return redirect('movie-list')
        
        else:

            return render(request, 'movie_edit.html', {'form':form})
        


