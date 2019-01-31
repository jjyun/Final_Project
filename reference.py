# USAGE
# python classify.py --model doggiedex.model --labelbin lb.pickle --image examples/XXX.jpg

# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import pickle
import cv2
import os
import classify2
import sys

model = "doggiedex.model"
labelbin = "lb.pickle"
dogpic = "examples/dog8.jpg"

classify2.classify(model,labelbin,dogpic)