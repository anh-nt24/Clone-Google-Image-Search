from feature_vector import *

is_train = False
if is_train:
    train()

img_path = 'Database/test/image_04252.jpg'

model = get_model()
s = get_feature_vector(model, img_path)
v = pickle.load(open(vector_file, 'rb'))
p = pickle.load(open(path_file, 'rb'))

d = np.linalg.norm(s-v, axis=1)
w = 10
idx = np.argsort(d)[:w] # the smaller the distance is, the more the same they are 
neighbor = dict({(p[i], d[i]) for i in idx})
imgs = [Image.open(i) for i in neighbor.keys()]

plt.imshow(Image.open(img_path))
plt.title('Queried Image')
dis = [*neighbor.values()]
fig = plt.figure(figsize=(15,7))
ax = fig.subplots(2,5)
for x in range(len(neighbor)):
    ax.flatten()[x].imshow(imgs[x])
    ax.flatten()[x].title.set_text(f'Độ giống: {round((1-dis[x])*100,2)}%')
    ax.flatten()[x].axis('off')
plt.show()
