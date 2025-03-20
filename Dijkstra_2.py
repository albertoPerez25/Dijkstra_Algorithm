import folium
# Para dibujar el mapa de salida
import geopy
# Para calcular distancia euclídea
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
app = Nominatim(user_agent="tycgis")
from folium.plugins import MiniMap
# import requests module 
import requests
import ipywidgets as widgets
import time
import os
import pandas as pd
from time import time


pueblos = {
 'Adra': (36.75932403011123, -2.9959979099413623),
 'Abrantes': (39.4631905, -8.1973618),
 'Adanero': (40.9438737, -4.6038249),
 'Ágreda': (41.8548465, -1.9214614),
 'Aguilar de Campoó': (42.7928369, -4.2605438),
 'Alacant': (38.3436365, -0.4881708),
 'Albocàsser': (40.3571915, 0.0245058),
 'Albufeira': (37.088241, -8.2526339),
 'Alcalá de Henares': (40.4818396, -3.3644973),
 'Alcance': (39.2535359, -1.0961698),
 'Alcantarilla': (37.9680342, -1.214954),
 'Alcañices': (41.6996962, -6.3471637),
 'Alcañiz': (41.0505393, -0.1307197),
 'Alcaraz': (38.6647483, -2.4910801),
 'Alcolea del Pinar': (41.0359238, -2.4673489),
 'Alcoy': (38.6982275, -0.4747767),
 'Alfaro': (42.1785741, -1.7492454),
 'Algeciras': (36.1311725, -5.4473991),
 'Almadén': (38.7742489, -4.832835),
 'Almadrones': (40.9012507, -2.7737105),
 'Almansa': (38.8682065, -1.0978627),
 'Almazán': (41.4870645, -2.5335988),
 'Almonte': (37.2611686, -6.5175751),
 'Almuñecar': (36.7328699, -3.68968),
 'Alzira': (39.151212, -0.4346556),
 'Amposta': (40.7079905, 0.5827636),
 'Andújar': (38.0392362, -4.0505603),
 'Ansiao': (39.9113771, -8.4359857),
 'Antequera': (37.0183652, -4.5596649),
 'Aranda de Duero': (41.6715067, -3.6851172),
 'Aranjuez': (40.03221, -3.6039604),
 'Arenas de San Pedro': (40.2107266, -5.0868775),
 'Arévalo': (41.0632758, -4.7198921),
 'Arganda del Rey': (40.3007708, -3.4380688),
 'Armiñón': (42.722587, -2.8722115),
 'Arzúa': (42.92374955, -8.15281746981209),
 'Astorga': (42.4553555, -6.0529025),
 'Aveiro': (40.640496, -8.6537841),
 'Avilés': (43.5554436, -5.9222466),
 'Ayamonte': (37.215797, -7.4060169),
 'Ayora': (39.0596612, -1.057216),
 'Baamonde': (43.1395946, -7.5390136),
 'Baena': (37.6173035, -4.324371),
 'Bailén': (38.096787, -3.7765601),
 'Barbastro': (42.034453, 0.1264012),
 'Barreiros': (43.535368982783446, -7.24283944475006),
 'Basauri': (43.235372, -2.8920543),
 'Baza': (37.4888637, -2.7709805),
 'Becerrea': (42.8544959, -7.1616043),
 'Beja': (38.0154479, -7.8650368),
 'Béjar': (40.3865812, -5.7649619),
 'Belmonte': (39.5592831, -2.7038117),
 'Benabarre': (42.1063137, 0.4820182),
 'Benavente': (42.0032862, -5.6738595),
 'Benicarló': (40.4180244, 0.4229813),
 'Benicàssim': (40.0554964, 0.0644165),
 'Benidorm': (38.5406255, -0.1290929),
 'Betanzos': (43.2757359, -8.23264173925292),
 'Bicorp': (39.1323971, -0.7877353),
 'Boltaña': (42.4457355, 0.0680185),
 'Borriol': (40.0422215, -0.0714919),
 'Braga': (41.5510583, -8.4280045),
 'Bragança': (41.5084468, -6.773302360533066),
 'Burgo de Osma': (41.5868712, -3.0674254),
 'Calatayud': (41.3527628, -1.6422977),
 'Caldas da Rainha': (39.4071857, -9.1346004),
 'Callosa del Segura': (38.3460486, -0.4944558),
 'Campillos': (37.0470137, -4.8621698),
 'Campomanes': (43.1054181, -5.8185558),
 'Cangas de Onís': (43.3136138, -5.065850290011571),
 'Cañete': (40.041797, -1.6490269),
 'Carballo': (43.2134123, -8.6891286),
 'Carboneras': (36.9968699, -1.8946552),
 'Carregado': (39.0055219, -8.9537297),
 'Cartagena': (37.60675362409654, -0.9841418509354086),
 'Casas Ibáñez': (39.2869161, -1.4706566),
 'Casa de Juan Gil': (39.126944, -1.2425),
 'Cascais': (38.6968919, -9.4204495),
 'Caspe': (41.2368564, -0.0394889),
 'Castelldefels': (41.2861022, 1.9824173),
 'Castelo Branco': (39.97675825, -7.446059929966704),
 'Castro Urdiales': (43.3843347, -3.2162576),
 'Caudete': (38.706703, -0.9867978),
 'Cerceda': (43.08523156594481, -3.4486988299225527),
 'Cervera': (41.670378400000004, 1.2680142494341275),
 'Chantada': (42.61090765, -7.810749170573104),
 'Chiclana de la Frontera': (36.4191096, -6.1460683),
 'Chiva': (39.4726098, -0.7178348),
 'Cieza': (38.2479256153942, -1.4182315889989041),
 'Cinctorres': (40.5825853, -0.2161136),
 'Cistierna': (42.8031437, -5.1255957),
 'Cocentaina': (38.744158, -0.4400707),
 'Coimbra': (40.2111931, -8.4294632),
 'Collado Villalba': (40.6431496, -3.9930128),
 'Coruche': (38.958218, -8.5283498),
 'Covilha': (40.2804021, -7.504191),
 'Cudillero': (43.54335745, -6.1936313237885),
 'Cullera': (39.1647217, -0.2542313),
 'Daimiel': (39.072196, -3.6143611),
 'Daroca': (41.1133264, -1.4170637),
 'Dos Hermanas': (37.283689, -5.9226718),
 'Durango': (43.17773905907672, -2.6240870550508753),
 'Durcal': (36.9879333, -3.5663828),
 'Écija': (37.5406007, -5.079589),
 'El Barco de Ávila': (40.3577409, -5.5231241),
 'El Burgo del Ebro': (41.5599303, -0.7204564),
 'Elda': (38.4789671, -0.7956759),
 'Elvas': (38.8806123, -7.1637237),
 'Elx': (38.2653307, -0.6988391),
 'Espiel': (38.1885533, -5.0189717),
 'Espinho': (41.0083643, -8.6394111),
 'Estepa': (37.29204, -4.8781876),
 'Estepona': (36.4268068, -5.1468484),
 'Estremoz': (38.8432944, -7.586907),
 'Évora': (38.5707742, -7.9092808),
 'Faro': (37.0162727, -7.9351771),
 'Feira': (40.9316799, -8.552306217314651),
 'Ferrol': (43.4846862, -8.233162),
 'Figueira da Foz': (40.1485808, -8.855655),
 'Figueres': (42.2666314, 2.9638434),
 'Fraga': (41.5221304, 0.3501756),
 'Fuengirola': (36.5388398, -4.6233974),
 'Gaia': (41.122811404202224, -8.616241437568595),
 'Gandia': (38.9675925, -0.1803423),
 'Gibraleón': (37.3746324, -6.9690748),
 'Gijón': (43.53819155356016, -5.665131371077161),
 'Gimileo': (42.5494612, -2.8229957),
 'Grado': (43.386210140855724, -6.074232865258658),
 'Grândula': (38.1790, -8.5648164),
 'Graus': (42.189949, 0.3389797),    
 'Grao de Sagunt': (39.64670082183546, -0.2853007827378621),
 'Guadiaro': (36.300318, -5.301881),
 'Guarda': (40.7046066, -7.195139236071309),
 'Guardamar del Segura': (38.0899985, -0.65381),
 'Guntín': (42.90121465, -7.657714434445812),
 'Hellín': (38.5106649, -1.6995137),
 'Herrera del Duque': (39.1676109, -5.0504659),
 'Híjar': (41.1747377, -0.4515985),
 'Honrubia': (39.613532, -2.2807538),
 'Ibi': (38.623288, -0.5730513),
 'Igualada': (41.5790182, 1.617346),
 'Izurzun': (43.31449706566802, -2.002465215572012),
 'Jabugo': (37.9168052, -6.7291607),
 'Jaca': (42.5692515, -0.549372),
 'Jerez de la Frontera': (36.681727, -6.139157),   
 'La Albuera': (38.7172283, -6.8230848),
 'La Bañeza': (42.2998096, -5.8970081),
 'La Espina': (43.2647914, -3.3880441),
 'Lagos': (37.136773214712676, -8.688351586068762),
 'La Jonquera': (42.4207991, 2.8728485),
 "L'Alcora": (40.0744223, -0.2138589),
 'Lalín': (42.6614127, -8.1109759),
 'La Línea de la Concepción': (36.1677899, -5.3482396),
 'La Magdalena': (42.78535541199772, -5.799146099403363),
 'Laredo': (43.40694714305638, -3.4165607026463864),
 'La Roda': (39.20702, -2.1581637),
 "La Seu d'Urgell": (42.3575723, 1.4560067),
 'La Unión': (37.6219632, -0.8827593),
 'Leiria': (39.7437902, -8.8071119),
 'León': (42.63414505, -5.971415104539984),
 'Lepe': (37.2551712, -7.201556),
 'Lerma': (42.0262334, -3.7559335),
 'Les Borges Blanques': (41.5203322, 0.8684098),
 "L'Hospitalet de l'Infant": (40.9930816, 0.9226161),
 'Linares': (38.0931247, -3.6357609),
 'Liria': (39.6251478, -0.5952749),
 'Llanes': (43.4211205, -4.7530835),
 'Llerena': (38.2378976, -6.0149901),
 'Llivia': (42.4640786, 1.9804293),
 'Loja': (37.1664839, -4.1496374),
 'Lorca': (37.6712139, -1.6990431),
 'Losa del Obispo': (39.695763, -0.8710594),
 'Los Alcázares': (37.7466009, -0.8556533),
 'Los Gallardos': (37.1675863, -1.9394052),
 'Luarca': (43.5439003, -6.5357408),
 'Lucena': (37.4091334, -4.4860128),
 'Lugo': (43.0396042, -7.456607166509571),
 'Macedo de Cavaleiros': (41.5362124, -6.9560267),
 'Madridejos': (39.4708879, -3.5355038),
 'Manresa': (41.7288939, 1.8286765),
 'Mansilla de la Mulas': (42.497603, -5.415263),   
 'Manzanares': (38.9962242, -3.3722143),
 'Maqueda': (40.06533, -4.3720335),
 'Marbella': (36.508976, -4.88562),
 'Marín': (42.3922393, -8.7029421),
 'Mataró': (41.5398348, 2.4448926),
 'Mazagón': (37.14597, -6.8562644),
 'Medinaceli': (41.1723392, -2.4353741),
 'Medina del Campo': (41.3085496, -4.9150256),
 'Mérida': (38.9174665, -6.3443977),
 'Mieres': (43.2488161, -5.7722468),
 'Miranda del Ebro': (42.788628, -3.3641992),
 'Mogadouro': (41.3418708, -6.7121674),
 'Molina de Aragón': (40.8491293, -1.8813995592876256),
 'Mombuey': (42.0226242, -6.3311768),
 'Monforte de Lemos': (42.5236693, -7.5096951),
 'Monóvar': (38.4387815, -0.8396316),
 'Monreal del Campo': (40.7896541, -1.3529881),
 'Montalbán': (40.8405106, -0.7945674618382108),
 'Montemor-o-Novo': (38.6481777, -8.2115858),
 'Montijo': (38.9098936, -6.6151799),
 'Montoro': (38.0215633, -4.3827296),
 'Monzón': (41.9143981, 0.1922412),
 'Morella': (40.6188277, -0.0998026),
 'Motril': (36.7450888, -3.5207655),
 'Murça': (41.42591455, -7.465569503607106),
 'Navalmoral de la Mata': (39.8928306, -5.5401199),
 'Navia': (43.5391112, -6.7233704),
 'Novelda': (38.3842144, -0.7674146),
 'Nueno': (42.2665821, -0.4393139),
 'Nules': (39.8532265, -0.1550092),
 'O Barco': (42.416462, -6.9843044),
 'Ocaña': (39.9586665, -3.5007717),
 'Odemira': (37.5976, -8.6422),
 'Oitura': (41.729177, -1.1932591),
 'Oliva': (38.9202443, -0.1208981),
 'Olot': (42.1822177, 2.4890211),
 'Onda': (39.9621514, -0.2593846),
 'Ontinyent': (38.8208523, -0.6099929),
 'Osorno': (42.4106725, -4.3609815),
 'Ourique': (37.651112, -8.2237262),
 'Padul': (37.0222913, -3.6274938),
 'Peniche': (39.3568749, -9.3786838),
 'Peñafiel': (41.5975136, -4.1227931),
 'Peñaranda de Bracamonte': (40.9024602, -5.2006416),
 'Peñíscola': (40.3576361, 0.4071043),
 'Piedrabuena': (39.0344592, -4.1753284),
 'Pinoso': (38.4021056, -1.041617),
 'Plasencia': (40.029921, -6.090168),
 'Pola de Siero': (43.3914146, -5.6608367),
 'Ponferrada': (42.5454124, -6.5938719),
 'Pont de Suert': (42.4079576, 0.7401693),
 'Ponteareas': (42.17561317640825, -8.5069639563138),    
 'Ponte de Lima': (41.7675021, -8.5830992),
 'Pontedeume': (43.4072585, -8.1718823),
 'Ponte do Sôr': (39.24832855, -8.012372917228461),
 'Portalegre': (39.2076447, -7.721513354015343),
 'Portbou': (42.4274333, 3.1588785),
 'Portman': (37.5911824, -0.8527408),
 'Porto': (41.1494512, -8.6107884),
 'Potes': (43.1536831, -4.623428),
 'Puertollano': (38.6852161, -4.1111749),
 'Puerto Lumbreras': (37.5635045, -1.8076233),
 'Puerto Real': (36.5286856, -6.1902161),
 'Puigcerdà': (42.4317966, 1.9278693),
 'Quintana del Puente': (42.0841001, -4.2074696),
 'Quintanilha': (41.7514181, -6.5700521),
 'Reinosa': (43.0010076, -4.1378363),
 'Requena': (39.4880777, -1.1001643),
 'Reus': (41.1555564, 1.1076133),
 'Riaza': (41.279379, -3.4772594),
 'Ribadavia': (42.2880044, -8.1429521),
 'Ribadeo': (43.5361589, -7.0436775),
 'Ribadesella': (43.4617129, -5.0587479),
 'Ribeira de Pena': (41.5217103, -7.795143),
 'Rincón de la Victorio': (36.718641739895496, -4.279642488207788),
 'Ripoll': (42.1982391, 2.1932496),
 'Ronda': (36.7421339, -5.1665916),
 'Ruidera': (38.977123, -2.8838992),
 'Sabiñánigo': (42.518364, -0.3647899),
 'Sacedón': (40.481085, -2.732881),
 'Sagunt': (39.6792916, -0.2786451),
 'Salamanca': (40.9651572, -5.6640182),
 'San Ciprián': (43.68631022379616, -7.459260592653653),
 'San Esteban de Gormaz': (41.574307, -3.2041516),
 'San Fernando': (36.4646672, -6.1983492),
 'San Rafael': (40.716319670498976, -4.1867767817737995),
 'Santa Pola': (38.1923641, -0.5555464),
 'Santarem': (39.2850041, -8.556447653068235),
 'Santiago de Compostela': (42.90645755, -8.51929826271505),
 "Sant Joan d'Alacant": (38.4014162, -0.4359957),
 'Santo Domingo de la Calzada': (42.4406711, -2.9536395),
 'Segorbe': (39.8519011, -0.4895537),
 'Serpa': (37.9436517, -7.5966902),
 'Setubal': (38.5241783, -8.8932341),
 'Silla': (39.3632045, -0.4112618),
 'Sines': (37.956549, -8.8689639),
 'Sintra': (38.79846, -9.3881),
 'Sitges': (41.2366707, 1.8228136),
 'Solares': (43.388846603816816, -3.7336059424529973),
 'Soria': (41.60125045, -2.721938035449954),
 'Sueca': (39.2025604, -0.3111645),
 'Tafalla': (42.5278279, -1.6744823),
 'Talavera de la Reina': (39.9603798, -4.8311717),
 'Tarancón': (40.0086075, -3.0102243),
 'Tarazona': (41.9065093, -1.7216461),
 'Tarifa': (36.0129082, -5.6050213),
 'Tavira': (37.1262493, -7.6499121),
 'Tordesillas': (41.500851, -5.00053),
 'Toro': (41.5216963, -5.3939824),
 'Torreblanca': (40.2202661, 0.1953363),
 'Torrelavega': (43.3487303, -4.0515082),
 'Torremolinos': (36.6242841, -4.4995448),
 'Torres Novas': (39.47962, -8.53955),
 'Torres Vedras': (39.0930856, -9.260741),
 'Torrevieja': (37.9775416, -0.6828446),
 'Totana': (37.7697645, -1.5025376),
 'Trujillo': (39.4605657, -5.8816626),
 'Tuj': (42.16978724230882, -8.62101807343588),
 'Úbeda': (38.0111494, -3.3718691),
 'Unquera': (43.3745998, -4.5145487),
 'Utiel': (39.5680838, -1.2051778),
 'Valdepeñas': (38.7594573, -3.3847392),
 'Valencia de Alcántara': (39.4131571, -7.2420859),
 'Valongo': (41.1909794, -8.4980511),
 'Valverde del Camino': (37.5739612, -6.7543559),
 'Vegadeo': (43.4153116, -6.999106571661519),
 'Vélez-Rubio': (37.6482765, -2.0745368),
 'Venta El Alto': (37.64697773887377, -6.157891419544876),
 'Venturada': (40.7985257, -3.6207369),
 'Vera': (37.2475942, -1.8681961),
 'Verín': (41.9406091, -7.4406032),
 'Viana do Castelo': (41.70416246220342, -8.809209172248952),    
 'Vic': (41.9302021, 2.2545943),
 'Vigo': (42.22388541452606, -8.729649369512089),    
 'Vielha': (42.7017572, 0.7954744),
 'Vila Flor': (41.3067941, -7.1517712),
 'Vilafranca del Cid': (40.4270485, -0.2577628),
 'Vilafranca del Penedés': (41.3463825, 1.6995213),
 'Vilagarcía de Arousa': (42.5947625, -8.7669178),
 'Vila Nova de Foz Côa': (41.0818397, -7.1424138),
 'Vila-real': (39.9372616, -0.1004465),
 'Vila Real': (41.278532346079366, -7.724376282447581),
 'Vilareal de Santo Antonio': (37.19302859757792, -7.424496347410952),    
 'Villalón de Campos': (42.0984494, -5.0347132),
 'Villarrobledo': (39.2681742, -2.6042132),
 'Villena': (38.6360967, -0.8659745),
 'Vinarós': (40.4703992, 0.4746076),
 'Viseu': (40.6574713, -7.9138664),
 'Xàtiva': (38.9880871, -0.5200052),
 'Xert': (40.5186118, 0.1585541),
 'Xinzo de Limia': (42.0637882, -7.7245498),
 'Yecla': (38.6135956, -1.1157882),
 'Zafra': (38.4253489, -6.4193627),
 'Zarauz': (43.2834873, -2.1723467),
 'Zuera': (41.8659094, -0.7886383)}
