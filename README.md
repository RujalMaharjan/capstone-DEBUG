# capstone-DEBUG

# run in awscli
```bash
eksctl create cluster --name capcluster --region ca-central-1 --nodegroup-name standard-workers --node-type t2.micro --nodes-min 4 --nodes-max 10 --nodes 4
aws eks --region ca-central-1 update-kubeconfig --name capcluster
```

# to run services in aws cli
```bash
kubectl apply -f deployment.yaml 
kubectl apply -f app-pod.yaml 
kubectl apply -f aiback-service.yaml 
kubectl apply -f service.yaml 
```

# to check status of pods in awscli
```bash
kubectl get pods -o wide
```

# to run application
```bash
kubectl get services -o wide
```
# to delete cluster
```bash
eksctl delete cluster -n capcluster
```

# run locally

# run minikube
```bash
minikube start
```

# to run services locally
```bash
kubectl apply -f deployment.yaml 
kubectl apply -f app-pod.yaml 
kubectl apply -f aiback-service.yaml 
kubectl apply -f service.yaml 
```

# to check status of pods
```bash
kubectl get pods -o wide
```

# to run application
```bash
minikube service aifront-service 
kubectl get services -o wide
```
