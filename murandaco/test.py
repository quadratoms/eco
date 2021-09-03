from paystack.resource import TransactionResource


rand = 'mu1'
secret_key = 'sk_test_ac7e6b6b04b712d76676cd40230e4db141f8b9e6'
random_ref = rand
test_email = 'quadratoms30'
test_amount = 'TEST_AMOUNT'
plan = 'Basic'
client = TransactionResource(secret_key, random_ref)
# response = c****lient.initialize(test_amount,
#                                  test_email,
#                                  plan)
# print(response)
# client.authorize()  # Will open a browser window for client to enter card details
verify = client.verify()  # Verify client credentials
print(verify['data']['status'])
# print(client.charge())  # Charge an already exsiting client
