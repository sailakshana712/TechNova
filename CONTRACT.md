# CONTRACT

Rule sheet: what each function takes IN and gives OUT.
Everyone must follow this so our code fits together.

```python
CLASSES = ["glioma", "meningioma", "notumor", "pituitary"]   # alphabetical = ImageFolder order

quality.check_quality(pil_img)    -> {"score": 0-1, "blur": f, "brightness": f, "contrast": f, "warnings": [str]}
model.predict(pil_img)            -> {"glioma": .02, "meningioma": .90, "notumor": .05, "pituitary": .03}
gradcam.explain(pil_img, cls)     -> {"overlay": np.ndarray, "box": [x1,y1,x2,y2] or None, "area_frac": f, "contour": ndarray or None}
notes.extract(note_text, cls)     -> [{"quote": "headaches for 3 weeks", "keyword": "headache"}]   # quotes verified to exist in note
notes.red_flags(note_text)        -> True/False   # any worrying symptoms in the note?
fusion.build_report(pil_img, note_text) -> {"quality":{}, "probs":{}, "findings":[{"condition","confidence","band","region","note_evidence"}], "mismatch": str or None, "disclaimer": str}
```

All box coordinates are in 224x224 space. The UI scales them for display.