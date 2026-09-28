# Count nucleotides in a DNA sequence
with open("dna_input.txt") as f:
    dna = f.read().strip().upper()

counts = {base: dna.count(base) for base in "ACGT"}
print(counts["A"], counts["C"], counts["G"], counts["T"])
