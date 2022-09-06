Welcome to the homepage of this project.

Functionality as of now (06-SEP-2022):
1. Can scrape successfully Ozone.bg, section with unpacked products.
2. Added a mysql database, hosted locally. This DB is fed the scrapped data.
3. Optional functionality exists to save the scrapped data into an excel file - only need to uncomment the commented parts of the code.

Future functionality to be added (More will follow on this):
1. A GUI that provides a user with the opportunity to add more rows to the db, and scrape more websites
2. Option to generate a dashboard from the price data in the SQL table.

Technologies used:
1. MySQL
2. BeautifulSoup
3. openpyxl



Description of the database:
![image](https://user-images.githubusercontent.com/96660814/188721315-092f8cb5-7ecb-438b-9681-5112df036659.png)



This is an image of the database holding the scrapped data. The ID column in the primary key and it is set to auto_increment.
![image](https://user-images.githubusercontent.com/96660814/188720847-291856f3-dc18-44ff-a816-092eb618c644.png)


