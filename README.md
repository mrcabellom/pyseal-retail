# Microsoft Responsible AI

## Index
1. About this project
1. To create the virutal environment
1. Data
1. To launch Jupyter notebook
1. How to run the demo
1. Further reading

## About this project
Homomorphic encrypytion is a form of encryption that allows computation on ciphertexts, generating an encrypted result which, when decrypted, matches the result of the operations as if they had been performed on the plaintext. This kind of encryption can be used for privacy-preserving outsourced storage and computation. 

In this repository, we will apply homomorphic encryption to the Fashion MNIST dataset.

## To create the virtual environment
*Note*: This step is not required to launch the demo. 

To create the virtual environment used in this project and needed to generate the weigths of the training network, you need to have installed anaconda. If you don't have it, you can download it in this [link](https://www.anaconda.com/download/).

Once this is done, the virtual environment can be created by using the *environment.yml* file, which contains all pip and conda dependencies' packages. To do so:

`conda env create --file environment.yml`

Once the environment is created, to activate it do the following: 

`activate responsibleai-he`

To deactivate it: 

`deactivate responsibleai-he`

To update the environment with new dependencies:

`conda env update --file environment.yml`

Keep in mind that to update the environment it must be activated.

## Data
Right now, the data used is stored in an Azure Storage Account. In order to run the demo, you will need to create in your Azure account an storage account. Inside the storage account, create a container, and inside this container create the folders data and models, which should have the same files as the ones in this repo.

## To launch Jupyters notebook

*Note*: Do not launch the jupyter notebook for demo purposes as it will update the weights used in the prediction network. 

To launch the jupyter notebook where the training network is, please create the virtual environment first. Once you have created the virtual environment, type in your console the following:

`jupyter notebook`

This will open your navigator with the directory you are in, you now just need to select the notebook you want to open. Please, make sure that the correct environment is being used. If not, select it and restart the kernel after.

## How to run the demo
To run the demo, you need to have Docker install in your computer. If you don't have it, you can download it in this [link](download.docker.com) and follow the instructions to install it in Windows [here](https://docs.docker.com/docker-for-windows/install/).

Once Docker is running, to run the network you just need to execute the following commands in your console:

``docker build -t <image_name>:<tag> -f Dockerfile .``

Once the Docker image is build, execute the following command to run it: 

``docker run --env IMAGES_FOLDER_ENCRYPTION="data/test_images" -it <image_name>:<tag>``

In Windows, you can also directly run ``build_docker.bat``, which will create the image, followed by ``run_docker_windows.bat`` which will run it.

This last command will start the demo. Please note that no images are display during the demo, however its labels are presented. Below, you can see a table with the different labels and its corresponding description:

| Label | Description |
| --- | --- |
| 0 | T-shirt/top |
| 1 | Trouser |
| 2 | Pullover |
| 3 | Dress |
| 4 | Coat |
| 5 | Sandal |
| 6 | Shirt |
| 7 | Sneaker |
| 8 | Bag |
| 9 | Ankle boot |

Therefore, when saying ``True label: 1`` it means that the image passed is a trouser and ``Prediction: 1`` means that the network predicted that the image passed to it belongs to the trouser class.

It takes around 13 minutes to obtain the prediction of one image. Enjoy!


## Further reading
- [Homomorphic encryption](https://www.microsoft.com/en-us/research/project/microsoft-seal/)
- [Fashion-MNIST](https://github.com/zalandoresearch/fashion-mnist)