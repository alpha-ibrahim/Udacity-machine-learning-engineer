Pothole dataset compiled at Electrical and Electronic Department, Stelllenbosch University, 2015

The entire dataset consists of two different sets, one was considered to be simple and the other more complex.
These datasets do share some files and there are a few instances where two different images would have the same name.
Therefore, the appropriate measures need to be taken if the data is combined into one larger dataset.

Each of the datasets contain folders containing the training (positive and negative) images as well as a set of positive test images.

For each file, there is a number k after the file name, indicating the number of potholes labeled in the image.  Following are 4k numbers: each group of 4 represents one pothole by the image coordinates of its top left corner (x and y), and then the size (width and height of bounding box around pothole).

Please cite the following papers if you wish to use the dataset:
[1] S. Nienaber, M.J. Booysen, R.S. Kroon, “Detecting potholes using simple image processing techniques and real-world footage”, SATC, July 2015, Pretoria, South Africa.
[2] S. Nienaber, R.S. Kroon, M.J. Booysen , “A Comparison of Low-Cost Monocular Vision Techniques for Pothole Distance Estimation”, IEEE CIVTS, December 2015, Cape Town, South Africa.

The pothole detection task was found to be much easier if only the region in the image that contained the road was cropped and then used in detection such
as in the example pseudocode below.

%%%Pseudocode
%%%Crop rectangular region

*Downsample input image with a factor of two
*Rect roadSection(0,(1272/2+100)-150,(3680/2),(500/2+50))  //Example values

