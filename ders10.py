import sqlite3

baglanti = sqlite3.connect("kutuphane.db")
cursor = baglanti.cursor()

def tabloOlustur():
    cursor.execute("CREATE TABLE IF NOT EXISTS Kitaplik (Isim TEXT, Yazar TEXT, Yayinevi TEXT, SayfaSayisi INT)")
    #cursor.execute("INSERT INTO Kitaplik")
    baglanti.commit()

#tabloOlustur()
def veriEkle():
    cursor.execute("INSERT INTO Kitaplik VALUES('Safahat', 'Mehmet Akif Ersoy', 'Anka', 500)")
    baglanti.commit()

#veriEkle()
def veriEkle2(isim,yazar,yayinevi,sayfaSayisi):
    cursor.execute("INSERT INTO Kitaplik VALUES (?,?,?,?)",(isim,yazar,yayinevi,sayfaSayisi))
    baglanti.commit()

#veriEkle2("Suç Ve Ceza","Dostoyevski","Eren",562)
def veriEkle3(isim,yazar,yayinevi,sayfaSayisi):
    cursor.execute("INSERT INTO Kitaplik VALUES (?,?,?,?)",(isim,yazar,yayinevi,sayfaSayisi))
    baglanti.commit()

#isim = input("Kitap ismi: ")
#yazar = input("Yazar ismi: ")
#yayinevi = input("Yayınevi ismi: ")
#sayfaSayisi = input("Sayfa sayısı: ")
#veriEkle3(isim,yazar,yayinevi,sayfaSayisi)

def veriAl():
    cursor.execute("SELECT * FROM Kitaplik")
    liste = cursor.fetchall()  #
    print( liste)
    for i in liste:
        print("Tupple List: ",i)

#veriAl()

def veriAl2():
    cursor.execute("SELECT Isim,Yazar FROM Kitaplik")
    liste = cursor.fetchall() 
    print( liste)
    for i in liste:
        print("Tupple List: ",i)

#veriAl2()

def veriAl3(yayinevi):
    cursor.execute("SELECT * FROM Kitaplik WHERE Yayinevi=?",(yayinevi,))
    liste = cursor.fetchall() 
    print("Liste: ",liste)
    for i in liste:
        print("Tupple List: ",i)

#veriAl3("Karaca")

def veriAl4(yazar):
    cursor.execute("SELECT Yayinevi,SayfaSayisi FROM Kitaplik WHERE Yazar=?",(yazar,))
    liste = cursor.fetchall() 
    print("Liste: ",liste)
    for i in liste:
        print("Yayınevi: ",i[0])
        print("SayfaSayisi: ",i[1])
#veriAl4("Enes")

def veriGuncelle(eskiYayievi,yeniYayinevi):
    cursor.execute("UPDATE Kitaplik SET Yayinevi=? WHERE Yayinevi=?",(yeniYayinevi, eskiYayievi,))
    baglanti.commit()

#veriGuncelle("Karaca","Kara")

def veriSil(yazar):
    cursor.execute("DELETE FROM Kitaplik WHERE Yazar=?",(yazar,))
    baglanti.commit()

veriSil("Enes")

baglanti.close()