#!/bin/bash

/usr/local/bin/kubectl delete deployment tomcat-deployment --kubeconfig /home/thanhnga/.kube/config
/usr/local/bin/kubectl apply -f /var/lib/jenkins/workspace/java-tomcat/app.yaml --kubeconfig /home/thanhnga/.kube/config