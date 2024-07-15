# capstone-DEBUG

# run minikube
```bash
minikube start
```

# to run services
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
```
