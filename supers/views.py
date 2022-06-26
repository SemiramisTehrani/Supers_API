from rest_framework.decorators import api_view
from rest_framework.response import Response

from supertypes.models import SuperType

from .serializers import SuperSerializer
from .models import Super


from django.shortcuts import get_object_or_404
from rest_framework import status

from supers import serializers

#@api_view(['GET','POST'])
#def supers_list(request):
    
#    if request.method == 'GET' :

#        supers = Super.objects.all()
#        serializer = SuperSerializer(supers, many = True)
#        return Response(serializer.data)

#    elif request.method == 'POST' :
#         serializer = SuperSerializer(data = request.data)
#         serializer.is_valid(raise_exception = True)
#         serializer.save()
#         return Response(serializer.data, status = status.HTTP_201_CREATED)

#@api_view(['GET'])
#def super_detail(request, pk) :
#    print(pk)
#    return Response(pk)


@api_view(['GET','POST'])
def supers_list(request):
    if request.method == 'GET' :

        #super_name = request.query_params.get('super_type')
        #print(super_name)

        #queryset = Super.objects.all()

        #if super_name :
        #    queryset = queryset.filter(super_type__type = super_name)
        
        #serializer = SuperSerializer(queryset, many = True)
        #return Response(serializer.data)

        # aadding custom response : following Examples and Definitions
        appending_dict_example ={}
        appending_dict_example['name'] = 'Semi'
        print(appending_dict_example)   # {name : 'Semi'}

        super_types =SuperType.objects.all()

        custom_response_dictionary = {}

        for super_type in super_types :
            supers = Super.objects.filter(supertype_id = super_type.id)
            super_serializer = SuperSerializer(supers, many = True)

            custom_response_dictionary[super_type.name] = {
                "Type"   : super_type.type,
                "supers" : super_serializer.data
            }
        return Response(custom_response_dictionary)




    
    elif request.method =='POST' :
        serializer = SuperSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)





@api_view(['GET','PUT','DELETE'])
def super_detail(request, pk) :
    super = get_object_or_404(Super,pk=pk)
    if request.method == 'GET' :
        serializer = SuperSerializer(super);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SuperSerializer(super, data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)