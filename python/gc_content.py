
def calculate_gc_content(dna):
    dna = dna.upper()
    gc = dna.count('G') + dna.count('C')
    gc_content = (gc / len(dna)) * 100
    return gc_content
   dna = "ATGCGCTA"
print(calculate_gc_content(dna)) 
