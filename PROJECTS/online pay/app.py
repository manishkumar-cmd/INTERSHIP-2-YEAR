from flask import Flask, render_template, request, send_from_directory, abort
import os
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

# ✅ Email Sending Function
def send_email_with_pdf(to_email, user_name):
    msg = EmailMessage()
    msg['Subject'] = 'Your PDF Download – Thank You!'
    msg['From'] = 'your_email@gmail.com'
    msg['To'] = to_email
    msg.set_content(f"Hi {user_name},\n\nThanks for your payment!\nPlease find your PDF attached.\n\nBest regards,\nYour Website Team")

    # Attach PDF
    with open('pdf/99.pdf', 'rb') as f:
        file_data = f.read()
        file_name = '99.pdf'

    msg.add_attachment(file_data, maintype='application', subtype='pdf', filename=file_name)

    # Gmail SMTP
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('thegamer6470b@gmail.com', 'ibpm zcgi iyda rtpt')  # Replace this
        smtp.send_message(msg)

# ✅ Home Page
@app.route('/')
def home():
    return render_template('index.html')

# ✅ Form Submit Page
@app.route('/submit', methods=['POST'])
def submit():
    print("Form data received:", request.form)

    name = request.form.get('name', '')
    email = request.form.get('email', '')
    upi_id = request.form.get('upi', '')


    if not name or not email:
        return "Missing required information.", 400

    # Save to file
    with open("payments.txt", "a") as f:
        f.write(f"{name}, {email}, {upi_id},\n")

    # Send PDF to Email
    try:
        send_email_with_pdf(email, name)
        print(f"Email sent to {email}")
    except Exception as e:
        print("Email error:", e)
        return "Payment recorded, but failed to send email.", 500

    return render_template('success.html', name=name)

# ✅ Manual PDF Download (optional)
@app.route('/download')
def download():
    try:
        return send_from_directory('pdf', 'yourfile.pdf', as_attachment=True)
    except FileNotFoundError:
        return "PDF not found", 404

# ✅ Run the App
if __name__ == '__main__':
    app.run(debug=True)
