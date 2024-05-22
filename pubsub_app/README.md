# Google Cloud Pub/Sub Manager
## Description
This project provides a Python interface to interact with Google Cloud Pub/Sub. With this manager, you can create topics and subscriptions, publish and receive messages using the Google Cloud Pub/Sub API.

Install dependencies using Poetry: 
- poetry install

Run tests to verify everything works correctly:
- poetry run pytest

## Usage 
- Configure Google Cloud credentials: gcloud auth application-default login
- Modify the config.py file with appropriate values for your Google Cloud Pub/Sub project
- Run main.py to utilize the Pub/Sub manager's functionalities:
  - poetry run python main.py

## Project structure
- pubsub_manager.py: Contains functions to interact with Google Cloud Pub/Sub.
- config.py: Manages project configurations.
- main.py: Example usage of Pub/Sub manager's functionalities.
- tests/: Contains unit tests for the Pub/Sub manager.
- poetry.lock and pyproject.toml: Configuration files for Poetry.

