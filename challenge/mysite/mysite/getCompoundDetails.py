import json
import os
from django.conf import settings
from pathlib import Path



def getCompounds():

    """This function (used in endpoint) returns all of the compound id's
    that are available. Useful in dropdowns etc at frontend.

    ***Would probably return JSON in reality instead of http"""

    #Alter base bath for use with Django server
    base_dir=settings.BASE_DIR
    file_path=os.path.join(base_dir,'mysite','compounds.json')

    print(os.path)
    compounds_in_file=[]

    # response is starting with a BOM (ï»¿) so change encoding
    with open(file_path, encoding='utf-8-sig') as data_file:
        data = json.load(data_file)

        for i in data:
            compounds_in_file.append(str(i['compound_id'])+", ")

    print(compounds_in_file)
    return compounds_in_file



def get_image(compound_id):

    """Takes in compound id and
    returns associated image.
    (Called automatically and served on another endpoint
    when a compound id is requested.)"""

    print("in image")
    # Alter base bath for use with Django server
    base_dir = settings.BASE_DIR

    # get associated images
    image = os.path.join(base_dir, 'mysite', 'static', 'images', str(compound_id) + ".png")
    #print(str(image))

    return image



def getCompoundDetails(compound_id):

    """Function that takes in compound id. Returns all related assay results information.
    Could query relevant sections in frontend to easily render charts/images etc.
    Reads in the compounds json file. For larger files, could instead change it to read from a database/models"""

    assay_result = {}

    base_dir = settings.BASE_DIR
    file_path = os.path.join(base_dir, 'mysite', 'compounds.json')

    # response is starting with a BOM ï»¿ so change encoding
    with open(file_path, encoding='utf-8-sig') as data_file:
        data = json.load(data_file)

        for compound_info in data:
            if str(compound_info['compound_id']) == compound_id:
                smiles=compound_info['smiles']
                assay_result['smiles']=smiles

                molecular_weight=compound_info['molecular_weight']
                assay_result['molecular_weight']=molecular_weight

                ALogP=compound_info['ALogP']
                assay_result['ALogP']=ALogP

                molecular_formula=compound_info['molecular_formula']
                assay_result['molecular_formula']=molecular_formula

                num_rings=compound_info['num_rings']
                assay_result['num_rings']=num_rings

                image=compound_info['image']
                assay_result['image']=num_rings

                assay_results_dict=compound_info['assay_results']
                assay_result['assay_results_dict']=assay_results_dict


        #print(assay_result)

        return assay_result


def getAssayResults(assay_results_dict):

    """This function takes in the dictionary of all assay results and
    returns just the result"""

    result = []
    for i in assay_results_dict:
        result_id=i['result_id']
        result=i['result']
        print(result_id,":",result)
        #append the resultid:result to results list
        result.append(result_id +":"+result)

    return result








