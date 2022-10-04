from re import A
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from .models import Category, Material, Profile, Comment
from .forms import CommentForm

def landing(request):
    return render(request, 'curriculum/landing.html', {})

def categories(request):
    all_category = Category.objects.all()
    context = {"all_category": all_category}
    return render(request, 'curriculum/categories.html', context)

# input: request, category_id
# request - something we pass from urls.py
# category_id is passed from our browser address (http://localhost:8000/category/1/)
# in this case, category_id = 1
def category(request, category_id):
    # Category (capital C) is the Category MODEL
    # .get() we are getting ONE object from the Category database
    # .get(pk=category_id) we are getting the Category that has a primary key (pk) of 1
    category = Category.objects.get(pk=category_id)
    
    # METHOD 1 of getting the materials
    # I am looking at the Material databse, and finding ALL the materials with the category primaru key of 1
    # for the material model, we have category (foreign key), name, media_type as ATTRIBUTES
    # category__pk --> it is getting the category OBJECT that is associated with the material, and getting the primary of that category object
    # kind of like the SQL WHERE statement
    materials = Material.objects.filter(category__pk = category_id)

    # # METHOD 2 of getting the materials
    # # Step 1: get all the materials
    # all_materials = category.materials.all()
    # # Step 2: create an empty of materials we want
    # materials = []
    # # Step 3: loop through all the materials and find the category's primary key
    # for i in range(len(all_materials)):
    #     this_material = materials[i]
    #     category_pk = this_material.category.pk
    #     # check to see whether it matches with category_id
    #     if category_pk == category_id:
    #         materials.append(this_material)

    # METHOD 1 of getting all the media type
    # Step 2: we create a new set (unique list)
    material_types = set()
    # Step 3: we are looping through ALL the materials, 
    for i in range(len(materials)):
        material_types.add(materials[i].media_type)
    
    ## METHOD 2 of getting all media type
    # material_types = set([material.media_type for material in materials])

    context = {"category": category, "materials": materials, "types": material_types}
    return render(request, 'curriculum/category.html', context)

def material(request, category_id, material_id):
    material = Material.objects.get(pk = material_id)
    category = Category.objects.get(pk = category_id)
    category_name = material.category.name
    material_name = material.name
    media_type = material.media_type
    comments = Comment.objects.filter(material__pk = material_id)

    form = CommentForm()

    context = {"category_name": category_name, "material_id": material.id, "name": material_name, "type": media_type, "comments": comments, 'form': form}
    return render(request, 'curriculum/material.html', context)

def comment(request, material_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = Comment(text=request.POST['comment'], material_id=material_id, profile_id=1)
            new_comment.save()
            return redirect(material, category_id=1, material_id=material_id)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CommentForm()

    return redirect(material, category_id=1, material_id=material_id)