def cetakSiku(x):  #Nomor 1
    for a in range(x):
        print((a+1)*"*")



def gambarlahPersegiEmpat(a,b):  #Nomor2
    for i in range(a):
        if(i==0):
            print(b*"@")
        elif(i==a-1):
            print(b*"@")
        else:
            print("@" + " " * (b-2) + "@")



def jumlahHurufVokal(x):  #Nomor3 a
    vokal = "aiueoAIUEO"
    a = 0
    hasil = 0

    for i in x:
        if i in vokal:
            a = a+1
    hasil = len(x),a
    return hasil



def jumlahHurufKonsonan(x): #Nomor3 b
    vokal = "aiueoAIUEO"
    a = 0
    hasil = 0

    for i in x:
        if i in vokal:
            a = a+1
    hasil = len(x),len(x)-a
    return hasil



def rerata(b):  #Nomor4
    jumlah = 0
    for i in range(len(b)):
        jumlah += b[i]
    jumlah = jumlah/len(b)
    return jumlah




from math import sqrt as sq  #Nomor5
def apakahPrima(n):
    n = int(n)
    assert n>=0
    primaKecil = [2,3,5,7,9,11]
    bukanPrKecil = [0,1,4,6,8,9,10]
    if(n in primaKecil):
        return True
    elif(n in bukanPrKecil):
        return False
    else:
        for i in range(2, int(sq(n))+1):
            if(n%i==0):
                return False
        return True



def bilanganPrima(n):  #Nomor6
    bawah = 2
    atas = 1000
    if(bawah >= 1 and atas > 1):
        for i in range(bawah,atas):
            prima = True
            for j in range(2,i):
                if(i%j==0):
                    prima=False
            if(prima == True):
                print(i)
    else:
        print("Bukan Bilangan Prima")



def faktorPrima(x):  #nomor7
    bilanganList = []
    loop = 2
    while loop <= x:
        if x % loop == 0:
            x /= loop
            bilanganList.append(loop)
        else:
            loop += 1
    return bilanganList



def apakahTerkandung(a,b):  #Nomor8
    x = True
    for i in range(len(b)):
        if a in b:
            x = True
        else:
            x = False
    return x



def kelipatan(x):  #Nomor9
    for i in range(x):
        if(i<=0):
            pass
        elif(i%3==0 and i%5==0):
            print 'Python UMS'
        elif (i%3==0):
            print 'Python'
        elif(i%5==0):
            print 'UMS'
        else:
            print i



from math import sqrt as detr  #Nomor10
def selesaikanABC(a,b,c):
    a = float(a)
    b = float(b)
    c = float(c)
    D = float(b*2 - 4*a*c)
    if(D < 0):
        hasil = "Determinan negatif, persamaan tidak mempunyai akar real"
        return hasil
    else:
        x1 = (-b + detr(D)) / (2*a)
        x2 = (-b + detr(D)) / (2*a)
        return hasil



def apakahKabisat(tahun): #Nomor11
    hasil = False
    if(tahun%4==0 and tahun%100!=0 and tahun%400!=0):
        hasil = True
    elif(tahun%100==0 and tahun%400!=0):
        hasil = False
    elif(tahun%400==0):
        hasil = True
    else:
        hasil = False
    return hasil



import random  #Nomor12
def tebak():
    a = random.randrange(1,101,1)
    b = -1
    n = 0
    print("Permainan Tebak Angka")
    print("Saya Menyimpan Sebuah Angka Bulat antara 1 sampai 100. Coba Tebak.")

    while(a != b):
        n = n + 1
        b = int(input("Masukkan Tebakan ke- " + str(n) + ":> "))
        if(b < a):
            print("Itu Terlalu Kecil. Coba lagi")
        elif(b > a):
            print("Itu Terlalu Besar. Coba lagi")
        else:
             print("Ya. Anda Benar.")
             break



def katakan(bilangan):  #Nomor13
    angka = ["","Satu","Dua","Tigas","Empat","Lima","Enam",
             "Tujuh","Delapan","Sembilan","Sepuluh","Sebelas"]
    Hasil = " "
    n = int(bilangan)
    if(n>=0 and n<=11):
        Hasil = Hasil + angka[n]
    elif(n < 20):
        Hasil = katakan(n%10) + " Belas"
    elif(n < 100):
        Hasil = katakan(n/10) + " Puluh" + katakan(n%10)
    elif(n < 200):
        Hasil = " Seratus" + katakan(n-100)
    elif(n < 1000):
        Hasil = katakan(n/100) + " Ratus" + katakan(n%100)
    elif(n < 2000):
        Hasil = " Seribu" + katakan(n-1000)
    elif(n < 10000):
        Hasil = katakan(n/1000) + " Ribu" + katakan(n%1000)
    elif(n < 20000):
        Hasil = " Sepuluh Ribu" + katakan(n-10000)
    elif(n < 100000):
        Hasil = katakan(n/10000) + " Puluh" + katakan(n%10000)
    elif(n < 200000):
        Hasil = " Seratus" + katakan(n-100000)
    elif(n < 1000000):
        Hasil = katakan(n/100000) + " Ratus" + katakan(n%100000)
    elif(n < 2000000):
        Hasil = " Satu Juta" + katakan(n-1000000)
    elif(n < 10000000):
        Hasil = katakan(n/1000000) + " Juta" + katakan(n%1000000)
    elif(n < 20000000):
        Hasil = " Satu Milyar" + katakan(n-10000000)
    else:
        Hasil = "Angka hanya sampai satu milyar"
    return Hasil



def formatRupiah(bilangan):  #Nomor14
    a = str(bilangan)
    if(len(a) <= 3):
        return "Rp " + a
    else:
        y = a[-3:]
        z = a[:-3]
        return formatRupiah(z) + "." + y
        print "Rp " + formatRupiah(z) + "." + y
