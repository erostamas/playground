#!/usr/bin/env python3
#
#import kubernetes
#
#core_api = kubernetes.client.CoreV1Api()
#watcher = kubernetes.watch.Watch()
#stream = watcher.stream(core_api.list_event_for_all_namespaces, timeout_seconds=5)
#for raw_event in stream:
#    print(raw_event)

from kubernetes import client, config, watch

# Configs can be set in Configuration class directly or using helper utility
config.load_kube_config()

api = client.CoreV1Api()
#print("Listing pods with their IPs:")
#ret = v1.list_pod_for_all_namespaces(watch=False)
#for i in ret.items:
#    print("%s\t%s\t%s" % (i.status.pod_ip, i.metadata.namespace, i.metadata.name))

resp = api.read_namespaced_config_map(name='dummy', namespace='development')
#print(resp)
rv = resp.metadata.resource_version
watcher = watch.Watch()
for event in watcher.stream(api.list_namespaced_config_map,
                              namespace='development',
                              resource_version=rv):
    #print(f"{event['type']} {event['object'].metadata.name}")
    print(f"{event}")