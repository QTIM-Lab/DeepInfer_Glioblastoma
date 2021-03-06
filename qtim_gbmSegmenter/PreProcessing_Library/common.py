
import glob
import os
import nibabel as nib
import numpy as np

def nifti_2_numpy(filepath):

    """ This and the function below are taken from nifti_util. Docker is having trouble installing matplotlib, which is
        imported in nifti_util, unfortunately.
    """

    img = nib.load(filepath).get_data().astype(float)
    return img

def save_numpy_2_nifti(image_numpy, reference_nifti_filepath=None, output_path=None, reference_affine=None):

    if reference_affine is None:
        nifti_image = nib.load(reference_nifti_filepath)
        reference_affine = nifti_image.affine
    output_nifti = nib.Nifti1Image(image_numpy, reference_affine)
    nib.save(output_nifti, output_path)

def run_test():
    return

if __name__ == '__main__':
    run_test()