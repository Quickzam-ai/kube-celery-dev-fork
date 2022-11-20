kubectl create -f deployments/celery-worker-deployment.yaml
kubectl create -f deployments/flask_application-service.yaml
kubectl create -f deployments/flask-application-deployment.yaml
kubectl create -f deployments/flower-deployment.yaml
kubectl create -f deployments/flower-service.yaml
kubectl create -f deployments/redis-deployment.yaml