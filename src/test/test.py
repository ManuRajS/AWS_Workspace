
if __name__ =="__main__":
    print('hello')
    x={'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'ap-south-1', 'eventTime': '2023-02-25T18:50:30.183Z', 'eventName': 'ObjectRemoved:Delete', 'userIdentity': {'principalId': 'AWS:AIDA44OWSYD6EFNKUKJL6'}, 'requestParameters': {'sourceIPAddress': '122.171.20.164'}, 'responseElements': {'x-amz-request-id': '1FBXETNSPFH9XW6T', 'x-amz-id-2': 'DXDlqGCdlrP6x6TsO9jXoJeopGntqvL1P2Xp06QUo2DIzJYa74HrAKwnVslTRAZs+uwT4ktlj5iPWLdFK45zzmkYWd3lTj5E'}, 's3': {'s3SchemaVersion': '1.0', 'configurationId': 'bucket-event', 'bucket': {'name': 'test-event-bucket-002', 'ownerIdentity': {'principalId': 'A2ZORGSP0NK0X4'}, 'arn': 'arn:aws:s3:::test-event-bucket-002'}, 'object': {'key': '1.jpeg', 'sequencer': '0063FA58762CDF0A0B'}}}]}
    bucekt_name=x['Records'][0]['s3']['bucket']['name']
    file_name=x['Records'][0]['s3']['object']['key']
    event=x['Records'][0]['eventName']
    print(bucekt_name,file_name,event)