from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Directory to save received JSON files
SAVE_DIRECTORY = "received_files"
os.makedirs(SAVE_DIRECTORY, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_json():
    try:
        # Check if the request contains JSON data
        if not request.is_json:
            return jsonify({"error": "Invalid content type. JSON expected."}), 400

        # Get the JSON data
        data = request.get_json()

        # Create a file name and save the JSON data
        file_name = os.path.join(SAVE_DIRECTORY, "data.json")
        with open(file_name, 'w') as file:
            import json
            json.dump(data, file, indent=4)

        return jsonify({"message": "File received and saved successfully.", "file_path": file_name}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run the Flask app on port 5000
    app.run(host='0.0.0.0', port=5000)
