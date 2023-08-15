import os
image_scale = 1000
round_pose = 1 #----> less than number of image
scale = 1 #default is 1 ---->round 2:4k | 4/3:2k | 1:FHD **is depends on your webcam res
cam_type = "Hor" #"Hor = Horizontal cam, Ver = Vertical cam"
cam_number = #choose your camera devices
crop_Hor = 0
crop_Ver = 0
window_name = "Game pose"

























Parent_folder = os.path.dirname(__file__) + "\\"
image_folder = Parent_folder + "raw ref img\\put image here"
output_all_image = Parent_folder + "reference image deletable"
output_all_point = Parent_folder + "all_reference_poses_point_deletable.py"

# Parent_folder = "set your path folder here"
# Parent_folder = Parent_folder + "\\"
# image_folder_name = "raw ref img\\put image here"#don't change
# image_folder = Parent_folder+image_folder_name
# output_folder_name = "reference image deletable"#don't change
# ouput_all_image = Parent_folder+output_folder_name
# reference_file_name = "all_reference_poses_point_deletable.py" #don't change
# ouput_all_point = Parent_folder+reference_file_name
