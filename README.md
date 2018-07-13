# Kubeconfig merge script

This script is intended to be used when needing to merge multiple kubernetes config files into one.

## How use it

First, install pyyaml

```
pip install -r requirements.txt
```

Then:

```
python kcm.py [all config files next to each other]
```

Example:

```
python kcm.py minikube okeconfig
```

It will create a file called mkubeconfig in the current directory