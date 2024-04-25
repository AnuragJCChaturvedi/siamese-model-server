# TensorFlow Model Server with FastAPI

## Overview

This repository hosts a TensorFlow 2.10 model server that provides image processing capabilities via a FastAPI interface. The server is containerized using Docker, ensuring easy deployment and management of dependencies. It exposes two primary endpoints: one for assessing image similarity accuracy and another for liveliness detection.

## Saimese Model Training

**Model/ai_models/AI_Project.ipynb**: The main Jupyter notebook that contains the code for training the saimese model.

## Features

- **Image Similarity Accuracy**: Determines the similarity between two images and returns a similarity score.
- **Liveliness Detection**: Detects if the subject in the image is a live person to prevent spoofing attacks.
- **Docker Integration**: All dependencies are managed via Docker for consistent and scalable deployments.

## Getting Started

### Prerequisites

- Docker installed on your machine
- Basic knowledge of Docker operations
- Python environment if you wish to run locally without Docker
- Access the siamese trained model [here](https://pitt-my.sharepoint.com/:u:/g/personal/anc527_pitt_edu/Ea956_Kr7q1HirCX2yaDfWkBShKPwlBddjRi1hRPYLdqqA?e=oU9WsT). Download and place **siamesemodelv2.h5** at the path **model-server/ai_models**.


### Installation and Setup

#### Clone this repository

#### Build the Docker Container

This project includes a Dockerfile which sets up the TensorFlow environment, installs necessary Python packages, and prepares the FastAPI server.

```
docker build -t model-server .
```

#### Running the Server

Start the Docker container with the following command:
```
docker run -p 8000:8000 model-server
```

This command runs the container and maps port 8000 of the container to port 8000 on your host, allowing you to access the FastAPI server at http://localhost:8000.
