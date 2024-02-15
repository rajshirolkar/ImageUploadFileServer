# ESP32 CAM Image Server

This server is built using FastAPI to facilitate image uploads from ESP32 CAM devices. It organizes images by username, allowing for the collection and retrieval of datasets for TinyML model training. Below are instructions on how to interact with the server for uploading and downloading images.

## Setup

To set up your environment and run the server, follow these steps:

### 1. Create a Virtual Environment

First, navigate to your project directory in the terminal and create a virtual environment. This will isolate your project's dependencies from other projects.

- For **Windows**:

```bash
python -m venv venv
```

- For **macOS** and **Linux**:

```bash
python3 -m venv venv
```

### 2. Activate the Virtual Environment

Next, activate the virtual environment:

- For **Windows**:

```bash
.\venv\Scripts\activate
```

- For **macOS** and **Linux**:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

With your virtual environment activated, install FastAPI, Uvicorn, and `python-multipart` using pip:

```bash
pip install fastapi uvicorn python-multipart
```

### 4. Run the Server

To start the server, simply run the `app.py` file. If you named your application file differently, replace `app.py` with your file name:

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

This command starts the server on `http://0.0.0.0:8000`, making it accessible on your local network.


## Uploading Images

To upload images from your ESP32 CAM device, use the `/upload/{username}/` endpoint. Replace `{username}` with a unique identifier for the device or user.

### Request Format

- **URL**: `/upload/{username}/`
- **Method**: POST
- **Body**: Form-data with:
  - Key: `file`
  - Value: The image file to upload

### Example using `curl`:

```bash
curl -X POST "http://0.0.0.0:8000/upload/john_doe/" -F "file=@/path/to/your/image.jpg"
```

This command uploads an image for the user `john_doe`. The server stores the image in a directory named `john_doe` within the `files` folder at the server's root.

## Downloading Images

To download all images for a specific user/device, use the `/images/{username}/` endpoint. This will return a ZIP file containing all the user's images.

### Request Format

- **URL**: `/images/{username}/`
- **Method**: GET

### Example using `curl`:

```bash
curl -o john_doe_images.zip "http://0.0.0.0:8000/images/john_doe/"
```

This command downloads all images for `john_doe` and saves them as `john_doe_images.zip`.

## Purpose

The primary goal of this server is to assist in the collection of image datasets from ESP32 CAM devices. These datasets can be used to train TinyML models, facilitating a wide range of machine learning applications on resource-constrained devices.

## Note

Ensure your ESP32 CAM device is configured to send HTTP POST requests with images to the server's `/upload/{username}/` endpoint. For security and scalability considerations, consider implementing authentication and rate limiting when deploying the server in a production environment.