tam1 = len(pueblos)


ciudades = {
    'A Coruña' : (43.37012643, -8.39114853),
    'Albacete' : (38.99588053, -1.85574745),
    'Alicante' : (38.34548705, -0.4831832),
    'Almería' : (36.83892362, -2.46413188),
    'Ávila' : (40.65586958, -4.69771277),
    'Badajoz' : (38.87874339, -6.97099704),
    'Barcelona' : (41.38424664, 2.17634927),
    'Bilbao' : (43.25721957, -2.92390606),
    'Burgos' : (42.34113004, -3.70419805),
    'Cáceres' : (39.47316762, -6.37121092),
    'Cádiz' : (36.52171152, -6.28414575),
    'Castelló de la Plana' : (39.98640809, -0.03688142),
    # 'Ceuta' : (35.88810209, -5.30675127),
    'Ciudad Real' : (38.98651781, -3.93131981),
    'Córdoba' : (37.87954225, -4.78032455),
    'Cuenca' : (40.07653762, -2.13152306),
    'Donostia' : (43.31924454673363, -1.9832245902526295),
    'Girona' : (41.98186075, 2.82411899),
    'Granada' : (37.17641932, -3.60001883),
    'Guadalajara' : (40.63435548, -3.16210273),
    'Huelva' : (37.26004113, -6.95040588),
    'Huesca' : (42.14062739, -0.40842276),
    'Jaén' : (37.7651913, -3.7903594),
    # 'Las Palmas' : (28.09937855, -15.41336841),
    'León' : (42.59912097, -5.56707631),
    'Lisboa' : (38.72457546504939, -9.149236171829303),    
    'Lleida' : (41.61527355, 0.62061934),
    'Logroño' : (42.46644945, -2.44565538),
    'Lugo' : (43.0091282, -7.55817392),
    'Madrid' : (40.40841191, -3.68760088),
    'Málaga' : (36.72034267, -4.41997511),
    #'Melilla' : (35.294731, -2.942281),
    'Murcia' : (37.98436361, -1.1285408),
    'Ourense' : (42.33654919, -7.86368375),
    'Oviedo' : (43.36232165, -5.84372206),
    'Palencia' : (42.0078373, -4.53460106),
    #'Illes Balears' : (39.57114699, 2.65181698),
    'Pamplona' : (42.814102, -1.6451528),
    'Pontevedra' : (42.43381442, -8.64799018),
    'Salamanca' : (40.96736822, -5.66538084),
    'Gipuzkoa' : (43.31717158, -1.98191785),
    #'Santa Cruz de Tenerife' : (28.46285408, -16.24720629),
    'Santander' : (43.46297885, -3.80474784),
    'Segovia' : (40.9498703, -4.12524116),
    'Sevilla' : (37.38620512, -5.99251368),
    'Soria' : (41.76327912, -2.46624798),
    'Tarragona' : (41.11910287, 1.2584219),
    'Teruel' : (40.34412951, -1.10927177),
    'Toledo' : (39.85715187, -4.02431421),
    'Valencia' : (39.47534441, -0.37565717),
    'Valladolid' : (41.65232777, -4.72334924),
    'Vitoria' : (42.85058789, -2.67275685),
    'Zamora' : (41.49913956, -5.75494831),
    'Zaragoza' : (41.65645655, -0.87928652),

}
tam = len(ciudades)

