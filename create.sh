kubectl create -f celery-flask-pod.yaml
kubectl create -f celery-flask-service.yaml
kubectl create -f celery-redis-pod.yaml
kubectl create -f celery-redis-service.yaml 
kubectl create -f celery-worker-pod.yaml
kubectl create -f celery-worker-service.yaml
kubectl create -f celery-flower-pod.yaml
kubectl create -f celery-flower-service.yaml
