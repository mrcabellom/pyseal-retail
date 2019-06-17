FROM ubuntu:16.04 

# Install binary dependencies
RUN apt-get update && apt-get install -qqy \
	g++ \
	python3 \
	python3-dev \
	python3-pip \
	python3-tk \
	python-qt4 \	
	sudo \
        libdpkg-perl \
	--no-install-recommends

RUN mkdir -p HomomorphicEncryptionDemo
COPY /source/ /HomomorphicEncryptionDemo/source
COPY /lib /HomomorphicEncryptionDemo/lib
COPY /data/test_images/ /HomomorphicEncryptionDemo/data/test_images
COPY /models/fashion_mnist/ /HomomorphicEncryptionDemo//models/fashion_mnist/

RUN pip3 install --upgrade pip
RUN pip3 install setuptools
RUN pip3 install numpy
RUN pip3 install matplotlib
RUN pip3 install azure-storage==0.36.0
RUN pip3 install singleton-decorator==1.0.0
WORKDIR /HomomorphicEncryptionDemo/lib/
RUN pip3 install seal-2.3-cp35-cp35m-linux_x86_64.whl

WORKDIR /HomomorphicEncryptionDemo/source

# Clean-up
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

CMD ["python3", "main.py"]
