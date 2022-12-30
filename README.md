# Clone-Google-Image-Search

This repo is a demo of google image searching, using a simple technique in computer vision content based image retrieval

## Diagram
![image](https://user-images.githubusercontent.com/106876168/209540082-75cf5a2a-0fd4-44e6-8073-f29e993df797.png)

* How it works?
  * Preparing a dataset and preprocessing
  * Extracting feature of each image and store in database as vectors
  * A user give an image to search, the system will extract its feature
  * Computing L2 norm (Euclidean distance) to get their similarity as formula:
    ```math
      d(s,v) = \sqrt{\sum_{i=1}^n (v_i - s_i)^2}
    ```
        where:
          s, v as 2 vectors
          n: n-space
   * The less the distance is, the more similar they are
   * Returning similar images
  
## About the project:
  - dataset source: [here](https://www.robots.ox.ac.uk/~vgg/data/flowers/102/index.html)
  - model to extract: mobilenet
  - required libraries: Tensorflow, keras, ngrok, flask
  
## How to use:
1. prepare a dataset and create a folder structure
2. enter `mongod` and connect to MongoDB
3. run `python3 feature_vector` to extract all images feature and store in database
4. change directory to backend folder `cd backend`
5. run `python3 app.py` to deploy on web
6. open localhost to view your website
 
## Results:

![image](https://user-images.githubusercontent.com/106876168/210039629-989ae36e-2cd5-42df-9d84-cca2dcc13bae.png)

![image](https://user-images.githubusercontent.com/106876168/210039651-196757e1-33ee-4f6d-a591-2ac36ccc809d.png)




