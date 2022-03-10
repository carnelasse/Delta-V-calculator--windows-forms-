# Delta V/ orbital velocity calculator (windows forms)

![Orbital mechanics calculator 10 03 2022 13_32_48](https://user-images.githubusercontent.com/57408600/157662650-0ac71f4f-557a-4ec0-89f8-fbb183840ef5.png) ![Orbital mechanics calculator 10 03 2022 13_32_54](https://user-images.githubusercontent.com/57408600/157662671-fe0e555b-a08b-4c12-89ae-efc5da35b10f.png) ![Orbital mechanics calculator 10 03 2022 13_33_03](https://user-images.githubusercontent.com/57408600/157662687-1c76285d-ea1b-459d-a4df-fe62963f2964.png)

### Cheat sheet:
- peryapse - point in orbit closest to the primary body.
- apoapse - point in orbit most distanced from the primary body.
- calculation radius - point in orbit where you want to make a calculation of orbital velocity. Can't be lower than peryapse, can't be higher than apoapse.
- final radius - in delta v calculation is new peryapse or apoapse after injection.
- injection into circular orbit - delta v required to turn elliptical orbit into circular (second injection).

### Modes:
- orbital velocity - velocity of orbiting body relative to primary body
- delta v - change in velocity required to reach desired orbit

### Primary bodies:
- Earth
- Moon
- Sun

## Orbital velocity
User inputs peryapse, apoapse and calculation radius which is distance from primary body that must be within peryapse-apoapse range. User will be notified with error message when input is incorrect.

## Delta V
User inputs peryapse, apoapse and final radius which is desired peryapse or apoapse of final orbit. Next program calculates injection into circular orbit which is delta v required to make the orbit circular.

Calculating even if orbit is below 0. Not a bug it's a feature.
