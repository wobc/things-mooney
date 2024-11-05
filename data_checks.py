# run this script locally to make sure you have downloaded the data correctly

import os
import numpy as np

# check if the stim folder exists
def check_data():
    if not os.path.exists('stim/'):
        print('Images folder not found. Please download the data first.')
    else:
        print('Images folder found! Checking data integrity...')
    

# check total amount of imges in stim folder
def check_total_images():
    files_gray = os.listdir('stim/gray')
    # check only files than end with "gray.jpg"
    files_gray = [f for f in files_gray if f.endswith('gray.jpg')]
    print(f'Total number of gray images: {len(files_gray)}')
    
    files_mooney = os.listdir('stim/mooney')
    print(f'Total number of mooney images: {len(files_mooney)}')

    # if number of mooney images is not equal to number of gray images, throw an error
    if len(files_gray) != len(files_mooney):
        print('Number of mooney images is not equal to number of gray images. Please download the data again.')
        return
    else:
        print('Same number of gray and mooney images.')
        
    # check all images have some size
    for f in files_gray:
        if os.path.getsize(f'stim/gray/{f}') == 0:
            print(f'{f} has size 0.')
            return
    print('Image files seem to be uncorrupted (check manually if needed)')
    print("\nReady to go!")



check_data()
check_total_images()



        

