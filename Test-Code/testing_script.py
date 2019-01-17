"""Read folder image and return label."""

# imports
from os import listdir
import print_functions_for_lab_checks as lab_check


def get_pet_labels(image_dir):
    """
    Extract the labels from a filename.

    Creates a dictionary of pet labels based upon the filenames of the image
    files. Reads in pet filenames and extracts the pet image labels from the
    filenames and returns these labels as petlabel_dic. This is used to check
    the accuracy of the image classifier model.
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by pretrained CNN models (string)
    Returns:
     petlabels_dic - Dictionary storing image filename (as key) and Pet Image
                     Labels (as value)

    """
    # Create list with filename from pet_images folder
    file_name = listdir(image_dir)

    # Create empty dictionary to store filenames and labels
    petlabels_dic = dict()

    # Loop through list file_name
    for item in range(0, len(file_name)):
        # Discard any system file that starts with a dot
        if file_name[item][0] != ".":
            # Create variable and add item formatted
            image_name = file_name[item].lower().split("_")
            # Create variable to hold temporaly the labels
            pet_label = ""
            # Loop through image_name
            for word in image_name:
                if word.isalpha():
                    # Add if item is an alphabetic character
                    pet_label += word + " "
            # Remove whitespace from the end
            pet_label = pet_label.strip()
            # Create Dictionary
            # Check if file is not repeated in the dict and add it
            if file_name[item] not in petlabels_dic:
                petlabels_dic[file_name[item]] = pet_label
            else:
                print("Warning: Duplicate files exist in directory")
    return (petlabels_dic)


answers_dic = get_pet_labels("pet_images/")

# Test the label dictionary (TODO: To be removed later)
lab_check.check_creating_pet_image_labels(answers_dic)
