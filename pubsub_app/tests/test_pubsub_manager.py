import unittest
from unittest.mock import patch, Mock
from pubsub_app.pubsub_manager import create_topic, create_subscription, publish_message, subscribe_messages


class TestPubSubManager(unittest.TestCase):

    @patch('pubsub_app.pubsub_manager.pubsub_v1.PublisherClient')
    def test_create_topic(self, MockPublisherClient):
        mock_publisher = MockPublisherClient.return_value
        mock_publisher.topic_path.return_value = 'projects/test-project/topics/test-topic'
        mock_publisher.create_topic.return_value = Mock(name='Topic')

        config = {
            'project_id': 'test-project',
            'topic_id': 'test-topic',
            'subscription_id': 'test-subscription'
        }
        create_topic(config)

        mock_publisher.topic_path.assert_called_once_with('test-project', 'test-topic')
        mock_publisher.create_topic.assert_called_once()

    @patch('pubsub_app.pubsub_manager.pubsub_v1.SubscriberClient')
    def test_create_subscription(self, MockSubscriberClient):
        mock_subscriber = MockSubscriberClient.return_value
        mock_subscriber.topic_path.return_value = 'projects/test-project/topics/test-topic'
        mock_subscriber.subscription_path.return_value = 'projects/test-project/subscriptions/test-subscription'
        mock_subscriber.create_subscription.return_value = Mock(name='Subscription')

        config = {
            'project_id': 'test-project',
            'topic_id': 'test-topic',
            'subscription_id': 'test-subscription'
        }
        create_subscription(config)

        mock_subscriber.topic_path.assert_called_once_with('test-project', 'test-topic')
        mock_subscriber.subscription_path.assert_called_once_with('test-project', 'test-subscription')
        mock_subscriber.create_subscription.assert_called_once()

    @patch('pubsub_app.pubsub_manager.pubsub_v1.PublisherClient')
    def test_publish_message(self, MockPublisherClient):
        mock_publisher = MockPublisherClient.return_value
        mock_publisher.topic_path.return_value = 'projects/test-project/topics/test-topic'
        mock_publisher.publish.return_value = Mock(name='Future')

        config = {
            'project_id': 'test-project',
            'topic_id': 'test-topic',
            'subscription_id': 'test-subscription'
        }
        publish_message(config, 'Hello, Pub/Sub!')

        mock_publisher.topic_path.assert_called_once_with('test-project', 'test-topic')
        mock_publisher.publish.assert_called_once_with('projects/test-project/topics/test-topic', b'Hello, Pub/Sub!')

    @patch('pubsub_app.pubsub_manager.pubsub_v1.SubscriberClient')
    def test_subscribe_messages(self, MockSubscriberClient):
        mock_subscriber = MockSubscriberClient.return_value
        mock_subscriber.subscription_path.return_value = 'projects/test-project/subscriptions/test-subscription'
        mock_streaming_pull_future = Mock()
        mock_subscriber.subscribe.return_value = mock_streaming_pull_future

        config = {
            'project_id': 'test-project',
            'topic_id': 'test-topic',
            'subscription_id': 'test-subscription'
        }
        subscribe_messages(config)

        mock_subscriber.subscription_path.assert_called_once_with('test-project', 'test-subscription')
        mock_subscriber.subscribe.assert_called_once()
        mock_streaming_pull_future.result.assert_called_once()


if __name__ == '__main__':
    unittest.main()
