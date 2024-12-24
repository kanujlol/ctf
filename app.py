from flask import Flask, render_template, request, redirect, url_for
from stegano import lsb

app = Flask(__name__)

# Helper function to decode the steganography message from an image file
def decode_image(file_path):
    message = lsb.reveal(file_path)
    return message

# Step 6: Steganography Extraction Page
@app.route('/step6', methods=['GET', 'POST'])
def step6():
    if request.method == 'POST':
        # Get the uploaded files
        image1 = request.files.get('image1')
        image2 = request.files.get('image2')
        
        # Save the files temporarily
        image1_path = 'static/' + image1.filename
        image2_path = 'static/' + image2.filename
        
        image1.save(image1_path)
        image2.save(image2_path)
        
        # Decode the hidden messages from both images
        message1 = decode_image(image1_path)
        message2 = decode_image(image2_path)
        
        # Combine the decoded messages
        combined_message = message1 + " " + message2
        
        # Check if the combined message matches the expected answer
        expected_answer = "croft"
        
        if combined_message.strip().lower() == expected_answer:
            return redirect(url_for('final'))  # Redirect to final step if correct
        else:
            return render_template('step6.html', error="Incorrect message. Try again.")
    
    return render_template('step6.html')

# Final Page: Reveal the Flag
@app.route('/final', methods=['GET'])
def final():
    return render_template('final.html', flag="SSMB")

if __name__ == '__main__':
    app.run(debug=True)
