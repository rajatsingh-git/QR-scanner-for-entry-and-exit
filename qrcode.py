import qrcode

# List of student data
students = {
    "John Doe": "STU001",
    "Jane Smith": "STU002",
    "Alice Brown": "STU003",
    "Bob Johnson": "STU004",
    "Eve White": "STU005",
    "Chris Black": "STU006",
    "David Green": "STU007",
    "Mike Red": "STU008",
    "Lilly Blue": "STU009",
    "Sam Yellow": "STU010"
}

# Generate QR codes for each student
for name, student_id in students.items():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(student_id)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill='black', back_color='white')
    
    # Save the image
    img.save(f"{student_id}_{name}.png")

print("QR codes generated successfully!")
