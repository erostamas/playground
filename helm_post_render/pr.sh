#!/bin/bash

#sed "s/app.kubernetes.io/lofasz/" < /proc/self/fd/0

echo "---
apiVersion: v1
kind: Pod
metadata:
  name: "{{ .Release.Name }}-test"
  annotations:
    "helm.sh/hook": test
spec:
  containers:
    - name: test
      image: busybox
      command: ['sh', '-c', 'wget -qO- http://my-service:80']
  restartPolicy: Never"