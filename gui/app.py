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

from flask import Flask, request, render_template, session, url_for
import os
import pandas as pd
import shutil
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
            subj_recog_pre = request.form.get('subj_recog_pre')
            subj_recog_post = request.form.get('subj_recog_post')
            semantic_distance_pre = request.form.get('semantic_distance_pre')
            semantic_distance_post = request.form.get('semantic_distance_post')
            entropy_pre = request.form.get('entropy_pre')
            entropy_post = request.form.get('entropy_post')
            get_gray = request.form.get('get_gray')
            
            # Prepare directories
            curr_dir = os.getcwd()
            output_directory = os.path.join(curr_dir, output_directory)
            os.makedirs(output_directory, exist_ok=True)

            # Load metadata
            metadata_path = os.path.join(os.path.dirname(curr_dir), 'things_mooney_metadata.csv')
            if not os.path.exists(metadata_path):
                raise FileNotFoundError(f"Metadata file not found: {metadata_path}")
            things_metadata = pd.read_csv(metadata_path)

            # Prepare criteria
            criteria = []
            variable_names = [
                "mean_subj_recog_pre", "mean_subj_recog_post",
                "mean_sem_dist_pre", "mean_sem_dist_post",
                "pre_semantic_entropy", "post_semantic_entropy"
            ]

            for var_name, value in zip(variable_names, [subj_recog_pre, subj_recog_post, semantic_distance_pre, semantic_distance_post, entropy_pre, entropy_post]):
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
                return "<p>No images found matching your criteria. Please adjust.</p>"

            # Save DataFrame to a temporary file
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".csv")
            df_selected.to_csv(temp_file.name, index=False)
            temp_file_path = temp_file.name
            #print(temp_file_path)
            
            # Save session data
            session['df_selected_path'] = temp_file_path
            session['output_directory'] = output_directory
            session['num_images'] = num_images
            session['get_gray'] = get_gray

            # Ask user to confirm download quantity (all images found or selected number of images)
            return f"""
                <p>{num_images_found} images found.</p>
                <form action="/download" method="POST">
                    <label for="num_images">Would you like to download all images or the number of images you specified ({num_images})?:</label>
                    <br>
                    <input type="checkbox" name="all_images"> All images
                    <br>
                    <input type="submit" value="Confirm Download">
                </form>
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
        # Load selected DataFrame from temporary file
        df_selected_path = session.get('df_selected_path')
        if not df_selected_path or not os.path.exists(df_selected_path):
            return "<p>Session expired or data lost. Please start over.</p>"

        # Reload user inputs
        df_selected = pd.read_csv(df_selected_path)
        output_directory = session.get('output_directory')
        num_images_to_download = session.get('num_images')
        get_gray = session.get('get_gray')
        all_images = request.form.get('all_images')

        # Adjust number of images
        if not all_images:
            num_images_to_download = int(num_images_to_download)
            if num_images_to_download > len(df_selected):
                return "<p>Number exceeds available images.</p>"
            df_selected = df_selected.sample(n=num_images_to_download)
        # if all images is selected --> df_selected = df_selected (no filtering)

        # Make directories to store images
        curr_dir = os.getcwd()
        stim_mooney = os.path.join(os.path.dirname(curr_dir), 'stim', 'mooney')
        stim_gray = os.path.join(os.path.dirname(curr_dir), 'stim', 'gray')
        os.makedirs(os.path.join(output_directory, 'mooney'), exist_ok=True)

        # Copy images
        for image in df_selected['image']:
            shutil.copy(os.path.join(stim_mooney, f"{image}_mooney.jpg"), os.path.join(output_directory, 'mooney'))
            # If user wants to download corresponding gray-images as well
            if get_gray:
                gray_dir = os.path.join(output_directory, 'gray')
                os.makedirs(gray_dir, exist_ok=True)
                shutil.copy(os.path.join(stim_gray, f"{image}_gray.jpg"), gray_dir)

        # Save image metadata to CSV
        df_selected.to_csv(os.path.join(output_directory, 'selected_images.csv'), index=False)

        session.clear()
        # After download, show a confirmation message and button to start new selection
        return f"""
            <p>Download complete. Files saved to {output_directory}.</p>
            <a href="{url_for('index')}">
                <button>Start New Selection</button>
            </a>
        """

    except Exception as e:
        return f"<p>Error: {e}</p>"


if __name__ == '__main__':
    app.run(debug=True)
