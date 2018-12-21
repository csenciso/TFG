#!/usr/bin/env bash

#Creo la imagen
docker build -t dialog-controller .
#docker run -p 0.0.0.0:8080:8080 dialog-controller

#Taggeo la imagen para subirla al registro
#docker tag dialog-controller @nameAKS.azurecr.io/dialog-controller:@version

#Subo la imagen al registro
#docker push @nameAKS.azurecr.io/dialog-controller:@version

#Cambio la imagen antigua por la nueva que acabo de subir
#kubectl set image deployment dialog-controller dialog-controller=@nameAKS.azurecr.io/dialog-controller:@version