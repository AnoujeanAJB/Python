class REGLE:
    def __init__(self,amorce="aucun",nomfichier=False,extension=[],nomDuFichier,aPartirDe,prefixe,suffixe):
        self.amorce=amorce
        self.nomfichier=nomfichier
        self.extension=extension
        self.nomDuFichier=nomDuFichier
        self.aPartirDe=aPartirDe
        self.prefixe=prefixe
        self.postfixe=suffixe
        
    def __str__(self):
        text=self.amorce+","+self.nomfichier+","+self.nomDuFichier+","+self.aPartirDe+","+self.prefixe+","+self.postfixe+","+self.extension

    def Get_amorce(self):
        return self.amorce

    def Set_amorce(self, amorce):
        self.amorce=amorce

    def Get_nomfichier(self):
        return self.nomfichier

    def Set_amorce(self, nomfichier):
        self.nomfichier=nomfichier

    def Get_nomDuFichier(self):
        return self.nomDuFichier

    def Set_nomDuFichier(self, nomDuFichier):
        self.nomDuFichier=nomDuFichier

    def Get_aPartirDe(self):
        return self.aPartirDe

    def Set_aPartirDe(self, aPartirDe):
        self.aPartirDe=aPartirDe

    def Get_prefixe(self):
        return self.prefixe

    def Set_prefixe(self, prefixe):
        self.prefixe=prefixe

    def Get_postfixe(self):
        return self.postfixe

    def Set_prefixe(self, postfixe):
        self.postfixe=postfixe

    def Get_extension(self):
        extension=""
        for ext in self.extension:
            extension=extension+ext+", "
        return extension

    def Set_extension(self, extension):
        self.extension.append(extension)
