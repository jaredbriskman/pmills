# Cribbed from this tutorial: https://www.pyimagesearch.com/2017/05/22/face-alignment-with-opencv-and-python/

# import the necessary packages
from imutils.face_utils import FaceAligner
from imutils.face_utils import rect_to_bb
import argparse
import imutils
import dlib
import cv2
import os
import sys
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
help="path to facial landmark predictor")
ap.add_argument("-i", "--images", required=True,
help="path to image folder")
ap.add_argument("-o", "--output", required=True,
help="path to output folder")
args = vars(ap.parse_args())

#https://stackoverflow.com/questions/120656/directory-tree-listing-in-python
def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

# initialize dlib's face detector (HOG-based) and then create
# the facial landmark predictor and the face aligner
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])
fa = FaceAligner(predictor, desiredFaceWidth=1600)

# load the input image, resize it, and convert it to grayscale
folder = args["images"]
for f in listdir_fullpath(folder):
    # Only read images
    if not f.endswith(".jpg"):
        continue
    image = cv2.imread(f)
    image = imutils.resize(image, width=1600)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
     
    # detect faces in the grayscale image
    rects = detector(gray, 2)

    # loop over the face detections
    for rect in rects:
            # extract the ROI of the *original* face, then align the face
            # using facial landmarks
            (x, y, w, h) = rect_to_bb(rect)
            bigrect = dlib.rectangle(top=(y-500), bottom=(y+h+500), left=(x-500), right=(x+w+500))
            center_y = rect.bottom() - (rect.bottom() - rect.top())/2
            center_x =  rect.right() - (rect.right() - rect.left())/2

            if center_y < 350 and center_x < 600:

                faceOrig = imutils.resize(image[y:y + h, x:x + w], width=1600)
                faceAligned = fa.align(image, gray, bigrect)
         
                f_new = f.split(".")[0].split("/")[-1] + "_aligned.jpg"
                output_folder = args["output"]
                cv2.imwrite(os.path.join(output_folder, f_new), faceAligned)
                print("saved image " + f_new)
