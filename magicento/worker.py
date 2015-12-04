import logging
import sys
import requests
import boto3


logging.basicConfig(stream=sys.stdout, level=logging.INFO)
LOG = logging.getLogger(__name__)

from magicento import magicento

def process_message(message):
  beanstalk = magicento.Beanstalk()
  beanstalk.create_beanstalk()


def poll():
  """Poll the SQS queue, processing messages as they are retrieved."""
  LOG.info("Starting polling.")
  response = requests.get('http://169.254.169.254/latest/dynamic/instance-identity/document').json()
  instance_id = response.get('instanceId')
  region = response.get('region')
  boto3.setup_default_session(region_name=region)
  
  while True:
      LOG.info("Checking for message from SQS.")
      try:
          sqs = boto3.resource('sqs')
          queue = sqs.get_queue_by_name(QueueName='Infra-Work')
          # TODO: Determine most appropriate timeout time.
          messages = queue.receive_messages(VisibilityTimeout=20)
          for message in messages:
              handle_message(message)
      except Exception:
          LOG.warning("Something went wrong with handling message.")
          import time; time.sleep(5)


def main():
    LOG.info("Starting AEMgent")
    poll()


if __name__ == '__main__':
    main()