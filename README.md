# Face-Recognition

This repository contains face recognition model using deep learning. 
Specifically, it uses a kind of matching network, FaceNet.
FaceNet: (https://arxiv.org/pdf/1503.03832.pdf)

For simplicity, this model uses open pre-trained models of FaceNet. It consists of Inception Modules.

## Requirement
Keras x.x.x.

Tensorflow x.x.x

OpenCV-python x.x.x

## File Description

* face_recognition_model.ipynb : Main model and applications of face recognition 
* fr_utils.py : It contains various utility functions for implementation of face recognition. - conv2d_bn: returns batch normalized convolutional blocks (up to 2 blocks) - load_weights: return pre-trained weight dictionary from weights directory. - load_weight_from_FaceNet: using above function, set pre-trained weights into model. - img_to_encoding: calculate inferred embedding vector of image. 
* inception_blocks_v2.py : Deep learning model with inception modules for FaceNet. It is implemented using Keras. 
* load_database.py : load image files and return embedding vectors of images with dictionary data structure. 
* weights : pre-trained weights of FaceNet. 
* train_test_file_for_pre_train : If you want to train in your own hand, use .h5 files in this directory.

