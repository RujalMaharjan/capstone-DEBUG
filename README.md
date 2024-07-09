# capstone-DEBUG

# run minikube
minikube start

# to run services
kubectl apply -f deployment.yaml 
kubectl apply -f app-pod.yaml 
kubectl apply -f aiback-service.yaml 
kubectl apply -f service.yaml 

# to check status of pods
kubectl get pods -o wide

# to run application
minikube service aifront-service 
