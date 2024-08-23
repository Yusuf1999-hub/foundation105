from datetime import date

class Dori:
    def __init__(self, nomi, kompaniya, narxi, muddati, tasir):
        self.d_name = nomi
        self.d_kompaniya = kompaniya
        self.d_tan_narx = narxi
        self.d_muddat = muddati
        self.d_tasir = tasir


class Apteka:
    def __init__(self, nomi):
        self.name = nomi
        self.dori_royxat = {}
        self.__kassa = 10000
        
    def set_kassa(self, dori_nomi:str, miqdor):
        if dori_nomi.capitalize() in self.dori_royxat:
            if miqdor <= self.dori_royxat[dori_nomi.capitalize()]['miqdor']:
                self.__kassa += (miqdor * self.dori_royxat[dori_nomi.capitalize()]['narx'])
                self.dori_royxat[dori_nomi.capitalize()]['miqdor'] -= miqdor
            else:
                print(f"{dori_nomi} siz so'ragan miqdorda mavjud emas")
                tasir = self.dori_royxat[dori_nomi.capitalize()]['tasir']
                for i in self.dori_royxat:
                    if self.dori_royxat[i]['tasir'] == tasir and miqdor <= self.dori_royxat[i]['miqdor']:
                        print(f"Sizga yordam beruvchi {i} nomli dori bor ekan kerakmi: ")
                        if int(input(">>> ")):
                            self.__kassa += (miqdor * self.dori_royxat[i]['narx'])
                            self.dori_royxat[i]['miqdor'] -= miqdor
        else:
            print("Bunday dori bizda mavjud emas")
        

    def dori_ochir(self, dori_nomi):
        if dori_nomi in self.dori_royxat:
            self.dori_royxat[dori_nomi]['miqdor'] = 0
            self.dori_royxat[dori_nomi]['muddat'] = ""
        

    def dori_qosh(self, obj:Dori, miqdor):
        if obj.d_name not in self.dori_royxat:
            self.dori_royxat[obj.d_name] = {
                'tasir' : obj.d_tasir,
                'narx'  : obj.d_tan_narx*2,
                'muddat': obj.d_muddat,
                'komp'  : obj.d_kompaniya,
                'miqdor': miqdor
            }
        else:
            self.dori_royxat[obj.d_name]['miqdor'] += miqdor
            self.dori_royxat[obj.d_name]['muddat'] = obj.d_muddat


        

    def tasir_boyicha(self):
        pass

    def srok_tekshir(self):
        for i in self.dori_royxat:
            mud = self.dori_royxat[i]['muddat'].split('.')[::-1]
            bugun = str(date.today()).split('-')

            dori_srogi = date(int(mud[0]), int(mud[1]), int(mud[-1]))
            bugun_srogi = date(int(bugun[0]), int(bugun[1]), int(bugun[-1]))

            if(dori_srogi < bugun_srogi):
                self.dori_ochir(i)

    def __str__(self):
        return f"""
Name: {self.name}
Dori_royxat: {[(i, self.dori_royxat[i]['miqdor']) for i in self.dori_royxat]}
"""


d1 = Dori("Trimol", "Ajanta pharma Limited", 1000, '12.05.2024', 'bosh')
d2 = Dori("Traykor", "Abbot Labaratories", 115000, '12.12.2024', 'yurak')
d3 = Dori("Teraflyu", "Novartis Konsyumer", 1200, '31.08.2024', 'grip')
d4 = Dori("Aspirin", "Shayana Pharm", 500, '10.10.2024', "bosh")
d5 = Dori("Mezim", "HINDI", 28000, '11.09.2024', 'oshqozon')
 

a1 = Apteka("777")

a1.dori_qosh(d1, 10)
a1.dori_qosh(d4, 55)

a1.set_kassa("trimol", 11)

print(a1)

a1.srok_tekshir()

print(a1)


