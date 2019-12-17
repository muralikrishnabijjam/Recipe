from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import RecipeItems
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RecipeItemsForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Helloworld'}
        return Response(content)


# def login_view(request):
#     if request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             login(request, user)
#             return HttpResponseRedirect(reverse('recipes:index'))
#         else:
#             return HttpResponse("Invalid Details")
#     return render(request, 'recipes/login.html')
#
#
# def logout_view(request):
#     return HttpResponseRedirect(reverse('recipes:login'))
#
#
# def index(request):
#     name = RecipeItems.objects.all()
#     context = {'name': name}
#     return render(request, 'recipes/index.html', context)
#
#
# def details(request, name_id):
#     name = get_object_or_404(RecipeItems, pk=name_id)
#     check = {'name': name}
#     return render(request, 'recipes/details.html', check)
#
# @login_required(login_url='/recipes/create')
# def create_recipes(request):
#     if request.method == "POST":
#             form = RecipeItemsForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 return HttpResponseRedirect(reverse('recipes:index'))
#             else:
#                 form = RecipeItemsForm
#             return render(request, "recipes/create.html", {'form': form})
#             # RecipeItems.objects.create(
#             #     name=request.POST["name"],
#             #     ingredients=request.POST["ingredients"],
#             #     process=request.POST["process"]
#             # )
#             # return HttpResponseRedirect(reverse('recipes:index'))
#     return render(request, "recipes/create.html")
#
#
# def register(request):
#     if request.method == "POST":
#         User.objects.create_user(
#                 username=request.POST["username"],
#                 email=request.POST["email"],
#                 password=request.POST["password"],
#             )
#         father_name = request.POST["father_name"],
#         dob = request.POST["dob"]
#         return HttpResponseRedirect(reverse('recipes:login'))
#     return render(request, 'recipes/register.html')
#
#     # def delete_view(request, del_id):
#     #     a = get_object_or_404(RecipeItems, pk=del_id)
#     #     a.delete()
#     #     return HttpResponseRedirect(reverse('recipes:index'))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#


















































































































































































































































































































































































































































































































































































































































































































































