SQLite format 3   @           
                                                        -�                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            � �                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      ~ #/�EAngel Vidalavidalh@gmail.comhttps://lh3.googleusercontent.com/-KtpXNdMG81c/AAAAAAAAAAI/AAAAAAAABIo/EZzawwupWlc/photo.jpg    ��p]D-                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       	#+ConvertibleThe Convertible 	!LuxuryThe Luxury 	#PremiumThe Premium 	Full-size... 	Mid-size... 	Compact...k 	!�CSubcompactSomething that is smaller than the compact size version of it, especially a very small car.   �    ����                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           	                ��   �+�5tableusersusersCREATE TABLE users (
	id INTEGER NOT NULL, 
	name VARCHAR(250) NOT NULL, 
	email VARCHAR(250) NOT NULL, 
	picture VARCHAR(250), 
	PRIMARY KEY (id)
)�h!!�tablecategoriescategoriesCREATE TABLE categories (
	id INTEGER NOT NULL, 
	user_id INTEGER, 
	vehicle_type VARCHAR(250) NOT NULL, 
	description VARCHAR(500), 
	PRIMARY KEY (id), 
	FOREIGN KEY(user_id) REFERENCES users (id)
)�S�tableitemsitemsCREATE TABLE items (
	id INTEGER NOT NULL, 
	category_id INTEGER, 
	user_id INTEGER, 
	make VARCHAR(250) NOT NULL, 
	model VARCHAR(250) NOT NULL, 
	description VARCHAR(2000), 
	picture1 VARCHAR(250), 
	picture2 VARCHAR(250), 
	picture3 VARCHAR(250), 
	displacement VARCHAR(20), 
	engine VARCHAR(50), 
	cylinders VARCHAR(20), 
	power VARCHAR(20), 
	speed VARCHAR(20), 
	seats VARCHAR(20), 
	weight VARCHAR(20), 
	year VARCHAR(20), 
	price VARCHAR(20), 
	PRIMARY KEY (id), 
	FOREIGN KEY(category_id) REFERENCES categories (id), 
	FOREIGN KEY(user_id) REFERENCES users (id)
)   9 �9                                                                                                                                                                                                                                                                                                             �j 		�K�K�KRenaultMeganehttp://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.pnghttp://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.pnghttp://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.png1300 cm3Petrol460KW100mph41200Kgr1989$6000�W 		)�?s�mToyotaCorollaA white one...http://bestsellingcarsblog.com/wp-content/uploads/2012/05/Toyota-Corolla-Finland-1998.jpghttp://i.ytimg.com/vi/2jo4jdFhasY/maxresdefault.jpghttp://www.todoautos.com.pe/attachments/f50/370962d1283995716-vendo-toyota-corolla-1998-hatchback-imagen-019.jpg1300 cm3Petrol4500HP250mph41200Kgr1999$8000    �                                                                                                                                                                                                                                                                  �  	!##�K�K�KMitsubishiSpace WagonThe big onehttp://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.pnghttp://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.pnghttp://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.png2400cm3Petrol4147HP250mph71850Kgr2003$24.000�l 		!�K�K�KVolksWagenBettlehttp://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.pnghttp://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.pnghttp://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.png1300 cm3Petrol450hp80mph41200Kgr1980$8750   $ �$                                                                                                                                                                                                                                                                                        �m 	!�K�K�KVolksWagenTouranhttp://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.pnghttp://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.pnghttp://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.png1300 cm3Diesel450hp80mph41200Kgr1980$8750�i 	�K�K�KRenaultSpacehttp://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.pnghttp://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.pnghttp://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.png1900cm3Diesel460KW100mph41200Kgr1989$6000   E }E                                                                                                                                                                                                                                                                                                                         �- 	�y��1�-ToyotaAurisThe Toyota Auris is a compact hatchback derived from         the Toyota Corolla. Introduced in 2006, the first generation shared         the E150 platform with the Corolla, while the second generation         compact five-door hatchback and station wagon called the Tour   �  	%)�K�K�KToyotaLand CruiserThe big one...http://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.pnghttp://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.pnghttp://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.png2500 cm3Diesel6500HP250mph42300Kgr1999$80000                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   ) t)                                                                                                                                                                                                                                                                                             �H
 	#7��/�!1PrimitiveFlintstonesThe Flintstones car
http://img.timeinc.net/time/photoessays/2008/10_cars/flintstones.jpghttp://www.gadgetshowprizes.co.uk/wp-content/uploads/2014/07/The-Flintstones1.jpghttps://therandomtexan.files.wordpress.com/2013/10/the-flintstones-car.jpgN/APure carbohydrates82HP2mph2+2101960N/A�		 	!��)�OVolksWagenTuareghttp://media.caranddriver.com/images/14q2/584477/2015-volkswagen-touareg-photos-and-info-news-car-and-driver-photo-589412-s-429x262.jpghttp://image.motortrend.ca/f/87234131/2015-Volkswagen-Touareg-TDI-inteiror.jpghttp://www.gtspirit.com/wp-content/uploads/2014/09/gtspirit-2015-volkswagen-touareg28-640x426.jpg3300 cm3Petrol8560hp80mph42200Kgr1980$89.750    ing         Sports uses the E180 platform. The name Auris is based on the Latin         word for gold, aurum.In Europe, Toyota positioned the Auris as the         replacement for the Corolla hatchback, while the notchback sedan         continued with the Corolla nameplate. It was not sold in North         America, as the larger Toyota Matrix had taken its place in the lineup         prior to its discontinuation in 2014. For the first generation only,         the more luxurious Auris was named Toyota Blade in Japan. The Auris         succeeds the Toyota Allex in Japan and the Corolla RunX. Toyota         Australia and Toyota New Zealand resisted suggestions from Toyota         Japan to adopt the new European Auris name for the Corolla.http://hybridcars2016.com/wp-content/uploads/2015-Toyota-Auris-Hybrid.jpghttp://hybridcars2016.com/wp-content/uploads/2015-Toyota-Auris-Hybrid-interior.jpghttp://hybridcars2016.com/wp-content/uploads/2015-Toyota-Auris-Hybrid-engine.jpg1900Hybrid4120KW100mph41200Kgr2015$25.000