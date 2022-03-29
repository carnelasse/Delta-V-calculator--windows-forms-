# This is a windows forms delta V and orbital velocity calculator

![Orbital mechanics calculator 10 03 2022 13_30_47](https://user-images.githubusercontent.com/57408600/160673920-4c2825aa-8aca-42e5-b1a6-38536d08412d.png)
![Orbital mechanics calculator 10 03 2022 13_33_03](https://user-images.githubusercontent.com/57408600/160673905-933a3681-bcba-410d-8962-ec7c73d0cfdf.png)
![Orbital mechanics calculator 10 03 2022 13_32_48](https://user-images.githubusercontent.com/57408600/160673915-7fb88e6d-48bb-4dec-85ac-c9e41b3ea8e9.png)

## Cheat sheet
- Peryapse - point in orbit closest to the center of mass of primary body.
- Apoapse - point in orbit most distanced from the center of mass of primary body.
- Calculation radius - point in orbit where you want to make a calculation of orbital velocity. Can't be lower than peryapse, can't be higher than apoapse.
- Final radius - in delta v calculation is new peryapse or apoapse after injection.
- Injection into circular orbit - delta v required to turn elliptical orbit into circular.

## Modes
- Orbital velocity
- Delta V

## Selecting primary body
User can chose celestial body being orbited in calculations.

Currently app supports:
- Earth
- Moon
- Sun

## Input variables
- Peryapse
- Apoapse
- Final orbit (for delta V only)
- Calculation orbit (for orbital velocity only)


User inputs apoapse and peryapse of orbit and chooses mode - orbital velocity or delta v - primary body - Earth, Moon or Sun.

Pressing 'calculate' will display either orbital velocity of object on chosen orbit or delta v and injection into circular orbit.

Calculating even if orbit is below 0. Not a bug it's a feature.
