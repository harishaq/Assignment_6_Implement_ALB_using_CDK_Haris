import aws_cdk as core
import aws_cdk.assertions as assertions

from assignment5_cdk_alb.assignment5_cdk_alb_stack import Assignment5CdkAlbStack

# example tests. To run these tests, uncomment this file along with the example
# resource in assignment5_cdk_alb/assignment5_cdk_alb_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Assignment5CdkAlbStack(app, "assignment5-cdk-alb")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