# Hacemos una copia de las capitales
capitales = {}
for c in ciudades:
    capitales[c] = ciudades[c]

# Sumamos latitudes y longitudes para ajustar en el mapa con la media
lat = 0
long = 0
for i in ciudades:
    lat += ciudades[i][0]
    long += ciudades[i][1]



#
# Cálculo de la distancia euclídea, a efectos ilustrativos
# Procedente del paquete GeoPy
#
distancia = geodesic((ciudades['Albacete'][0], ciudades['Albacete'][1]), (ciudades['Madrid'][0], ciudades['Madrid'][1]))

# Ejemplo de uso
# La distancia es una información estructurada, para obtenerlo en formato numérico hay que especificar en kilómetros

print(distancia)
print(distancia.kilometers)

# La documentación puede consultarse en https://geopy.readthedocs.io/en/stable/



#
#  El fichero carreteras.txt debe establecerse con el path correspondiente a la ubicación en cada práctica
#
file_path = "./carreteras.txt"

data = pd.read_csv(file_path, delimiter = "\t")
dicCarreteras = {}
for row in data.itertuples():
    sp = row._1.split(':')
    dicCarreteras[(sp[0],sp[1])] = float(sp[2])


#
#  El fichero autovias.txt debe establecerse con el path correspondiente a la ubicación en cada práctica
#
file_path = "./autovias.txt"

