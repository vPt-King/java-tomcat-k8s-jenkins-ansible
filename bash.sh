#!/bin/bash
name_deployment=$(kubectl get deployment | awk '{print $1}' | grep tomcat)
kubectl delete deployment $name_deployment 
kubectl apply -f app.yaml