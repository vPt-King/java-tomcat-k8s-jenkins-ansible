#!/bin/bash
sed -i "s|image: thanhvu638/javaweb:v[^\"]*|image: thanhvu638/javaweb:v$1|g" ./app.yaml
name_deployment=$(kubectl get deployment | awk '{print $1}' | grep tomcat)
kubectl delete deployment $name_deployment 
kubectl apply -f app.yaml