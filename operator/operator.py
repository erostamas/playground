#!/usr/bin/env python3

import kopf
import kubernetes.client
from kubernetes.client.rest import ApiException
import yaml


@kopf.on.create('erostamas.crd', 'v1', 'bands')
def create_fn(spec, **kwargs):
    name = kwargs["body"]["metadata"]["name"]
    print("Name is %s\n" % name)
    # Create the deployment spec
    doc = yaml.safe_load(f"""
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: {name}-deployment
          labels:
            app: {name}
        spec:
          replicas: {spec.get('my-replica-count', 1)}
          selector:
            matchLabels:
              app: {name}
          template:
            metadata:
              labels:
                app: {name}
            spec:
              containers:
              - name: nginx
                image: nginx
    """)

    # Make it our child: assign the namespace, name, labels, owner references, etc.
    kopf.adopt(doc)

    # Actually create an object by requesting the Kubernetes API.
    api = kubernetes.client.AppsV1Api()
    #try:
    depl = api.create_namespaced_deployment(namespace=doc['metadata']['namespace'], body=doc)
      # Update the parent's status.
    return {'children': [depl.metadata.uid]}
    #except ApiException as e:
    #  print("Exception when calling AppsV1Api->create_namespaced_deployment: %s\n" % e)
      