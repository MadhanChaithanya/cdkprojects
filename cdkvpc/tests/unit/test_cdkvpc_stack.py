import json
import pytest

from aws_cdk import core
from cdkvpc.cdkvpc_stack import CdkvpcStack


def get_template():
    app = core.App()
    CdkvpcStack(app, "cdkvpc")
    return json.dumps(app.synth().get_stack("cdkvpc").template)


def test_sqs_queue_created():
    assert("AWS::SQS::Queue" in get_template())


def test_sns_topic_created():
    assert("AWS::SNS::Topic" in get_template())
