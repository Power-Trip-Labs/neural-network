# Neural Network
A neural network library built without any AI libraries, only NumPy.

## How to Use
### Training
You have to set any images you want the model to train off of in the `train/` folder.

Then, run `train.py`. It will automatically take all the images and train the A.I. model. This could take a while!
It will store the output as a `model.pkl` file.
### Usage
You can now run `model.py`, with the only requirement being the `model.pkl` that you got from training.

It will ask for a `.png` file, and you can provide a relative or absolute path here. It will then find the closest image that matches your PNG.

Note that its output is the name of the image, so you might have to do some filtering to determine what the PNG is (bus) instead of a image name (bus3)
