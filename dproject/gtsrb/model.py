import matplotlib.pyplot as plt
import glob
from skimage.color import rgb2lab
from skimage.transform import resize
from collections import namedtuple
import numpy as np

class Gtsrb:

    def __init__(self):
        np.random.seed(100)
        self.N_CLASSES = 43
        self.RESIZE_IMAGE =(32, 32)
        self.Dataset = namedtuple('Dataset', ['X', 'y'])

    def read_dataset(self, rootpath, n_labels, resize_to):
        images = []
        labels = []

        for c in range(n_labels):
            full_path = rootpath + '/' + format(c, '05d') + '/'
            for img_name in glob.glob(full_path + "*.ppm"):
                img = plt.imread(img_name).astype(np.float32)
                img = rgb2lab(img / 255.0)[:, :, 0]
                if resize_to:
                    img = resize(img,
                                 resize_to,
                                 mode='reflect')
                label = np.zeros((n_labels,), dtype=np.float32)
                label[c] = 1.0
                images.append(img.astype(np.float32))
                labels.append(label)
         return self.Dataset(
              X = self.to_tf_format(images).astype(np.float32),
              y = np.matrix(labels).astype(np.float32)
         )
    """
    모델 훈련과 예측
    모델 훈련 데이터의 미니배치를 생성하는 함수; 
    훈련을 반복할 때마다 훈련 데이터셋에서 추출된 표본의 
    미니배치를 삽입. 
    관측치, 레이블, 배치 크기를 인수로 가져와 
    미니배치 생성기를 반환하는 함수를 생성한다.
    """
     def minibatcher(self, X, y, batch_size, shuffle):
         assert X.shape[0] == y.shape[0]
         n_samples = X.shape[0]

        if shuffle:
           idx = np.random.permutation(n_samples)
        else:
            idx = list(range(n_samples))
        print("인덱스 값: {}".format(idx))
        temp = int(
            np.ceil(n_samples / batch_size) # ceil 무조건 올림. 3.1이면 4
        )
        print("temp 값: {]".format(temp))
        for k in range(temp):
        print("---- k is {}  ----".format(k))
        from_idx = k * batch_size
        print("---- from_idx is {} ---- ".format(from_idx))
        to_idx = (k+1)*batch_size
        print("---- to_idx is {} -----".format(to_idx))
        yield X[idx[from_idx: to_idx,:, :, :], y[idx[from_idx:to_idx]]



    @staticmethod
     def to_tf_format(imags):
        return np.stack([img[:, :, np.newaxis] for img in imgs],
                        axis=0).astype(np.float32)

