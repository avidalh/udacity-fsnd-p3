#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Categories, Base, Items, Users


"""
populate.py
Project-3 main file
Udacity FSND

Insert some dummy user, categories and items into BD

"""

__author__ = "Angel Vidal"
__contact__ = "avidalh@gmail.com"
__date__ = "June 30, 2015"
__version__ = "0.1 Release Candidate"


engine = create_engine('postgresql:///catalog')
# engine = create_engine('sqlite:///catalog.sql')

# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()

session = DBSession()


def populate():
    # Create my user
    User1 = Users(
        name="Angel Vidal",
        email="avidalh@gmail.com",
        picture="https://lh3.googleusercontent.com/-KtpXNdMG81c/AAAAAAAAAAI/AAAAAAAABIo/EZzawwupWlc/photo.jpg")  # noqa

    session.add(User1)
    session.commit()

    # create Category 1
    economy = Categories(
        vehicle_type="Subcompact",
        description="Something that is smaller than the compact size \
        version of it, especially a very small car.",
        user_id=1)

    session.add(economy)
    session.commit()

    # create Category 2
    fullSize = Categories(
        vehicle_type="Compact",
        description="...",
        user_id=1)

    session.add(fullSize)
    session.commit()

    # create Category 3
    minivan = Categories(
        vehicle_type="Mid-size",
        description="...",
        # picture = "",
        user_id=1)

    session.add(minivan)
    session.commit()

    # create Category 4
    compact = Categories(
        vehicle_type="Full-size",
        description="...",
        # picture = "",
        user_id=1,
    )

    session.add(compact)
    session.commit()

    # create Category 5
    premium = Categories(
        vehicle_type="Premium",
        description="The Premium",
        # picture = "",
        user_id=1,
    )

    session.add(premium)
    session.commit()

    # create Category 6
    luxury = Categories(
        vehicle_type="Luxury",
        description="The Luxury",
        # picture = "",
        user_id=1,
    )

    session.add(luxury)
    session.commit()

    # create Category 7
    convertible = Categories(
        vehicle_type="Convertible",
        description="The Convertible",
        # picture = "",
        user_id=1,
    )

    session.add(convertible)
    session.commit()

