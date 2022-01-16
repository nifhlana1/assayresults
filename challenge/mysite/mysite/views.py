#from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse, JsonResponse
from  mysite.getCompoundDetails import getCompounds, getCompoundDetails, get_image

# from rest_framework.response import Response
# from rest_framework import status
# from pathlib import Path


@api_view(['GET', 'POST'])
def all_compoundsView(request):

    """Endpoint that returns all of the compounds available. Could use for dropdown in frontend to
    select more information.
    Returns HTTP for visual purposes, but would return JSON in reality."""

    if request.method == 'GET':

        try:
            all_compounds = getCompounds()

            return HttpResponse(all_compounds)

        except:
            #Would need better error handling here, in reality
            print("Error")


@api_view(['GET', 'POST'])
def compoundsResults(request):

    """Endpoint that takes in compoundinfo (passed in get request from frontend)
     and returns all assay for that specific compound.

     Front end could then easily query any relevant info from this endpoint, to render charts and info.

     Returns JSON response"""

    if request.method == 'GET':
        compound_id = request.GET.get("compound_id")
        try:
            compound_info = getCompoundDetails(compound_id)
            #print(compound_info)
            return JsonResponse(compound_info)

        except:
            # Would need better error handling here in reality
            print("Error")


@api_view(['GET', 'POST'])
def get_compound_image(request):

    """Endpoint that takes in compound id (passed in get request from frontent) and serves its image
    ---note, not complete for time reasons. Would convert to byte stream.

    Returns http response."""

    if request.method == 'GET':
        print("in get")
        compound_id = request.GET.get("compound_id")
        print(compound_id)
        image=get_image(compound_id)

        print(image)

    return HttpResponse(image, content_type="image/png")


