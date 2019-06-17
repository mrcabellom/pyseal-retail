import matplotlib.pyplot as plt
import numpy as np
import os
import sys
import time

from encryption.encryption_config import config
from encryption.encryption_handler.encryption_handler import EncryptionHandler
from networks.server_net.predictor_net import Predictor
from services.storage.blob_storage import BlobStorageService
from settings import AZURE_STORAGE


def main():

    storage = BlobStorageService(AZURE_STORAGE['STORAGE_ACCOUNT_NAME'], AZURE_STORAGE['STORAGE_ACCOUNT_KEY'])
    blobs = storage.list_blobs(AZURE_STORAGE['CONTAINER'])

    # Download test images and weights
    for blob in blobs:
        if os.environ['IMAGES_FOLDER_ENCRYPTION'] in blob.name or 'models' in blob.name:
            storage.download_blob(AZURE_STORAGE['CONTAINER'], blob.name, '../' + blob.name)

    debug = False
    if len(sys.argv)>0:
        if sys.argv[0] == 'debug':
            debug = True

    images_folder = os.path.join('../', os.environ['IMAGES_FOLDER_ENCRYPTION'])
    for image in os.listdir(images_folder):
        print('True label: {}'.format(image))
        imfile = os.path.join(images_folder,image)
        test_im = np.load(imfile)

        plt.imshow(np.reshape(test_im,(28,28)))
        plt.show()
        start1=time.clock()
        handler = EncryptionHandler(config)
        op = handler.package

        #encrypt image
        ln = test_im.shape[0]
        start = time.clock()
        encrypted_image = []
        for i in range(ln):
            encrypted_image.append((op.Ciphertext()))
            handler.encryptor.encrypt(handler.encoder.encode(test_im[i]), encrypted_image[i])
        print("time taken for encrypting image:  " + (str)(time.clock() - start)+"s")
        print("Noise budget in fresh encryption: " + (str)(handler.decryptor.invariant_noise_budget(encrypted_image[100])) + " bits")
    
        #call the predictor 
        predictor = Predictor(op,debug= debug, handler= handler)
        logits = predictor.predict_image(encrypted_image)

        start = time.clock()
        dec_logits=(handler.get_matrix(logits))
        print("Prediction : "+(str)(np.argmax(dec_logits)))
        print("time taken for decrypting image:  " + (str)(time.clock() - start)+"s")
        print("total time taken for the network: " + (str)(time.clock() - start1)+"s")


if __name__ == '__main__':
    main()