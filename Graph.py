class Peta:
  def __init__(self):
    self.cityList = {}

  def printPeta(self):
    for kota in self.cityList:
      print(kota, ":",self.cityList[kota])

  def tambahkanKota(self,kota):
    if kota not in self.cityList:
      self.cityList[kota] = []
      return True
    return False

  def hapusKota(self,kotaDihapus):
    #cek apakah kota yang ingin dihapus ada di list
    if kotaDihapus in self.cityList:
    #iterasi setiap kotalain untuk hapus kotadihapus
      for kotalain in self.cityList:
        #cek apakah kota yang ingin dihapus ada jalannya ke kotalain
        if kotaDihapus in self.cityList[kotalain]:
          self.cityList[kotalain].remove(kotaDihapus)
      del self.cityList[kotaDihapus]
      return True
    return False
