This is celery backend dev area

**Links:** 
* [**Simple Flask**](http://143.244.142.58:5000/simple_start_task)
* [**FLOWER**](http://143.244.142.58:5556/dashboard)


# Kompose: [**link**](https://github.com/kubernetes/kompose)

## Install: 
```python 
# first run this
curl -L https://github.com/kubernetes/kompose/releases/download/v1.27.0/kompose-linux-amd64 -o kompose

# change the permission to execute 
chmod +x kompose

# move to kompose path for read the binary file!
sudo mv ./kompose /usr/local/bin/kompose
```

## To run this: 
```python 
kompose convert -o folder_name/
```


# First deployment then service. 