data = pd.read_csv(file_path, delimiter = "\t")
dicAutovias = {}
for row in data.itertuples():
    sp = row._1.split(':')
    dicAutovias[(sp[0],sp[1])] = float(sp[2])


salida = folium.Map(location = [lat/tam, long/tam], zoom_start=6)
for i in ciudades:
    folium.Marker(
        location=[ciudades[i][0] , ciudades[i][1]],
        #icon=folium.Icon(color = 'red'),
        icon=folium.DivIcon(html=f"""
            <div><svg>
                <rect x="0", y="0" width="5" height="5", fill="black", opacity=".5" />
            </svg></div>"""),
            #<circle cx="0" cy="0" r="10" fill="#red" opacity=".5"/>
        popup=''
    ).add_to(salida)
    
    
salida


# Preparar el grafo

dist = {}
#Creamos un nuevo diccionario unión de los otros dos
ciudades.update(pueblos)
nodos = len(ciudades)
for i in ciudades:
    for j in ciudades:
        elem = (i, j)
        if elem in dicCarreteras.keys():
            dist[elem]  = dicCarreteras[elem]/90
            dist[(j,i)] = dicCarreteras[elem]/90
            # Los tramos de carreteras los consideramos a 90 km/h
        elif elem in dicAutovias.keys():
            dist[elem]  = dicAutovias[elem]/120
            dist[(j,i)] = dicAutovias[elem]/120     
            # Los tramos de autovía los consideramos a 120 km/h


