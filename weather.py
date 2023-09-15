import requests
import json

Api = 'a91c1752c84fea7efe626fcf268f2313'
inCity = input('Введите город: ')
json.data = 0
# ссылка на АПИ, которая возвращает json ответ, который мы можем распарсить (почитай про F-строки, одна из самых полезных и частых вещей)
weather = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={inCity}&appid={Api}')
# с помощью встроенной библиотеки парсим этот json в python-структуру
json_data = weather.json()
# достаём из json долготу и широту (если посмотрим на структуру этого json, то увидишь что там есть словари (и мб списки)\
# тут значит, что в json, который мы получили, идём по ключу "coord", а затем по ключу "lat", где получаем какое-то значение
# это как "сначала идём в А, когда мы зашли в А, мы видим Б В Г и т.д, но нам нужно только Б, мы идём в Б, заходимв Б и видим там нужное нам значение
lat = json_data['coord']['lat']
lon = json_data['coord']['lon']
# тут это другой запрос (взятый из документации которую я тебе кинул), подставляешь долготу и широту города, он также возвращает тебе какую-то инфу
city = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={Api}&units=metric')
json_city = city.json()
print(f"Температура в городе {inCity}: ", str(json_city['main']['temp']) + "C°")



# maxim_dict = {
#     "Key1": "Value1",
#     "Key2": {
#         "key3": 'val3'
#     }
# }
#
# maxim_dict["key4"] = [1, 2, 3]
# print(maxim_dict['Key2']["key3"])


