The dataset is the Titanic passenger list. 891 rows, 12 columns.

Command:
python3 analysis.py

Most surprising finding:

The gender gap was way larger than i expected. 74% of women survived vs only 19% of men. I knew the "women and children first" rule existed but seeing it in actual numbers made it feel real. Even in 3rd class where conditions were worst, 50% of women survived compared to only 13.5% of men in the same class.

The other thing that surprised me was how much data was missing for Cabin. When you drop rows with no cabin info you go from 891 rows down to 204. That means 77% of passengers had no cabin recorded at all. It makes me wonder if cabin data was only recorded for 1st class passengers, because 1st class had the highest survival rate and Cherbourg (which also had a high survival rate) was mostly wealthy passengers boarding there.

What i would investigate next:

I would look at whether having a cabin number recorded correlates with survival independent of class. If cabin data exists only for wealthier passengers then the cabin column might just be a proxy for class and wealth. I would also look at family size using SibSp and Parch columns to see if traveling alone vs with family changed your odds of surviving.
