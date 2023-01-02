import random
szm1 = random.randint(0,24)
szm2 = random.randint(0,13)
szm3 = random.randint(0,3)
szemelyek = ["Berki Krisztián","Gyurcsány Ferenc","Orbán Viktor","Márki-Zay Péter","Karácsony Gergely","A dollár baloldal","a fidesz","Zámbó Kriszián","Zámbo Jimmy","Erzsike néni","Ronáldinyo"
,"Jakab Péter","Szopófantom","Segg titán","Novák Katalin","Gulyás Gergely","Német Szilárd"," szegedi férfi","A csöves","Viccelek","XVI. Benedek pápa","Soros György","Brüsszel","A migráns","libernyák"]

cselekves = ["beszart sőt össze is fosta magát","meghalt mégis tulélte","Meggyilkolta volt élettársát","Lopott autóval döntött ki egy villanypóznát","Fagyhaláltól mentették meg",
"Másfél hétig lakott egy kecskeméti szállodában, de nem akart fizetni","Ez lehetett " + szemelyek[szm1] + " valódi arca??","emlékezetes sexjelenetei","teljesen meztelenre vetkőzött",
"Mindenkit megőrjít a hosszúcombú " + szemelyek[szm1] + " csábító kacérkodása","Egy egészen kicsi bikiniben élvezi a pihenést","bikiniben mosolyog az új fotóján","radikális iszlamista " + szemelyek[szm1] + " támadt machetével a rendőrökre szilveszterkor New Yorkban",
"A vonat elé löktött egy 3 éves gyereket"]
fajta = ["-fotó","-videó","-képek"," "]
if cselekves[szm2] == "Ez lehetett " + szemelyek[szm1] + " valódi arca??":
    print (cselekves[szm2], fajta[szm3])  
elif cselekves[szm2] == "Mindenkit megőrjít a hosszúcombú " + szemelyek[szm1] + " csábító kacérkodása":
    print (cselekves[szm2], fajta[szm3])  
elif cselekves[szm2] == "radikális iszlamista " + szemelyek[szm1] + " támadt machetével a rendőrökre szilveszterkor New Yorkban":
    print (cselekves[szm2], fajta[szm3])
else:
    print (szemelyek[szm1],cselekves[szm2], fajta[szm3])
