"""
File Name: app.py
Author: Johannah Voeller (voeller@ugr.es); University of Granada (Spain)

Description: 
Interface to select Mooney images from the THINGS-Mooney database (https://github.com/wobc/things-mooney), implemented in python with flask.
Main script app.py, frontend implementation in base.html and index.html

To use Selection GUI:
1) Navigate to app.py folder ('gui')
2) Open a new terminal at folder
3) Type: 'python3 app.py'
4) A local sever opens (http://127.0.0.1:5000)
5) Type the server address in your web browser and start the image selection!

"""

#-----------------
# Impoprt Modules
#-----------------

from flask import Flask, request, render_template, session, url_for, send_file, redirect
import os
import pandas as pd
import shutil
import zipfile
import tempfile

app = Flask(__name__)
app.secret_key = 's3cr3t_k3y_12345'


#-----------------
# Image Selection
#-----------------

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Parse form inputs
            output_directory = request.form['output_directory']
            num_images = int(request.form['num_images'])
            subj_ident_pre = request.form.get('subj_ident_pre')
            subj_ident_post = request.form.get('subj_ident_post')
            semantic_distance_pre = request.form.get('semantic_distance_pre')
            semantic_distance_post = request.form.get('semantic_distance_post')
            entropy_pre = request.form.get('entropy_pre')
            entropy_post = request.form.get('entropy_post')
            get_gray = request.form.get('get_gray')
            
            # Prepare directories
            curr_dir = os.getcwd()
            #output_directory = os.path.join(curr_dir, output_directory)
            #os.makedirs(output_directory, exist_ok=True)

            # Load metadata
            metadata_path = os.path.join(os.path.dirname(curr_dir), 'things_mooney_metadata.csv')
            if not os.path.exists(metadata_path):
                raise FileNotFoundError(f"Metadata file not found: {metadata_path}")
            things_metadata = pd.read_csv(metadata_path)

            # Prepare criteria
            criteria = []
            variable_names = [
                "subj_ident_pre", "subj_ident_post",
                "sem_dist_pre", "sem_dist_post",
                "sem_entropy_pre", "sem_entropy_post"
            ]

            for var_name, value in zip(variable_names, [subj_ident_pre, subj_ident_post, semantic_distance_pre, semantic_distance_post, entropy_pre, entropy_post]):
                if value:
                    start, stop = map(float, value.split(";")) if ";" in value else (float(value), None)
                    criteria.append({f"{var_name}_start": start, f"{var_name}_stop": stop or things_metadata[var_name].max()})
                else:
                    criteria.append({f"{var_name}_start": None, f"{var_name}_stop": None})

            # Filter images
            def select_images(metadata, criteria, variable_names):
                conditions = []
                for crit, var_name in zip(criteria, variable_names):
                    start, stop = crit.get(f"{var_name}_start"), crit.get(f"{var_name}_stop")
                    if start is not None and stop is not None:
                        conditions.append((metadata[var_name] >= start) & (metadata[var_name] <= stop))
                if conditions:
                    combined_condition = conditions[0]
                    for cond in conditions[1:]:
                        combined_condition &= cond
                    return metadata[combined_condition]
                return metadata

            # Apply function to select images that meet criteria
            df_selected = select_images(things_metadata, criteria, variable_names)
            num_images_found = len(df_selected)

            # Alert if no images meet criteria
            if num_images_found == 0:
                return """
                    <div style="font-family: Arial, sans-serif; max-width: 500px; margin: auto; padding: 20px; border-radius: 10px; background-color: #f9f9f9; text-align: center;">
                        <h2>No images found</h2>
                        <p>Sorry, no images match your selected criteria. Please try adjusting your selection.</p>
                        <br>
                        <a href="/"><button style="padding: 10px 20px; background-color: #dc3545; color: white; border: none; border-radius: 5px; cursor: pointer;">🔄 Start New Selection</button></a>
                    </div>
                """

            # Save filtered DataFrame to a temporary CSV file
            temp_csv_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
            df_selected.to_csv(temp_csv_file.name, index=False)
            csv_file_path = temp_csv_file.name

            # Save criteria to a text file
            temp_txt_file = tempfile.NamedTemporaryFile(delete=False, suffix=".txt")
            txt_file_path = temp_txt_file.name

            with open(txt_file_path, "w") as txt_output:
                txt_output.write("Selected Criteria:\n")
                for criteria in criteria:
                    txt_output.write(str(criteria) + "\n")

            
            # Save session data
            session['df_selected_path'] = csv_file_path
            session['criteria'] = txt_file_path
            session['output_directory'] = output_directory
            session['num_images'] = num_images
            session['get_gray'] = get_gray

            # Ask user to confirm download quantity (all images found or selected number of images)
            return f"""
                <div style="font-family: Arial, sans-serif; max-width: 500px; margin: auto; padding: 20px; border-radius: 10px; background-color: #f9f9f9; text-align: center;">
                    <h2>{num_images_found} images found</h2>
                    <p>Would you like to download all images or the specified number ({num_images})?</p>
                    <form action="/download" method="POST">
                        <label>
                            <input type="checkbox" name="all_images"> Download all images
                        </label>
                        <br><br>
                        <button type="submit" style="padding: 10px 20px; background-color: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer;">Confirm Selection & Download</button>
                    </form>
                    <br>
                    <a href="/" style="color: #007bff; text-decoration: none;">⬅ Start New Selection</a>
                </div>
            """

        except Exception as e:
            return f"<p>Error: {e}</p>"

    return render_template('index.html', error=None)



