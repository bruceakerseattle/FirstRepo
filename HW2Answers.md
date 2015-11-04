##Class 2 Homework: Command Line Chipotle

1.) Used commands head -n 20 chipotle.tsv, tail -n 20 chipotle.tsv to look at a sample of the data - each row seems to be a line-item from an order at chipotle,
      each column is an attribute of the line-item.<br>
2.) 1834 by looking at last line from tail chipotle.tsv<br>
3.) 4623 from grep -c . chipotle.tsv<br>
4.) Chicken from grep -c "Chicken Burrito" chipotle.tsv and grep -c "Steak Burrito" chipotle.tsv<br>
5.) Black Beans from grep -c "Chicken Burrito.\*Black Beans" chipotle.tsv, grep -c "Chicken Burrito.\*Pinto Beans" chipotle.tsv<br>
6.) ls *.[ct]sv
airlines.csv         bikeshare.csv  drinks.csv   imdb_1000.csv  titanic.csv  vehicles_test.csv   yelp.csv
bank-additional.csv  chipotle.tsv   hitters.csv  sms.tsv        ufo.csv      vehicles_train.csv<br>
7.) 48 using grep -cir dictionary * and adding up the numbers<br>
8.) 