maxim_dict = {
    "Key1": "Value1",
    "Key2": True
}
# test = [
# 	{
# 		"_id": "64fb3ba356efb221503c0afc",
# 		"index": 0,
# 		"guid": "a2399454-2713-4752-80d9-6d96a9ca626d",
# 		"isActive": True,
# 		"balance": "$1,620.90",
# 		"picture": "http://placehold.it/32x32",
# 		"age": 23,
# 		"eyeColor": "brown",
# 		"name": "Julia Blair",
# 		"gender": "female",
# 		"company": "SHEPARD",
# 		"email": "juliablair@shepard.com",
# 		"phone": "+1 (938) 429-2068",
# 		"address": "479 Prescott Place, Smeltertown, Palau, 2908",
# 		"about": "Esse mollit labore officia eu deserunt enim id. Enim et nulla non nulla deserunt fugiat irure fugiat. Anim ex reprehenderit veniam cillum commodo mollit commodo adipisicing ad fugiat. Veniam do pariatur ea ullamco id anim consequat ut. Sunt irure cillum fugiat ea fugiat incididunt irure. Aliquip sint minim do nisi ad dolore ut anim laborum qui sint aliqua. Nostrud non nisi id laborum Lorem sint duis mollit dolor do.\r\n",
# 		"registered": "2018-07-01T01:11:58 -03:00",
# 		"latitude": -56.195188,
# 		"longitude": 118.731891,
# 		"tags": [
# 			"tempor",
# 			"culpa",
# 			"in",
# 			"voluptate",
# 			"veniam",
# 			"qui",
# 			"magna"
# 		],
# 		"friends": [
# 			{
# 				"id": 0,
# 				"name": "Stanton Battle"
# 			},
# 			{
# 				"id": 1,
# 				"name": "Pennington Hebert"
# 			},
# 			{
# 				"id": 2,
# 				"name": "Ramona Dunn"
# 			}
# 		],
# 		"greeting": "Hello, Julia Blair! You have 4 unread messages.",
# 		"favoriteFruit": "apple"
# 	},
# 	{
# 		"_id": "64fb3ba36e94e2a26099470e",
# 		"index": 1,
# 		"guid": "de10efd0-e1db-4e97-84e7-f6fd6e228fe2",
# 		"isActive": False,
# 		"balance": "$3,229.04",
# 		"picture": "http://placehold.it/32x32",
# 		"age": 36,
# 		"eyeColor": "green",
# 		"name": "Jenny Cannon",
# 		"gender": "female",
# 		"company": "GEEKWAGON",
# 		"email": "jennycannon@geekwagon.com",
# 		"phone": "+1 (900) 506-3080",
# 		"address": "205 Denton Place, Orason, Kansas, 4979",
# 		"about": "Excepteur pariatur ex ut voluptate ad officia aute. Cupidatat amet sit nisi velit. Et duis irure cillum Lorem est ad nostrud magna mollit esse commodo. Irure tempor nulla mollit minim velit ipsum excepteur dolor duis. Irure qui amet laboris mollit cupidatat. Elit qui pariatur sint sunt et commodo irure.\r\n",
# 		"registered": "2017-01-31T01:19:08 -03:00",
# 		"latitude": -36.831052,
# 		"longitude": 85.128664,
# 		"tags": [
# 			"cillum",
# 			"laborum",
# 			"proident",
# 			"consequat",
# 			"laborum",
# 			"veniam",
# 			"cillum"
# 		],
# 		"friends": [
# 			{
# 				"id": 0,
# 				"name": "Rhea Hubbard"
# 			},
# 			{
# 				"id": 1,
# 				"name": "Francisca Oliver"
# 			},
# 			{
# 				"id": 2,
# 				"name": "Julianne Carrillo"
# 			}
# 		],
# 		"greeting": "Hello, Jenny Cannon! You have 2 unread messages.",
# 		"favoriteFruit": "banana"
# 	},
# 	{
# 		"_id": "64fb3ba3f2bb85d498601a21",
# 		"index": 2,
# 		"guid": "84cfb4b9-045f-429b-a5a6-c2fa9ae06998",
# 		"isActive": False,
# 		"balance": "$2,888.14",
# 		"picture": "http://placehold.it/32x32",
# 		"age": 21,
# 		"eyeColor": "green",
# 		"name": "Rollins Potts",
# 		"gender": "male",
# 		"company": "ZAGGLES",
# 		"email": "rollinspotts@zaggles.com",
# 		"phone": "+1 (935) 516-2116",
# 		"address": "442 Johnson Avenue, Darrtown, Oregon, 9191",
# 		"about": "Dolore officia enim nostrud mollit velit incididunt aute esse cupidatat excepteur. Fugiat velit sit in duis. Nostrud commodo ex est cillum.\r\n",
# 		"registered": "2023-08-13T05:53:55 -03:00",
# 		"latitude": -81.91604,
# 		"longitude": -13.683279,
# 		"tags": [
# 			"amet",
# 			"dolor",
# 			"in",
# 			"deserunt",
# 			"in",
# 			"eu",
# 			"quis"
# 		],
# 		"friends": [
# 			{
# 				"id": 0,
# 				"name": "Naomi Travis"
# 			},
# 			{
# 				"id": 1,
# 				"name": "Thompson Vega"
# 			},
# 			{
# 				"id": 2,
# 				"name": "Sellers Pope"
# 			}
# 		],
# 		"greeting": "Hello, Rollins Potts! You have 2 unread messages.",
# 		"favoriteFruit": "apple"
# 	},
# 	{
# 		"_id": "64fb3ba3f385b16abb37c9af",
# 		"index": 3,
# 		"guid": "2aba602b-8318-42f1-b561-a8c807fe8fb6",
# 		"isActive": True,
# 		"balance": "$3,290.45",
# 		"picture": "http://placehold.it/32x32",
# 		"age": 22,
# 		"eyeColor": "brown",
# 		"name": "Laurie Strong",
# 		"gender": "female",
# 		"company": "KAGE",
# 		"email": "lauriestrong@kage.com",
# 		"phone": "+1 (945) 418-3040",
# 		"address": "242 Garfield Place, Waterloo, New Mexico, 1440",
# 		"about": "Irure excepteur occaecat sint exercitation aliquip incididunt sit magna exercitation consequat excepteur sit nisi. Minim mollit velit pariatur elit dolor mollit reprehenderit anim eu ipsum. Minim aliqua et in esse sunt cillum labore ipsum adipisicing ullamco occaecat consectetur do dolore. Adipisicing magna adipisicing consequat ipsum consequat cillum. Quis deserunt id qui officia consectetur adipisicing laboris id. Magna cupidatat esse velit voluptate anim voluptate est dolor do magna. Commodo elit exercitation adipisicing reprehenderit ullamco sit cupidatat fugiat velit proident eu qui enim sint.\r\n",
# 		"registered": "2015-07-08T11:57:23 -03:00",
# 		"latitude": 85.131771,
# 		"longitude": -168.64641,
# 		"tags": [
# 			"enim",
# 			"amet",
# 			"mollit",
# 			"velit",
# 			"incididunt",
# 			"occaecat",
# 			"commodo"
# 		],
# 		"friends": [
# 			{
# 				"id": 0,
# 				"name": "Aline Blevins"
# 			},
# 			{
# 				"id": 1,
# 				"name": "Estella Rosales"
# 			},
# 			{
# 				"id": 2,
# 				"name": "Gloria Bauer"
# 			}
# 		],
# 		"greeting": "Hello, Laurie Strong! You have 8 unread messages.",
# 		"favoriteFruit": "strawberry"
# 	},
# 	{
# 		"_id": "64fb3ba34e728908bb349bd8",
# 		"index": 4,
# 		"guid": "8f835a4f-27ab-47ba-bfee-a46ba9f2a62f",
# 		"isActive": False,
# 		"balance": "$3,207.45",
# 		"picture": "http://placehold.it/32x32",
# 		"age": 31,
# 		"eyeColor": "blue",
# 		"name": "Brittany Riddle",
# 		"gender": "female",
# 		"company": "VENDBLEND",
# 		"email": "brittanyriddle@vendblend.com",
# 		"phone": "+1 (943) 542-3144",
# 		"address": "503 School Lane, Bourg, Oklahoma, 2032",
# 		"about": "Cillum ut excepteur sunt eiusmod mollit. Commodo aliqua ex aute pariatur culpa mollit adipisicing magna enim do non duis sint adipisicing. Eu occaecat ullamco elit cillum Lorem do laborum. Consectetur aliqua dolore reprehenderit duis quis non. Veniam eu aute reprehenderit quis mollit non do consequat esse laboris id excepteur voluptate.\r\n",
# 		"registered": "2019-01-18T11:35:34 -03:00",
# 		"latitude": -79.403077,
# 		"longitude": -93.186778,
# 		"tags": [
# 			"adipisicing",
# 			"voluptate",
# 			"do",
# 			"proident",
# 			"excepteur",
# 			"aliquip",
# 			"cillum"
# 		],
# 		"friends": [
# 			{
# 				"id": 0,
# 				"name": "Brenda Burris"
# 			},
# 			{
# 				"id": 1,
# 				"name": "Susanna Giles"
# 			},
# 			{
# 				"id": 2,
# 				"name": "Carver Robertson"
# 			}
# 		],
# 		"greeting": "Hello, Brittany Riddle! You have 2 unread messages.",
# 		"favoriteFruit": "banana"
# 	},
# 	{
# 		"_id": "64fb3ba3ada1ece83bbc5605",
# 		"index": 5,
# 		"guid": "5f5334a0-4672-4f8c-ad01-1e2dba3c706a",
# 		"isActive": False,
# 		"balance": "$1,935.94",
# 		"picture": "http://placehold.it/32x32",
# 		"age": 28,
# 		"eyeColor": "green",
# 		"name": "Barbara Barrett",
# 		"gender": "female",
# 		"company": "FURNITECH",
# 		"email": "barbarabarrett@furnitech.com",
# 		"phone": "+1 (983) 486-3182",
# 		"address": "864 Doscher Street, Cutter, South Carolina, 2089",
# 		"about": "Exercitation laborum consequat proident minim magna minim aliquip tempor ullamco reprehenderit cupidatat ullamco. Occaecat cupidatat Lorem magna minim nostrud. Eiusmod voluptate incididunt duis ut nisi velit irure sit. Sunt pariatur nulla in ex culpa est laboris do eiusmod consequat officia eu culpa amet.\r\n",
# 		"registered": "2021-02-18T08:21:03 -03:00",
# 		"latitude": 86.332784,
# 		"longitude": 21.804633,
# 		"tags": [
# 			"aliquip",
# 			"eiusmod",
# 			"officia",
# 			"ipsum",
# 			"amet",
# 			"elit",
# 			"ullamco"
# 		],
# 		"friends": [
# 			{
# 				"id": 0,
# 				"name": "Hoover Harrell"
# 			},
# 			{
# 				"id": 1,
# 				"name": "Cathleen Reynolds"
# 			},
# 			{
# 				"id": 2,
# 				"name": "Blake Holman"
# 			}
# 		],
# 		"greeting": "Hello, Barbara Barrett! You have 4 unread messages.",
# 		"favoriteFruit": "strawberry"
# 	},
# 	{
# 		"_id": "64fb3ba35e3a86c4219a5b59",
# 		"index": 6,
# 		"guid": "8764c181-bbff-453c-a4ab-d64b8144aeb0",
# 		"isActive": True,
# 		"balance": "$2,790.32",
# 		"picture": "http://placehold.it/32x32",
# 		"age": 20,
# 		"eyeColor": "blue",
# 		"name": "Nora Goodman",
# 		"gender": "female",
# 		"company": "LUNCHPAD",
# 		"email": "noragoodman@lunchpad.com",
# 		"phone": "+1 (933) 577-2036",
# 		"address": "451 Navy Walk, Soham, New Hampshire, 7918",
# 		"about": "Tempor dolor aliqua nisi dolor ipsum elit ex minim cillum. Aute commodo esse culpa est labore anim ipsum mollit ullamco. Consectetur esse velit elit ea mollit dolor mollit. Officia sit minim ullamco nisi enim qui duis laborum eu excepteur aliqua.\r\n",
# 		"registered": "2023-05-20T10:09:13 -03:00",
# 		"latitude": -28.309909,
# 		"longitude": 76.642517,
# 		"tags": [
# 			"minim",
# 			"velit",
# 			"adipisicing",
# 			"excepteur",
# 			"laborum",
# 			"voluptate",
# 			"Lorem"
# 		],
# 		"friends": [
# 			{
# 				"id": 0,
# 				"name": "Deanna Wells"
# 			},
# 			{
# 				"id": 1,
# 				"name": "Gilmore Luna"
# 			},
# 			{
# 				"id": 2,
# 				"name": "Susie Wade"
# 			}
# 		],
# 		"greeting": "Hello, Nora Goodman! You have 3 unread messages.",
# 		"favoriteFruit": "strawberry"
# 	}
# ]

# print()

# maxim_list = [maxim_dict, maxim_dict, maxim_dict]
#
# for i in maxim_list:
#     if i == 2:
#         print(i, maxim_list.index(i))



max_list = [{"key": "val1"}, [0,2,4,2,2,2,2,2,2,2,22,], 41, "str", {"key": "val2"}]

# dict = {
#
# 	1: [],
# 	"str": {}
# }

for var1 in max_list:
	if isinstance(var1, dict):
		print("is dict")
	elif isinstance(var1, list):
		print("is list")
	elif isinstance(var1, int):
		print("is int")
	else:
		print(type(var1))

print()