#-----------------
# Image Download
#-----------------

@app.route('/download', methods=['POST'])
def download():
    try:
       # Retrieve session data
        df_selected_path = session.get('df_selected_path')
        criteria_path = session.get('criteria')
        num_images_to_download = session.get('num_images')
        get_gray = session.get('get_gray')
        all_images = request.form.get('all_images')
        folder_name = session.get('output_directory')

        # Check if required files exist
        if not df_selected_path or not os.path.exists(df_selected_path):
            return "<p>Session expired or data lost. Please start over.</p>"

        if not criteria_path or not os.path.exists(criteria_path):
            return "<p>Criteria file is missing. Please start over.</p>"

        # Load selected images DataFrame
        df_selected = pd.read_csv(df_selected_path)

        # Load criteria from the text file
        with open(criteria_path, "r") as criteria_file:
            criteria_content = criteria_file.readlines()

        # Adjust number of images
        if not all_images:
            num_images_to_download = int(num_images_to_download)
            if num_images_to_download > len(df_selected):
                return "<p>Number exceeds available images.</p>"
            df_selected = df_selected.sample(n=num_images_to_download)

        # Create temporary folder for zipping
        temp_dir = "temp_download"
        os.makedirs(temp_dir, exist_ok=True)
        mooney_dir = os.path.join(temp_dir, 'mooney')
        gray_dir = os.path.join(temp_dir, 'gray')
        os.makedirs(mooney_dir, exist_ok=True)

        # Define paths to get images (parent dir)
        stim_mooney = os.path.abspath(os.path.join(os.getcwd(), '..', 'stim', 'mooney'))

        if not os.path.exists(stim_mooney):
            return f"<p>Error: stim/mooney folder not found at {stim_mooney}</p>"

        # Debugging: Print the path
        print(f"Looking for images in: {stim_mooney}")

        stim_gray = os.path.abspath(os.path.join(os.getcwd(), '..', 'stim', 'gray'))

        if not os.path.exists(stim_gray):
            return f"<p>Error: stim/mooney folder not found at {stim_gray}</p>"

        # Debugging: Print the path
        print(f"Looking for images in: {stim_gray}")


        # Copy images to temp folder
        for image in df_selected['image']:
            shutil.copy(os.path.join(stim_mooney, f"{image}_mooney.jpg"), mooney_dir)
            if get_gray:
                os.makedirs(gray_dir, exist_ok=True)
                shutil.copy(os.path.join(stim_gray, f"{image}_gray.jpg"), gray_dir)

        # Save metadata and criteria
        df_selected.to_csv(os.path.join(temp_dir, 'selected_images.csv'), index=False)
        with open(os.path.join(temp_dir, 'criteria.txt'), "w") as file:
            file.writelines(criteria_content)

        # Create ZIP file
        zip_filename = f"{folder_name}.zip"
        zip_path = os.path.join(os.getcwd(), zip_filename)
        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for root, _, files in os.walk(temp_dir):
                for file in files:
                    zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), temp_dir))

        # Remove temp directory
        shutil.rmtree(temp_dir)

        # Store ZIP path in session & Redirect to success page
        session['zip_path'] = zip_path
        return send_file(zip_path, as_attachment=True)

        #return redirect(url_for('success'))
    
    except Exception as e:
        return f"<p>Error: {e}</p>"

if __name__ == '__main__':
    app.run(debug=True)
