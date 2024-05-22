from google.cloud import pubsub_v1

def create_topic(config):
    client = pubsub_v1.PublisherClient()
    topic_path = client.topic_path(config['project_id'], config['topic_id'])
    try:
        topic = client.create_topic(request={"name": topic_path})
        print(f"Topic created: {topic.name}")
    except Exception as e:
        print(f"An error occurred: {e}")

def create_subscription(config):
    client = pubsub_v1.SubscriberClient()
    topic_path = client.topic_path(config['project_id'], config['topic_id'])
    subscription_path = client.subscription_path(config['project_id'], config['subscription_id'])
    try:
        subscription = client.create_subscription(
            request={"name": subscription_path, "topic": topic_path}
        )
        print(f"Subscription created: {subscription.name}")
    except Exception as e:
        print(f"An error occurred: {e}")

def publish_message(config, message):
    client = pubsub_v1.PublisherClient()
    topic_path = client.topic_path(config['project_id'], config['topic_id'])
    try:
        future = client.publish(topic_path, message.encode("utf-8"))
        print(f"Published message ID: {future.result()}")
    except Exception as e:
        print(f"An error occurred: {e}")

def subscribe_messages(config):
    client = pubsub_v1.SubscriberClient()
    subscription_path = client.subscription_path(config['project_id'], config['subscription_id'])

    def callback(message):
        print(f"Received message: {message.data.decode('utf-8')}")
        message.ack()

    streaming_pull_future = client.subscribe(subscription_path, callback=callback)
    print(f"Listening for messages on {subscription_path}..\n")

    try:
        streaming_pull_future.result(timeout=10)
    except Exception as e:
        streaming_pull_future.cancel()
        print(f"An error occurred: {e}")
