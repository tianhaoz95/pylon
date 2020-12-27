# Self-hosted Machine Learning Platform

### Boot up K8 cluster

```bash
minikube start --cpus 6 --memory 32768 --disk-size=120g --driver=none
```

### Run Nvidia plugin for K8 cluster

#### With `kubectl` (for non-production)

```bash
kubectl create -f https://raw.githubusercontent.com/NVIDIA/k8s-device-plugin/v0.7.3/nvidia-device-plugin.yml
```

#### With `helm` (for production)

```bash
helm repo add nvdp https://nvidia.github.io/k8s-device-plugin
helm repo update
helm install --generate-name nvdp/nvidia-device-plugin
```

Then restart docker with:

```bash
systemctl daemon-reload
systemctl restart docker
```

### Run KubeFlow server

First `cd` into `[project_root]/[namespace]/[project_id]` and then:

```bash
kfctl apply -V -f https://raw.githubusercontent.com/kubeflow/manifests/master/kfdef/kfctl_k8s_istio.v1.2.0.yaml
```

### Port forward KubeFlow server

First `export` variables `KUBEFLOW_HOST` and `KUBEFLOW_PORT`, then:

```bash
kubectl port-forward --address $KUBEFLOW_HOST,localhost -n istio-system svc/istio-ingressgateway $KUBEFLOW_PORT:80
```

## FAQ

### The `conntrack` not installed

Error message:

```bash
* Using the none driver based on user configuration
X Sorry, Kubernetes v1.18.2 requires conntrack to be installed in root's path
Error: Command failed: sudo -E /home/runner/work/_temp/minikube start --vm-driver=none --kubernetes-version v1.18.2
```

Solution:

```bash
sudo apt-get install -y conntrack
```

Note: thanks to [this answer](https://github.com/manusa/actions-setup-minikube/issues/7#issuecomment-617419571).

### Juju permission denied

```bash
microk8s enable kubeflow
Password [63C2EBCP2ACRYGZMHZQ43RTXL8WORF]: 
Enabling dns...
Enabling storage...
Enabling dashboard...
Enabling ingress...
Enabling metallb:10.64.140.43-10.64.140.49...
Waiting for DNS and storage plugins to finish setting up
DNS and storage setup complete. Checking connectivity...
Bootstrapping...
Kubeflow could not be enabled:
ERROR cannot load ssh client keys: open /var/snap/microk8s/1864/juju/share/juju/ssh/juju_id_rsa: permission denied
Command '('microk8s-juju.wrapper', 'bootstrap', 'microk8s', 'uk8s')' returned non-zero exit status 2
```

Solution:

```bash
sudo chown -R $USER /var/snap/microk8s/current/juju/share/juju/
```

## References

* [awesome-production-machine-learning](https://github.com/EthicalML/awesome-production-machine-learning)
* [nvidia-docker](https://github.com/NVIDIA/nvidia-docker)
* [Nvidia Cloud Native Technologies Docs](https://docs.nvidia.com/datacenter/cloud-native/index.html)
* [Minikube: use the none driver docs](https://minikube.sigs.k8s.io/docs/tutorials/nvidia_gpu/#using-the-none-driver)
* [KubeFlow with Minikube docs](https://www.kubeflow.org/docs/started/workstation/minikube-linux/)
