from flask import Flask, request, render_template
import pandas as pd
from datetime import datetime

app = Flask(__name__)

# Path to the Excel file
EXCEL_FILE = "student_entry_exit_log.xlsx"

# Initialize the Excel file if it doesn't exist
def init_excel_file():
    try:
        df = pd.read_excel(EXCEL_FILE)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Student_ID", "Timestamp", "Status"])
        df.to_excel(EXCEL_FILE, index=False)

# Route to render the HTML page
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle QR code scanning
@app.route('/scan', methods=['POST'])
def scan():
    data = request.get_json()  # Get the JSON data sent from the front-end
    
    qr_code = data.get('qr_code')  # Access QR Code from the JSON
    entry_exit = data.get('entry_exit')  # Access the entry/exit status
    
    if not qr_code or not entry_exit:
        return "Invalid data", 400
    
    student_id = qr_code.strip()
    status = entry_exit
    
    # Log the timestamp and status
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Load the Excel file and append the new log
    df = pd.read_excel(EXCEL_FILE)
    new_log = pd.DataFrame({"Student_ID": [student_id], "Timestamp": [timestamp], "Status": [status]})
    
    # Use pd.concat instead of append
    df = pd.concat([df, new_log], ignore_index=True)
    
    # Save back to the Excel file
    df.to_excel(EXCEL_FILE, index=False)
    
    return "QR Code scanned and data logged!"


if __name__ == '__main__':
    init_excel_file()
    app.run(debug=True)
