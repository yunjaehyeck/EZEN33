from gtsrb.trainer import Trainer
from gtsrb.model import Gtsrb


if __name__ =='__main':
    model = Gtsrb()
    dataset = model.read_dataset(
        'images/',
        model.N_CLASSES,
        model.RESIZE_IMAGE)
    t = Trainer(model)
    trainer.execute()
