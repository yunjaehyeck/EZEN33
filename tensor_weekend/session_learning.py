import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data

mnist = input_data.read_data_sets('MNIST_data/', one_hot=True)

#n_digits = 60
#n_epoch = 50  #epoch 에퍽, 에포크: 회전
#batch_size = 150

print("훈련 이미지:", mnist.train.images.shape)
print("훈련 라벨:", mnist.train.labels.shape)
print("테스트 이미지:", mnist.test.images.shape)
print("테스트 라벨:", mnist.test.labels.shape)
print("검증 이미지:", mnist.validation.images.shape)
print("검증 라벨:", mnist.validation.labels.shape)
print('\n')

mnist_idx=100

print('[label]')
print('one-hot encoding vector label =', mnist.train.labels[mnist_idx])
print('number label =', np.argmax(mnist.train.labels[mnist_idx]))
print('\n')

print('[image]')

for index, pixel in enumerate(mnist.train.images[mnist_idx]):
    if index % 28 == 0:
        print('\m' )
    else:
        print("%10f" % pixel, end="")
print('\n')

plt.figure(figsize=(5,5))
image = np.reshape(mnist.train.images[mnist_idx],[28,28])
plt.imshow(image, cmap='Greys') #cmap = 'Greys" 를 제거하면 컬러로 보임
plt.show()