###########################################################################################
###########################################################################################
# Esta clase implementa un diccionario de prioridad
#
class dicPrioridad:
    
    # Constructor. Opcionalmente toma una lista de pares
    # (elemento,valor)
    def __init__(self,objetos=[]):
        self.diccionario = {}
        self.vector = [ ]
        self.tamano = -1 # Realmente es el índice del último elemento.
        # Se insertan de uno en uno los objetos.
        for (elemento,valor) in objetos:
            item = (elemento, valor)
            self.inserta(item)
 
   # Inserta un elemento
    def inserta(self, item):
        # Lo añade al final
        self.vector.append(item)
        self.tamano += 1
        
        #
        #  TODO:COMPLETAR
        #
        
        # Obtiene el indice del nuevo elemento
        indice = self.tamano

        # Llama a up_heapify para restaurar la propiedad del heap
        self.up_heapify(indice)

        #print(self.vector, " | ",self.diccionario)

    # Extrae el elemento mínimo del diccionario de prioridad
    def extrae_min(self):
        # Si el tamaño es 0, no devuelve nada
        if self.tamano <= 0:
            return None
        #
        #  TODO:COMPLETAR
        #
        # Guarda el elemento mínimo (raíz)
        min_elemento = self.vector[0]

        # Reemplaza la raíz con el último elemento
        ultimo_elemento = self.vector.pop()
        self.tamano -= 1

        if self.tamano > 0: # Si hay elementos en el heap.
            self.vector[0] = ultimo_elemento
            # Restaura la propiedad del heap
            self.down_heapify(0)
        else:
            self.vector = [] # Si solo habia un elemento, ahora el vector queda vacio.

        # Actualiza el diccionario
        del self.diccionario[min_elemento[0]]
        #print(self.vector, " | ",self.diccionario)

        return min_elemento

    # Actualiza el valor de un elemento 
    def actualiza(self, item):
        # Posición del elemento que se va a modificar
        indice = self.diccionario[item[0]]
        # Se actualiza el elemento        
        self.vector[indice] = item

        #
        #  TODO:COMPLETAR
        #
        # Se actualiza el elemento        
        valor_anterior = self.vector[indice][1] # guarda el valor anterior
        self.vector[indice] = item
        valor_nuevo = self.vector[indice][1] # guarda el valor nuevo

        self.up_heapify(indice)
        return
        # Compara el valor nuevo con el valor anterior
        if valor_nuevo > valor_anterior:
            # Si el valor nuevo es mayor, usa up_heapify
            self.up_heapify(indice)
        elif valor_nuevo < valor_anterior:
            # Si el valor nuevo es menor, usa down_heapify
            self.down_heapify(indice)
            
            
    # Borra un elemento de la cola
    # No haremos uso de esta función
    def borra(self, elemento):
        # Si el elemento no está en el diccionario, vuelve
        if elemento not in self.diccionario:
            return
        # Índice del elemento
        indice = self.diccionario[elemento]
        # Lo intercambiamos con el último
        self.cambia_elementos(indice, self.tamano)
  
        # Borra el diccionario y del vector
        del(self.diccionario[elemento])
        del(self.vector[self.tamano])
        # Decrece el tamaño
        self.tamano -= 1        
        # Se arregla el heap
        # Se saca la posición del padre
        padre = self.nodopadre(indice)
        # Si el nodo tiene padre, y su valor es menor que el del padre
        self.up_heapify(indice)
        return
        if padre>0 and self.vector[indice][1]<self.vector[padre][1]:
            # Hace intercambio para arriba
            self.up_heapify(indice)
        # Si no
        else:
            # Hace intercambio para abajo
            self.down_heapify(indice)        
        
    # Reordena el diccionario de prioridad hacia arriba a partir del elemento
    # almacenado en la posicion indice (Ordena de mayor a menor, siendo el menor el que quedaria en la cabeza sin tener hijo)
    def up_heapify(self,indice):
        #print(f"up_heapify called with index: {indice}")
        # Si es la raíz del árbol, no hace nada.
        if indice == 0: 
            self.diccionario[self.vector[indice][0]] = indice
            return
        # Saca el padre
        padre = self.nodopadre(indice)

        # Si el valor del índice es mayor que el del padre
        # se cumple la propiedad.  
        if (self.vector[indice][1]>=self.vector[padre][1]): 
            # Metemos el valor en el diccionario
            self.diccionario[self.vector[indice][0]] = indice
            return indice
        # Si no, hace el intercambio, y llama a la función 
        # recursiva con el padre.     
        else: 
            self.cambia_elementos(padre, indice)
            self.up_heapify(padre)
            return
    
    # Reordena el diccionario de prioridad hacia abajo a partir del elemento
    # almacenado en la posicion indice
    def down_heapify(self,indice):
        # Extrae los índices de los hijos.
        hijoIz = self.hijo_izquierdo(indice)
        hijoDe = self.hijo_derecho(indice)
        
        # Si el índice del hijo izquierdo es mayor que el tamaño es que
        # no tiene hijos, y vuelve.
        if hijoIz>self.tamano:
            return
        # Si no tiene hijo derecho, o el valor del hijo izquierdo es menor, entonces
        # el hijo a considerar es el izquierdo
        if hijoDe>self.tamano or (self.vector[hijoIz][1] < self.vector[hijoDe][1]):
            hijo = hijoIz
        # Si tiene hijo derecho y el hijo izquierdo no es menor, entonces utiliza el
        # derecho.    
        else:
            hijo = hijoDe
        
        # Si el valor del hijo es menor que el del padre
        # intercambia y llama a la función recursiva con el hijo.
        if self.vector[hijo][1] < self.vector[indice][1]:
            self.cambia_elementos(indice, hijo)
            self.down_heapify(hijo)
            return
   
    
    # Intercambia dos elementos (han de ser padre e hijo)
    def cambia_elementos(self, nodo1, nodo2):
        # Cambia los valores en el diccionario. 
        self.diccionario[self.vector[nodo1][0]] = nodo2
        self.diccionario[self.vector[nodo2][0]] = nodo1
        # Cambia los valores en el vector
        self.vector[nodo2],self.vector[nodo1] = self.vector[nodo1],self.vector[nodo2]        
       
         
    # Devuelve la posición del padre del elemento almacenado en la posición
    # indice del vector    
    def nodopadre(self,indice):    
        if (indice%2==0):  
            return int((indice-2) / 2) # Hijo derecho
        else:  
            return int((indice-1) / 2) # Hijo izquierdo
    
    # Devuelve la posición del hijo izquierdo del elemento almacenado en la 
    # posición indice del vector        
    def hijo_izquierdo(self,indice): 
        return 2*indice+1
    
    # Devuelve la posición del hijo derecho del elemento almacenado en la 
    # posición indice del vector        
    def hijo_derecho(self,indice): 
        return 2*indice+2  
      
    # Devuelve True si el elemento almacenado en la posición indice es una 
    # hoja del árbol.  
    def es_hoja(self,indice): 
        return (self.__hijo_izquierdo(indice) >= self.tamano) and (self.__hijo_derecho(indice) >= self.tamano)
    
    # Devuelve True si el elemento almacenado en la posición indice tiene
    # solamente un hijo.
    
    def un_hijo(self,indice): 
        return (self.__hijo_izquierdo(indice) < self.tamano) and (self.__hijo_derecho(indice) >= self.tamano)
        
        
    # Con estas funciones se premite llamar al diccionario de prioridad como a cualquier
    # otra secuencia    
        
    # Devuelve el valor de un elemento
    # Si dp es un diccionario de prioridad, se puede utilizar 'dp[elemento]'
    def __getitem__(self,elemento):
        indice = self.diccionario[elemento]
        #print(self.diccionario," | ",indice," | ",elemento)
        return self.vector[indice][1]   
    
    # Devuelve True si el diccionario contiene el elemento.
    # Si dp es un diccionario de prioridad, se puede usar 'elemento in dp'
    def __contains__(self,elemento):  
        return elemento in self.diccionario   
    
    # Esta función permite actualizar directamente el valor de un elemento
    # Si dp es un diccionario de prioridad, se puede hacer 'dp[elemento]=valor'
    def __setitem__(self, elemento, valor):
        if elemento in self.diccionario:
            self.actualiza((elemento, valor))  
        else:
            self.inserta((elemento, valor))
        
    # Esta función permite actualizar directamente el valor de un elemento
    # Si dp es un diccionario de prioridad, se puede hacer 'del dp[elemento]'        
    def __delitem__(self,elemento):      
        self.borra(elemento)  

