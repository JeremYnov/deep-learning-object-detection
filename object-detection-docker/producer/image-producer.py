from PIL import Image
import os 
from pathlib import Path
from utils import (set_logger, config_reader, acked)
from confluent_kafka import Producer
    
PARENT_PATH = os.fspath(Path(__file__).parents[1])
CONFIG_PATH = os.path.join(PARENT_PATH,"configurations","settings.ini")
KAFKA_CONFIG_DICT = config_reader(CONFIG_PATH, "kafka")
CRYPTO_TOPIC = config_reader(CONFIG_PATH, "app.settings")["topic_raw"]
LOGGER = set_logger("producer_logger")

from PIL import Image
import numpy as np 
from numpy import asarray

class ImageProducer(): 
    def __init__(self) -> None:
        pass

    def image_preprocessing(self, image_name:str):
        img = Image.open(f'{PARENT_PATH}/{image_name}').resize((300,300))
        img_np_array = asarray(img)
        return img_np_array
    
    def image_decode(self, numpy_image_array):
        pilImage =  Image.fromarray(numpy_image_array)
        pilImage.show()

    def produce_image(self):
        producer = Producer(KAFKA_CONFIG_DICT)
        np_array_image = self.image_preprocessing('street-image.jpg')
        print(np_array_image)
        try:
            producer.produce(
                topic=CRYPTO_TOPIC,
                value=np_array_image,
                callback=acked)
            producer.poll(1)
        except Exception as e:
            print(f'The problem is : {e}')

imageProducer = ImageProducer()
imageProducer.image_preprocessing('street-image.jpg')