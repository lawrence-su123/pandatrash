import requests

print("=== Python Receipt OCR Demo - Need help? Email support@asprise.com ===")

receiptOcrEndpoint = 'https://ocr.asprise.com/api/v1/receipt' # Receipt OCR API endpoint
#imageFile = "receipt.jpg" # // Modify this to use your own file if necessary
imageFile = 'C:/Users/lawre/Downloads/panda_receipt_ex.jpg'
r = requests.post(receiptOcrEndpoint, data = { \
  'client_id': 'TEST',        # Use 'TEST' for testing purpose \
  'recognizer': 'auto',       # can be 'US', 'CA', 'JP', 'SG' or 'auto' \
  'ref_no': 'ocr_python_123', # optional caller provided ref code \
  }, \
  files = {"file": open(imageFile, "rb")})
z = r.text.find('Survey Code')
print(r.text) # result in JSON
print(r.text.find('Survey Code'))
print(r.text[z+1:z+20])