###########################################################################################
###########################################################################################                
                
# Esta función permite comprobar el funcionamiento del diccionario de prioridad.        
def test():
        L = [('A',6.5), ('B',4.3), ('C',3.7), ('D',5.8), ('E',9.1), ('F',7.2), ('G',7)]       
        # Creamos el diccionario de prioridad con la lista
        dp = dicPrioridad(L)
        #print(dp.vector, " | ",dp.diccionario)
        print(dp.extrae_min())
        #print(dp.vector, " | ",dp.diccionario)
        dp.inserta(('H', 1))
        print(dp['F'])
        #print(dp.vector, " | ",dp.diccionario)
        dp.actualiza(('F',3))
        print(dp['F'])
        #print(dp.vector, " | ",dp.diccionario)
        print('F' in dp)
        del dp['F']
        print('F' in dp)
        print(dp.extrae_min())
        #print(dp.vector, " | ",dp.diccionario)
        dp['X'] = 3.14
        print(dp['X'])
        #print(dp.vector, " | ",dp.diccionario)

#test()   
#exit()


# Algoritmo 2
# Esta función debe implementar el algoritmo de Dijkstra con diccionario de prioridad
#
def dijkstra2(origen,destino):

    S = set([]) # Nodos incluidos
    Q = set([]) # Nodos candidatos
    DP = dicPrioridad() # Distancia al origen, implementada como diccionario de prioridad
    P = {} # Camino

    edges = list(dist.keys())
    
    # Estas estructuras almacenan los resultados  
    nodosVisitados = set([])
    aristasVisitadas = set([])
    camino = []
    TiempoViaje = 0  # Distancia al origen

    for v in ciudades:
        DP.inserta((v,float('inf')))
    

    #print(DP.extrae_min())
    S.add(origen)
    ultimo = origen
    distanciaAnterior = 0

    while ultimo!=destino:
    # Extrae los nuevos candidatos
        busca = [v for (u,v) in edges if u==ultimo]

        for v in busca:
            if v not in S:
                Q.add(v)
                if distanciaAnterior + dist[ultimo,v] < DP[v]:
                    DP.actualiza((v,distanciaAnterior + dist[ultimo,v]))
                    P[v] = ultimo

        # Aquí ya ha salido del bucle
        # Busca el mejor candidato 
        # Esta acción es logarítmica en el tamaño de Q
        #
        # item = (ultimo,distancia)
        #


        item = DP.extrae_min()

        ultimo = item[0]
        distanciaAnterior = item[1]
        TiempoViaje = item[1]

        print(ultimo)

        Q.remove(ultimo)
        S.add(ultimo)
   
        nodosVisitados.add(ultimo)
        aristasVisitadas.add((P[ultimo],ultimo))
                    
    # Aquí ya ha salido del bucle
    # TiempoViaje se mantiene como la distancia al último
        
    # Recupera el camino
    d = destino
    o = P[d]
    camino.append((d,o))
    while o != origen:
        d = o
        o = P[d]
        camino.append((d,o))               
        
        # Devuelve la salida.
    return (TiempoViaje, Q | S,  aristasVisitadas, camino)   

