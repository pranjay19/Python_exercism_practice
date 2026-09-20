def to_rna(dna_strand):

   
    new_list=[]
    for i in dna_strand:
        if i=="G":
            new_list.append("C")
        elif i=="C":
            new_list.append("G")
        elif i=="T":
            new_list.append("A")
        else:
            new_list.append("U")

    rna_stand="".join(new_list)
    return rna_stand
            