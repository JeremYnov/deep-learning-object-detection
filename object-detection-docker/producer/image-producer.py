from PIL import Image
import io
import os 
from pathlib import Path
from utils import (
    set_logger, config_reader, acked)
import zipfile
import matplotlib.pyplot as plt 
# from confluent_kafka import Producer
    
PARENT_PATH = os.fspath(Path(__file__).parents[1])

CONFIG_PATH = os.path.join(
    PARENT_PATH,
    "configurations",
    "settings.ini")

KAFKA_CONFIG_DICT = config_reader(
    CONFIG_PATH, "kafka")

class ImageProducer: 
    def __init__(self) -> None:
        pass

    def image_to_byte_array(self, image:Image):
        imgByteArr = io.BytesIO()
        image.save(imgByteArr, format=image.format)
        imgByteArr = imgByteArr.getvalue()
        print(imgByteArr)
        return imgByteArr

    def read_images(self):
        z = zipfile.ZipFile(f"{PARENT_PATH}/data.zip")
        for i in range(len(z.namelist())):
            file_in_zip = z.namelist()[i]
            if (".jpg" in file_in_zip or ".JPG" in file_in_zip):
                data = z.read(file_in_zip)
                dataEnc = io.BytesIO(data)
                print(dataEnc)
                img = Image.open(dataEnc)

    # def produce_image():
    #     producer = Producer()

imageProducer = ImageProducer()
imageProducer.read_images()