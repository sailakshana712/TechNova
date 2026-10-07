# TechNova
Multimodal Medical Image Intelligence – HNX26PSI05


# Brain MRI Second Opinion

A tool that helps doctors review brain MRI scans. It is decision support, not a diagnosis.

## What it does
You upload a brain MRI and type a patient note. The app says which tumour type it suspects (glioma, meningioma, pituitary, or none), shows a heatmap and box of where it looked, quotes the patient note as evidence, and gives a confidence level. If a finding has no image region and no note quote, it is removed.

## Tech used
PyTorch (ResNet18), Grad-CAM, OpenCV, Streamlit

## How to run
git clone YOUR_REPO_LINK
cd YOUR_REPO_NAME
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py

## Data
Brain Tumor MRI Dataset from Kaggle (by Masoud Nickparvar). Patient notes are made up by us (synthetic).

## Results
Test accuracy: PUT_YOUR_NUMBER
Example input and output: see the outputs folder.

## What we built
Done: classifier, heatmap with box, confidence levels, note quotes, evidence check, image quality check, Streamlit app.
Not done: PUT_ANYTHING_YOU_SKIPPED

## Limitations
Small public dataset, not tested on real hospitals, not medically validated. The doctor always decides.
