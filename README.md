# Delta V/ orbital velocity calculator (windows forms)

![image](https://user-images.githubusercontent.com/57408600/157662293-f8b81f5c-9998-4bd4-8e96-0cbd5644392a.png)

![Orbital mechanics calculator 10 03 2022 13_32_48](https://user-images.githubusercontent.com/57408600/157662650-0ac71f4f-557a-4ec0-89f8-fbb183840ef5.png)

![Orbital mechanics calculator 10 03 2022 13_32_54](https://user-images.githubusercontent.com/57408600/157662671-fe0e555b-a08b-4c12-89ae-efc5da35b10f.png) ![Orbital mechanics calculator 10 03 2022 13_33_03](https://user-images.githubusercontent.com/57408600/157662687-1c76285d-ea1b-459d-a4df-fe62963f2964.png)



This is a windows forms delta V and orbital velocity calculator
User inputs apoapse and peryapse of orbit and chooses mode - orbital velocity or delta v - primary body - Earth, Moon or Sun.
Peryapse - point in orbit most distanced from the center of mass of primary body.
Apoapse - point in orbit closest to the center of mass of primary body.
Calculation radius - point in orbit where you want to make a calculation of orbital velocity. Can't be lower than peryapse, can't be higher than apoapse.
Final radius - in delta v calculation is new peryapse or apoapse after injection.
Injection into circular orbit - delta v required to turn elliptical orbit into circular.
Pressing calculate will display either orbital velocity of object on chosen orbit or delta v and injection into circular orbit.

Calculating even if orbit is below 0. Not a bug it's a feature.
