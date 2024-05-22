import time
from .config import get_config
from .pubsub_manager import create_topic, create_subscription, publish_message, subscribe_messages

if __name__ == "__main__":
    config = get_config()

    create_topic(config)
    create_subscription(config)
    publish_message(config, "Hello, Pub/Sub!")
    time.sleep(1)  # Attendi che il messaggio sia pubblicato
    subscribe_messages(config)
