import mxnet as mx
import gluoncv

# you can change it to your image filename
#이미지 파일 경로 설정하기
filename = './cat.jpeg'

# you may modify it to switch to another model. The name is case-insensitive
#원하는 모델로 수정히가
model_name = 'Xception'  #VGG16, DenseNet201, GoogLeNet, Xception, resnet101_v1d_0.73

# download and load the pre-trained model
#pre-train된 모델 다운로드, 로딩
net = gluoncv.model_zoo.get_model(model_name, pretrained=True)

# load image
img = mx.image.imread(filename)

# apply default data preprocessing
transformed_img = gluoncv.data.transforms.presets.imagenet.transform_eval(img)

# run forward pass to obtain the predicted score for each class
pred = net(transformed_img)

# map predicted values to probability by softmax
prob = mx.nd.softmax(pred)[0].asnumpy()

# find the 5 class indices with the highest score
ind = mx.nd.topk(pred, k=5)[0].astype('int').asnumpy().tolist()

# print the class name and predicted probability
print('The input picture is classified to be')
for i in range(5):
    print('- [%s], with probability %.3f.'%(net.classes[ind[i]], prob[ind[i]]))
