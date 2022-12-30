import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from retrieval.feature_vector import *

def cbir(img_path):
    model = get_model()
    s = get_feature_vector(model, img_path)
    data = collection.find()
    v, p = [], []
    for i in data:
        v.append(pickle.loads(i['vector']))
        p.append(i['path'])

    d = np.linalg.norm(s-v, axis=1)
    w = 50
    idx = np.argsort(d)[:w] # the smaller the distance is, the more the same they are 
    neighbor = dict({(p[i], d[i]) for i in idx})
    origin = img_path
    return [origin, neighbor]

if __name__ == '__main__':
    origin, neighbor = cbir('../Database/test/image_04252.jpg')
    plt.imshow(Image.open(origin))
    plt.title('Queried Image')
    dis = [*neighbor.values()]
    imgs = [*neighbor.keys()]
    fig = plt.figure(figsize=(15,7))
    ax = fig.subplots(2,5)
    for x in range(len(neighbor))[:10]:
        ax.flatten()[x].imshow(Image.open(imgs[x]))
        ax.flatten()[x].title.set_text(f'Độ giống: {round((1-dis[x])*100,2)}%')
        ax.flatten()[x].axis('off')
    plt.show()
