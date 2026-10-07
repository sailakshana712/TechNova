## Quality Check and Notes (Person 3)

### Image quality check
Checks if an MRI is too blurry, too dark, too bright or low contrast.
Cutoff numbers were set by measuring 20 normal images against
blurred/darkened copies of them (not guessed).
- Caught 80 of 80 degraded images
- Wrongly flagged 1 of 20 normal images
- Limitation: does not detect noise, because noise makes an
  image look sharper to the blur formula

### Notes reader
Finds symptom sentences in a doctor's note using keyword rules.
Every quote returned is checked to exist in the original note,
so it cannot invent text.
- All 8 test notes are SYNTHETIC (made up). No real patient data.
- Works on clear notes, handles empty notes without crashing
- Limitation: misses abbreviations like "HA" (headache) and
  "N/V" (nausea/vomiting)

### Test cases
8 synthetic notes: 3 matching tumours, 2 irrelevant,
1 contradicting (pair with a no-tumour MRI), 1 empty, 1 messy.