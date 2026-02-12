class Person:
  def __init__(self, nama, gender, umur):
    self.nama = nama
    self.gender = gender
    self.umur = umur

class karyawan:
  def __init__(self, nama,gender,umur,gaji,):
    Person.__init__(self, nama, gender, umur)
    self.__gaji = gaji

  def get_gaji(self):
   print(self._gaji)

   def set_gaji(self,ngaji):
        self._gaji = ngaji
        print("Gaji Berhasil Diubah")

class  rekening:
  def __init__(self, norek, pin):
    self.norek = norek
    self.__pin = pin

  def get_pin(self):
        print(self.__pin)

  def set_pin(self, pinBaru):
      self.__pin = pinBaru
      print("PIN Berhasil Diganti")
    