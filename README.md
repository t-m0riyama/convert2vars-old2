convert2vars
=============

A small tool for mutual conversion of JSON, YAML with embedded parameters.
Parameter processing can take advantage of the powerful features of the Jinja2 template engine.

*This document has been translated into English by machine translation. Please note that some parts may be inaccurate.*

## Installation
```
$ pip install convert2vars
```

## Requirements
* Python 3.7 or later

## Usage

### Basic Usage

The following simple example shows how to convert a k8s Deployment file.
This file contains two parameters (REPLICAS and CONTAINER_PORT), which are converted to the specified values by using the -e option.

``` k8s Deployment sample
$ cat k8s-deployment.yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: {{ REPLICAS | default(2, True) }}
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: {{ CONTAINER_PORT | default(80, True) }}

$ convert2vars convert -e REPLICAS=4 -e CONTAINER_PORT=8080 -t k8s-deployment.yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 4
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - image: nginx:1.14.2
        name: nginx
        ports:
        - containerPort: 8080
```

### Specifying Parameters

Parameter values can be specified in the following ways, or a combination of several methods.
* -e option
  - Specify by command line option as described above. Multiple parameters can also be specified.
* Environment variables
  - After setting environment variables, execution with the -E option produces the same results as described above.
  ```
  $ export REPLICAS=4
  $ export CONTAINER_PORT=8080
  $ convert2vars convert -t k8s-deployment.yml -E
  ```
  - --dotenv-file option can also be specified to use a combination of dotenv files.
  ```
  $ cat dotenv-temp
  CONTAINER_PORT=8080
  REPLICAS=4
  
  $ convert2vars convert -t k8s-deployment.yml --dotenv-file dotenv-temp -E
  ```

* Parameter files
  - By using a file that enumerates parameters and their values, many parameters can be specified at once.
  - JSON, YAML, and ini format files are available. The following three parameter files all produce the same results as in the example with the -e option described above.

  ``` JSON parameter file example 
  ## JSON format (k8s-parameter.json)
  {
  "REPLICAS": 3,
  "CONTAINER_PORT": 8080
  }
  ```

  ``` YAML parameter file example
  ## YAML format (k8s-parameter.yml)
  REPLICAS: 3
  CONTAINER_PORT: 8080
  ```

  ``` ini parameter file example
  ## ini format (k8s-parameter.ini)
  [default]
  REPLICAS=3
  CONTAINER_PORT=8080
  ```
  - When using a parameter file, use the -i and -t options together.
  ```
  $ convert2vars convert -t k8s-deployment.yml -i k8s-parameter.json
  ```

### Template engine support
  The filter, conditional branching, and iteration functions provided by Jinja2 can be used without modification. In the following example, since the parameter values are not explicitly specified, they are converted to the default values of 2 and 80 by Jinja2's default filter.

```
$ convert2vars convert -t samples/templates/k8s-deployment.yml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 2
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - image: nginx:1.14.2
        name: nginx
        ports:
        - containerPort: 80
```

### Format Conversion
For JSON and YAML, it is possible to mutually convert formats.
In the following example, the -f option is used to convert to JSON format.
To perform format conversion, do not use the -t option, but specify the conversion source file as a parameter file with the -i option.

```
$ convert2vars convert -e REPLICAS=4 -e CONTAINER_PORT=8080 -i k8s-deployment.yml -f json | jq .
{
  "apiVersion": "apps/v1",
  "kind": "Deployment",
  "metadata": {
    "name": "nginx-deployment"
  },
  "spec": {
    "replicas": 4,
    "template": {
      "metadata": {
        "labels": {
          "app": "nginx"
        }
      },
      "spec": {
        "containers": [
          {
            "name": "nginx",
            "image": "nginx:1.14.2",
            "ports": [
              {
                "containerPort": 8080
              }
            ]
          }
        ]
      }
    }
  }
}
```

## License

The convert2vars module was written by t-m0riyama.
convert2vars is released under the MIT license.

See the file LICENSE for more details.