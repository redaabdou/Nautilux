from rest_framework.response import Response
from .models import Category, Equipment
from .serializers import CategorySerializer, EquipmentSerializer, EquipmentSerializerForPagination
from rest_framework import status
from django.http import Http404
from rest_framework.views import APIView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

class CategoryList(APIView):
    """
    List all category, or create a new Category.
    """
    
    def get(self, request, format=None):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)
    
    
    def post(self, request, format=None):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetail(APIView):
    """
    Retrieve, update or delete a Category instance.
    """
    
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404
    
    
    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)
    
    
    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class EquipmentList(APIView):
    """
    List all equipment, or create a new Equipment.
    """
    
    def get(self, request, format=None):
        equipment = Equipment.objects.all()
        serializer = EquipmentSerializer(equipment, many=True)
        return Response(serializer.data)

    
    def post(self, request, format=None):
        serializer = EquipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EquipmentDetail(APIView):
    """
    Retrieve, update or delete a Equipment instance.
    """
    
    def get_object(self, pk):
        try:
            return Equipment.objects.get(pk=pk)
        except Equipment.DoesNotExist:
            raise Http404
    
    
    def get(self, request, pk, format=None):
        equipment = self.get_object(pk)
        serializer = EquipmentSerializer(equipment)
        return Response(serializer.data)
    
    
    def put(self, request, pk, format=None):
        equipment = self.get_object(pk)
        serializer = EquipmentSerializer(equipment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def delete(self, request, pk, format=None):
        equipment = self.get_object(pk)
        equipment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoriesList(APIView):
    """
    List category
    """
    
    def post(self, request, format=None):
        parent = request.data.get("parent")
        if parent is not None:
            category_list = Category.objects.filter(parent=parent)
        else:
            category_list = Category.objects.filter()
        page_number = request.GET.get('page', 1)
        paginate_result = do_paginate(category_list, page_number)
        category_list = paginate_result[0]
        paginator = paginate_result[1]
        serializer = CategorySerializer(category_list, many=True)
        return Response(serializer.data)

class EquipmentsList(APIView):
    """
    List Equipment.
    {
    "categories": [
            1,3
        ],
        "quantity": {"min":222, "max":58888}
    }
    """
    
    def post(self, request, format=None):
        try:
            categories = request.data.get("categories")
            quantity = request.data.get("quantity")
            min = quantity.get("min")
            max = quantity.get("max")
        except:
            pass

        if categories is not None and quantity is not None :
            equipment_list = Equipment.objects.filter(quantity__gte=min).filter(quantity__lte=max).filter(categories__in=categories)
        elif quantity is not None:
            equipment_list = Equipment.objects.filter(quantity__gte=min).filter(quantity__lte=max)
        elif categories is not None:
            equipment_list = Equipment.objects.filter(categories__in=categories)
        else:
            equipment_list = Equipment.objects.filter()
        page_number = request.GET.get('page', 1)
        paginate_result = do_paginate(equipment_list, page_number)
        equipment_list = paginate_result[0]
        paginator = paginate_result[1]
        serializer = EquipmentSerializerForPagination(equipment_list, many=True)
        return Response(serializer.data)

def do_paginate(data_list, page_number):
        ret_data_list = data_list
        # display at most 30 records in each page.
        result_per_page = 30
        # build the paginator object.
        paginator = Paginator(data_list, result_per_page)
        try:
            # get data list for the specified page_number.
            ret_data_list = paginator.page(page_number)
        except EmptyPage:
            # get the lat page data if the page_number is bigger than last page number.
            ret_data_list = paginator.page(paginator.num_pages)
        except PageNotAnInteger:
            # if the page_number is not an integer then return the first page data.
            ret_data_list = paginator.page(1)
        return [ret_data_list, paginator]
