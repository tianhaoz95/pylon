# Linux Workstation Setup

## Choose a distro

* Ubuntu
* Linux Mint
* Zorin OS
* Pop!_OS

## GitHub setup

* Generate `ssh` key: [instructions](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)
* Add `ssh` key: [instructions](https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account)

## Python setup

* Install `pip`: https://bootstrap.pypa.io
    * For Python 2.7: https://bootstrap.pypa.io/2.7/get-pip.py
    * For the latest Python: https://bootstrap.pypa.io/get-pip.py

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3.8 get-pip.py
```

## Flutter setup

If `flutter doctor -v` cannot find Android Studio, use the following command:

```bash
flutter config --android-studio-dir=$PATH_TO_INSTALLATION
```

## SSH setup

### Local network discovery

### Credentials

### SSH config

### Multiple workstations

## Generic setup

### Install Docker

Check out the instructions [here](https://docs.docker.com/engine/install/ubuntu/).

Also, don't forget to set up non-root docker with the instructions [here](https://docs.docker.com/engine/install/linux-postinstall/). This will make your life much easier.

## Domain specific setup

### ML

#### ML infra

##### Install Nvidia tools

* Install Nvidia driver, CuDNN and CUDA: check [here](https://www.tensorflow.org/install/gpu#ubuntu_1804_cuda_110) for instructions.

##### Install TensorFlow

##### Install Nvidia container support

#### ML platform

## FAQ

### Should I setup VNC?
