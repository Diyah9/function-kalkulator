print ('\t\t*************************************')
print ('\t\t*          KALKULATOR               *')
print ('\t\t*************************************')
def fungsi(nilai1,nilai2,tugas):
    if tugas =="+":
        hasil = nilai1+nilai2
    elif tugas =="-":
        hasil = nilai1-nilai2
    elif tugas =="*":
        hasil = nilai1*nilai2
    elif tugas =="/":
        hasil = nilai1/nilai2

    return hasil
    
