## Model and explanation

**Model:** ResNet-18 (ImageNet pre-trained), fine-tuned for 6 epochs on the
Kaggle "Brain Tumor MRI Dataset" to classify scans as glioma, meningioma,
pituitary, or no tumour. Input is resized to 224x224. The checkpoint with the
best validation accuracy was kept.

**Results (on this dataset's held-out test split, 1,600 images):**

| Class | Precision | Recall |
|---|---|---|
| glioma | 0.97 | 0.82 |
| meningioma | 0.90 | 0.96 |
| notumor | 0.90 | 1.00 |
| pituitary | 0.99 | 0.97 |

Overall accuracy: **94%**. Confusion matrix (rows = true, columns = predicted,
order: glioma, meningioma, notumor, pituitary):

    [[328  35  37   0]
     [  4 383   9   4]
     [  0   0 400   0]
     [  5   7   0 388]]

Full report: `assets/report.txt`.

**Main weakness:** gliomas are missed most often (recall 0.82). 37 of 400 test
gliomas were predicted as "no tumour" and 35 as meningioma.

**Explanation (Grad-CAM):** the heatmap shows which image regions most
influenced the predicted class. It is coarse (computed on a 7x7 grid and
stretched to 224x224). In many images it highlights the central part of the
head rather than the exact tumour. The outline and box are made by
thresholding the heatmap. They are NOT a trained segmentation and are not a
tumour boundary. See `readme_pics/` for good and bad examples.

**Limitations:**
- Accuracy is measured on this dataset's test split only. This is not clinical
  accuracy. The public dataset may contain near-duplicate images, and there is
  no external validation.
- This is a demo, not a medical device. Do not use it for diagnosis.