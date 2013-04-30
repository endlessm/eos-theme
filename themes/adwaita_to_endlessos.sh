#!/bin/bash
# Run this to rename the Adwaita theming engine to EndlessOS

for x in `find EndlessOS -name "*adwaita*"`
do
    y="${x/adwaita/endlessos}"
    git mv $x $y
done

for x in `grep -rl adwaita EndlessOS`
do
    sed -i s/adwaita/endlessos/g $x
done

for x in `grep -rl Adwaita EndlessOS`
do
    sed -i s/Adwaita/EndlessOS/g $x
done

for x in `grep -rl ADWAITA EndlessOS`
do
    sed -i s/ADWAITA/ENDLESSOS/g $x
done