#
# Mapa para la salida de Dijkstra 2
#

salida2 = folium.Map(location = [lat/tam, long/tam], zoom_start=6)
for i in capitales:
    folium.Marker(
        location=[capitales[i][0] , capitales[i][1]],
        #icon=folium.Icon(color = 'red'),
        icon=folium.DivIcon(html=f"""
            <div><svg>
                <rect x="0", y="0" width="5" height="5", fill="black", opacity=".5" />
            </svg></div>"""),
        popup=''
    ).add_to(salida2)



# Prueba
Origen = 'Albacete'
Destino = 'Vigo'

t=time()
Ans2 = dijkstra2(Origen, Destino)
t=time()-t

print('El tiempo de viaje es ', Ans2[0])
print('Número de nodos: ', len(Ans2[3]))
print('El tiempo de cómputo es ', t)
print('Aristas estudiadas: ', len(Ans2[2]))

# Dibujar una línea negra entre los puntos candidatos
folium.Marker(
    location=[ciudades[Origen][0] , ciudades[Origen][1]],
    #icon=folium.Icon(color = 'red'),
    icon=folium.DivIcon(html=f"""
        <div><svg>
            <rect x="0", y="0" width="10" height="10", fill="red", opacity=".8" />
        </svg></div>"""),
    popup=''
).add_to(salida2)
folium.Marker(
    location=[ciudades[Destino][0] , ciudades[Destino][1]],
    #icon=folium.Icon(color = 'red'),
    icon=folium.DivIcon(html=f"""
        <div><svg>
            <rect x="0", y="0" width="10" height="10", fill="red", opacity=".8" />
        </svg></div>"""),
    popup=''
).add_to(salida2)
    
for arista in Ans2[2]:
    linea = folium.PolyLine(locations=[ciudades[arista[0]], ciudades[arista[1]]],
                        color='black', weight=2, opacity=0.5).add_to(salida2)
for arista in Ans2[3]:
    linea = folium.PolyLine(locations=[ciudades[arista[0]], ciudades[arista[1]]],
                        color='red', weight=5, opacity=0.8).add_to(salida2)    
salida2
