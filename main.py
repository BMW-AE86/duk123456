from fpdf import FPDF
import boto3

# Read emails from file
with open("emails.txt", "r") as file:
    emails = [email.strip() + "," for email in file.readlines()]

# Save emails as a PDF
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

for email in emails:
    pdf.cell(200, 10, txt=email, ln=True, align='L')

pdf_file_name = "new-emails.pdf"
pdf.output(pdf_file_name)

# Upload PDF to Wasabi
wasabi_s3 = boto3.client(
    's3',
    endpoint_url='https://s3.wasabisys.com',
    aws_access_key_id='ANLDS76GW5KOK4REGUYC',  # Replace with your Wasabi Access Key
    aws_secret_access_key='MmiG5F1DwpNMbtQQsD7Zkw95AhIJHzqXnIfXzimQ'  # Replace with your Wasabi Secret Key
)

bucket_name = "houssem"  # Replace with your Wasabi bucket name
try:
    wasabi_s3.upload_file(pdf_file_name, bucket_name, pdf_file_name)
    print(f"PDF '{pdf_file_name}' uploaded successfully to Wasabi bucket '{bucket_name}'.")
except Exception as e:
    print(f"Failed to upload PDF to Wasabi: {e}")
