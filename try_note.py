from notes import extract, red_flags

note = "45F, progressive headaches for 3 weeks. New-onset seizure."
print(extract(note, "glioma"))
print(red_flags(note))