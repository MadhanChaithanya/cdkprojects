#!/usr/bin/env python3

from aws_cdk import core

from cdkvpc.cdkvpc_stack import CdkvpcStack


app = core.App()
CdkvpcStack(app, "devVPC")

app.synth()
