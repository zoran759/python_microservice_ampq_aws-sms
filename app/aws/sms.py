import boto3
import os


def data_validate(validateData):
    if not validateData["number"] or not validateData["message"]:
        return False
    else:
        return True


def send_sms(data):
	client = boto3.client(
		"sns",
		aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
		aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
		region_name=os.getenv("AWS_DEFAULT_REGION")
	)

	#Send SMS message
	client.publish(
		PhoneNumber=data["number"],
		Message=data["message"]
	)
