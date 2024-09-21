# final_project
Final Project of the course "Google IT Automation with Python"

# Context

The work is for an online fruits store, who needs to develop a system that will update the catalog information with data provided by the suppliers. The suppliers send the data as large images with an associated description of the products in two files (.TIF for the image and .txt for the description). The images need to be converted to smaller jpeg images and the text needs to be turned into an HTML file that shows the image and the product description. The contents of the HTML file need to be uploaded to a web service that is already running using Django. You also need to gather the name and weight of all fruits from the .txt files and use a Python request to upload it to your Django server.

The Python script should process the images and descriptions and then update company's online website to add the new products.

Once the task is complete, the supplier should be notified with an email that indicates the total weight of fruit (in lbs) that were uploaded. The email should have a PDF attached with the name of the fruit and its total weight (in lbs).

Finally, in parallel to the automation running, there will be a health check of the system which will send an email if something goes wrong.

# Content

This repository is composed by the following scripts:

1) changeImage.py - converts .TIFF images and to .JPEG alongside the resolution
2) supplier_image_upload.py - uploads the convert images into a web server catalog
3) run.py - converts the .TXT files into a JSON with the appropriate structure and upload them to the web server
4) reports.py - generate a PDF file to send to the supplier, indicating that the data was correctly processed
5) emails.py - notify supplier with the uploaded content
6) main.py - will run all the above scripts in the correct order
7) health_check.py - monitors some system statistics and will notify users if something is wrong
