from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    balance: int


@dataclass
class Point:
    x: int
    y: int


point1 = Point(5, 7)
point2 = Point(-10, 12)
print(point1)
print(point2)


@dataclass
class Location:
    name: str
    longitude: float = 0
    latitude: float = 11.5


stonehenge = Location('Stonehenge', 51, 1.5)