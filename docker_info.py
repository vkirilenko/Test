#!/usr/bin/env python3

import os
import sys
import docker
import json

def get_address():
    port = 80
    arg_lst = sys.argv[1:]
    if len(arg_lst) == 0:
        print("\nNo IP is provided, trying to get ENV value...")
        try:
            IP = os.environ['DOCKER_HOST']
        except:
            print("No container IP available in environment values!")
            print("Trying to connect with 127.0.0.1")
            return ['127.0.0.1', port]
    if arg_lst[0].startswith('http'):
        arg_lst[0] = arg_lst[0].split("//")[1]
    if ":" in arg_lst[0]:
        IP, port = arg_lst[0].split(":")[0], arg_lst[0].split(":")[1]
    else:
        IP = arg_lst[0]
    return [IP, port]

def connect(addr: list):
    try:
        dclient = docker.DockerClient(base_url='unix://var/run/docker.sock', version='auto')
        dconts = dclient.containers.list(all)
    except:
        print("No docker connections established. Check docker service is running!")
        sys.exit(1)
    else:
        for cont in dconts:
            if cont.attrs['State']['Status'] != 'running':
                print(f"\nContainer {cont.attrs['Name'][1:]} with ID: {cont.attrs['Id']} is dead or stopped!")

def cont_list():
    dclient = docker.DockerClient(base_url='unix://var/run/docker.sock', version='auto')
    for cont in dclient.containers.list():
        print(f"\nContainer {cont.attrs['Name']} is in state: {cont.attrs['State']['Status']}")

def cont_inspect():
    dclient = docker.DockerClient(base_url='unix://var/run/docker.sock', version='auto')
    print("")
    for cont in dclient.containers.list(all):
        info = ["Name: "+cont.attrs['Name'][1:], "Status: "+cont.attrs['State']['Status'],"Image: "+cont.attrs['Config']['Image'],"IP address: "+cont.attrs['NetworkSettings']['IPAddress']]
        print("Container information:")
        for item in info:
            print(item)
        print('')
        try:      
            print("Full container information stored in files (with DOCKER-<container name>)")
            filename = "DOCKER-" + cont.attrs['Name'][1:] + ".json"
            output = open(filename, "wt")
            json.dump(cont.attrs, output)
            output.close()
        except:
            pass
        print('-----')


if __name__ == "__main__":
    addr = get_address()
    connect(addr)
    cont_list()
    cont_inspect()