# create Items:
    car1 = Items(
        make="Toyota",
        model="Corolla",
        description="A white one...",
        picture1="http://bestsellingcarsblog.com/wp-content/uploads/2012/05/Toyota-Corolla-Finland-1998.jpg",  # noqa
        picture2="http://i.ytimg.com/vi/2jo4jdFhasY/maxresdefault.jpg",  # noqa
        picture3="http://www.todoautos.com.pe/attachments/f50/370962d1283995716-vendo-toyota-corolla-1998-hatchback-imagen-019.jpg",  # noqa
        displacement="1300 cm3",
        engine="Petrol",
        cylinders="4",
        power="500HP",
        speed="250mph",
        seats="4",
        weight="1200Kgr",
        year="1999",
        price="$8000",
        category_id=1,
        user_id=1)

    session.add(car1)
    session.commit()

    car2 = Items(
        make="Renault",
        model="Megane",
        description="",
        picture1="http://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.png",  # noqa
        picture2="http://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.png",  # noqa
        picture3="http://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.png",  # noqa
        displacement="1300 cm3",
        engine="Petrol",
        cylinders="4",
        power="60KW",
        speed="100mph",
        seats="4",
        weight="1200Kgr",
        year="1989",
        price="$6000",
        category_id=1,
        user_id=1)

    session.add(car2)
    session.commit()

    car3 = Items(
        make="VolksWagen",
        model="Bettle",
        description="",
        picture1="http://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.png",  # noqa
        picture2="http://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.png",  # noqa
        picture3="http://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.png",  # noqa
        displacement="1300 cm3",
        engine="Petrol",
        cylinders="4",
        power="50hp",
        speed="80mph",
        seats="4",
        weight="1200Kgr",
        year="1980",
        price="$8750",
        category_id=1,
        user_id=1)

    session.add(car3)
    session.commit()

    car1 = Items(
        make="Mitsubishi",
        model="Space Wagon",
        description="The big one",
        picture1="http://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.png",  # noqa
        picture2="http://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.png",  # noqa
        picture3="http://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.png",  # noqa
        displacement="2400cm3",
        engine="Petrol",
        cylinders="4",
        power="147HP",
        speed="250mph",
        seats="7",
        weight="1850Kgr",
        year="2003",
        price="$24.000",
        category_id=2,
        user_id=1)

    session.add(car1)
    session.commit()

    car2 = Items(
        make="Renault",
        model="Space",
        description="",
        picture1="http://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.png",  # noqa
        picture2="http://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.png",  # noqa
        picture3="http://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.png",  # noqa
        displacement="1900cm3",
        engine="Diesel",
        cylinders="4",
        power="60KW",
        speed="100mph",
        seats="4",
        weight="1200Kgr",
        year="1989",
        price="$6000",
        category_id=2,
        user_id=1)

    session.add(car2)
    session.commit()

    car3 = Items(
        make="VolksWagen",
        model="Touran",
        description="",
        picture1="http://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.png",  # noqa
        picture2="http://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.png",  # noqa
        picture3="http://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.png",  # noqa
        displacement="1300 cm3",
        engine="Diesel",
        cylinders="4",
        power="50hp",
        speed="80mph",
        seats="4",
        weight="1200Kgr",
        year="1980",
        price="$8750",
        category_id=2,
        user_id=1)

    session.add(car3)
    session.commit()

    car1 = Items(
        make="Toyota",
        model="Land Cruiser",
        description="The big one...",
        picture1="http://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.png",  # noqa
        picture2="http://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.png",  # noqa
        picture3="http://plainicon.com/dboard/userprod/2825_96ae8/prod_thumb/plainicon.com-49509-w-128px-a052.png",  # noqa
        displacement="2500 cm3",
        engine="Diesel",
        cylinders="6",
        power="500HP",
        speed="250mph",
        seats="4",
        weight="2300Kgr",
        year="1999",
        price="$80000",
        category_id=3,
        user_id=1)

    session.add(car1)
    session.commit()

    car2 = Items(
        make="Toyota",
        model="Auris",
        description="The Toyota Auris is a compact hatchback derived from \
            the Toyota Corolla. Introduced in 2006, the first generation \
            shared the E150 platform with the Corolla, while the second \
            generation compact five-door hatchback and station wagon called \
            the Touring Sports uses the E180 platform. The name Auris is \
            based on the Latin word for gold, aurum.In Europe, Toyota \
            positioned the Auris as the replacement for the Corolla \
            hatchback, while the notchback sedan continued with the Corolla \
            nameplate. It was not sold in North America, as the larger \
            Toyota Matrix had taken its place in the lineup prior to its \
            discontinuation in 2014. For the first generation only, the more \
            luxurious Auris was named Toyota Blade in Japan. The Auris \
            succeeds the Toyota Allex in Japan and the Corolla RunX. Toyota \
            Australia and Toyota New Zealand resisted suggestions from Toyota \
            Japan to adopt the new European Auris name for the Corolla.",
        picture1="http://hybridcars2016.com/wp-content/uploads/2015-Toyota-Auris-Hybrid.jpg",  # noqa
        picture2="http://hybridcars2016.com/wp-content/uploads/2015-Toyota-Auris-Hybrid-interior.jpg",  # noqa
        picture3="http://hybridcars2016.com/wp-content/uploads/2015-Toyota-Auris-Hybrid-engine.jpg",  # noqa
        displacement="1900 cm3",
        engine="Hybrid",
        cylinders="4",
        power="120KW",
        speed="100mph",
        seats="4",
        weight="1200Kgr",
        year="2015",
        price="$25k",
        category_id=3,
        user_id=1)

    session.add(car2)
    session.commit()

    car3 = Items(
        make="VolksWagen",
        model="Tuareg",
        description="",
        picture1="http://media.caranddriver.com/images/14q2/584477/2015-volkswagen-touareg-photos-and-info-news-car-and-driver-photo-589412-s-429x262.jpg",  # noqa
        picture2="http://image.motortrend.ca/f/87234131/2015-Volkswagen-Touareg-TDI-inteiror.jpg",  # noqa
        picture3="http://www.gtspirit.com/wp-content/uploads/2014/09/gtspirit-2015-volkswagen-touareg28-640x426.jpg",  # noqa
        displacement="3300 cm3",
        engine="Petrol",
        cylinders="8",
        power="560hp",
        speed="80mph",
        seats="4",
        weight="2200Kgr",
        year="1980",
        price="$89.750",
        category_id=3,
        user_id=1)

    session.add(car3)
    session.commit()


# main fucntion
if __name__ == '__main__':
    populate()
