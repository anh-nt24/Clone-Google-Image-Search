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
2. run 'python3 feature_vector' to extract all images feature and store in database (MongoDB)
3. change directory to backend folder 'cd backend'
4. run 'python3 app.py' to deploy on web
5. open localhost to view your website
 
## Results:
![image](https://user-images.githubusercontent.com/106876168/209541095-902ec9ff-b1ba-478e-acd0-75d52e98b0b3.png)

![image](https://user-images.githubusercontent.com/106876168/209541128-e49f26fd-a167-4fe3-b881-ca93f5eab78a.png)


