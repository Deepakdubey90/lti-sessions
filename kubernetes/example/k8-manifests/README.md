# Creating secret

```
kubectl create secret docker-registry docker-hub \
  --docker-server=docker.io \
  --docker-username=akhilputhiry \
  --docker-password=************ \
  --docker-email=akhilputhiry@gmail.com
```


# Running curl

```
kubectl run curl \
  --stdin \
  --tty \
  --image=appropriate/curl \
  --command \
  -- /bin/sh
```
