# Kalkulator sederhana
def add(num1, num2):
    return num1 + num2
def substract(num1, num2):
    return num1 - num2
def division (num1, num2):
    return num1 / num2
def multiple (num1, num2):
    return num1 * num2

#menu

while True:	 
  print("Kalkulator sederhana")
  print("1. Pertambahan")
  print("2. Pengurangan")
  print("3. Pembagian") 
  print("4. Perkalian")
  print("5. Keluar")

  choice = input ("Apa yang anda perlukan: ")
  if choice == '5':
    break
  angka1 = float (input('Masukkan angka 1 = '))
  angka2 = float (input('Masukkan angka 2 = '))

  if choice == "1":
     print (angka1,"+",angka2,"=",add (angka1, angka2))
  elif choice == "2":
     print (angka1,'-',angka2,"=",substract (angka1, angka2))
  elif choice == "3":
     print (angka1,'/',angka2,'=',division (angka1, angka2))
  elif choice ==  "4":
     print (angka1,'*',angka2, "=",multiple (angka1, angka2))
  else:
     print ("wrong input/input salah")

