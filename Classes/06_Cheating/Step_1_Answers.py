
#####
# Step 1 - ModelBuilder to Python Script
#####

# Task 1 - Using the provided model - Step_1_toolbox.zip, export the Model to a python script and paste below.
# In Model Builder, go to the menu item Model > Export > To Python Script.

# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2021-03-12 12:31:57
"""
import arcpy

def Model():  # Find Areas Suitable for Development

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = True

    Roads = r"C:\Data\Course_ArcGIS_Python\Classes\06_Cheating\ProFolder_Step_1_toolbox\Step_1_data\Step_1_data\RI_Roads.shp"
    Places = r"C:\Data\Course_ArcGIS_Python\Classes\06_Cheating\ProFolder_Step_1_toolbox\Step_1_data\Step_1_data\Places.shp"
    State_Boundary = r"C:\Data\Course_ArcGIS_Python\Classes\06_Cheating\ProFolder_Step_1_toolbox\Step_1_data\Step_1_data\State_Boundary_1997.shp"

    arcpy.env.workspace = r"C:\Data\Course_ArcGIS_Python\Classes\06_Cheating\ProFolder_Step_1_toolbox\Step_1_data\Step_1_data"

    # Process: Buffer roads (Buffer) (analysis)
    Buffered_Roads = "RI_Roads_Buffer.shp"
    arcpy.analysis.Buffer(in_features=Roads, out_feature_class=Buffered_Roads, buffer_distance_or_field="10 Miles", line_side="FULL", line_end_type="ROUND", dissolve_option="ALL", dissolve_field=[], method="PLANAR")

    # Process: Buffer places (Buffer) (analysis)
    Buffered_Places = "Places_Buffer.shp"
    arcpy.analysis.Buffer(in_features=Places, out_feature_class=Buffered_Places, buffer_distance_or_field="10 Miles", line_side="FULL", line_end_type="ROUND", dissolve_option="ALL", dissolve_field=[], method="PLANAR")

    # Process: Buffered data intersected (Intersect) (analysis)
    Buffered_data_intersected_output = "RI_Roads_Buffer_Intersect.shp"
    arcpy.analysis.Intersect(in_features=[[Buffered_Roads, ""], [Buffered_Places, ""]], out_feature_class=Buffered_data_intersected_output, join_attributes="ALL", cluster_tolerance="", output_type="INPUT")

    # Process: Clip (Clip) (analysis)
    Suitable_Areas_for_Development = "State_Boundary_1997_Clip.shp"
    arcpy.analysis.Clip(in_features=Buffered_data_intersected_output, clip_features=State_Boundary, out_feature_class=Suitable_Areas_for_Development, cluster_tolerance="")

if __name__ == '__main__':
    Model()