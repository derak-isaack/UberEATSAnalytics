## <div style="padding: 35px;color:white;margin:10;font-size:200%;text-align:center;display:fill;border-radius:10px;overflow:hidden;background-image: url(https://images.pexels.com/photos/7078619/pexels-photo-7078619.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1)"><b><span style='color:black'><strong> UBER-EATS RESTAURANTS BIG DATA MENU PRICE ANALYSIS </strong></span></b> </div> 

![Duckdb](https://img.shields.io/badge/DuckDB-FFF000?logo=duckdb&logoColor=000&style=for-the-badge)
![sql](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=fff&style=for-the-badge)
![UberEats](https://img.shields.io/badge/Uber%20Eats-06C167?logo=ubereats&logoColor=fff&style=for-the-badge)
![parquet](https://img.shields.io/badge/Apache%20Parquet-50ABF1?logo=apacheparquet&logoColor=fff&style=for-the-badge)
![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?logo=kaggle&logoColor=fff&style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=for-the-badge)

### <div style="padding: 20px;color:white;margin:10;font-size:90%;text-align:left;display:fill;border-radius:10px;overflow:hidden;background-image: url(https://w0.peakpx.com/wallpaper/957/661/HD-wallpaper-white-marble-white-stone-texture-marble-stone-background-white-stone.jpg)"><b><span style='color:black'> Project Overview</span></b> </div>

`Big data analytics` for delivery companies is always very necessary to uncover customer trends and patterns. Trends help these companies in optimizing their services to ensure a smooth flow of operations between riders as well as forecast future demand of various products and services. 

This project aimed to analyze the menus of various restaurants that use `uber-eats courier` as their supply company. As this is big data, the use of `OLAP-DATABASES` comes in handy to perfrom heavy analytics using `SQL`. These databases offer:

* `Scalability`: Can easily manage massive amounts of data efficiently.
* `Low latency`: Optimized for complex analytical queries due to their latency structure and optimized data structures and indexing. 
* `Batch processing`: Good for `large-scale` data processing tasks efficiently.

`Uber-Eats` customers also have the right to investigate the prices of various items on the menu to find the cheapest and most expensive restaurants to save on expenditure. The data was sourced from `kaggle` and can be accessed by using the following ![link](https://www.kaggle.com/datasets/ahmedshahriarsakib/uber-eats-usa-restaurants-menus)

### <div style="padding: 20px;color:white;margin:10;font-size:90%;text-align:left;display:fill;border-radius:10px;overflow:hidden;background-image: url(https://w0.peakpx.com/wallpaper/957/661/HD-wallpaper-white-marble-white-stone-texture-marble-stone-background-white-stone.jpg)"><b><span style='color:black'> Objectives</span></b> </div>

1. Investigate the `number of restaurants` that use `UBER-EATS`.
2. Investigate the `top restaurants with the largest number of items.`
3. Investigate the `price range of items` for the restaurant with the highest number of items.
4. Investigate the `average price of items` across various restaurants
5. Investigate the `most expensive restaurant.`
6. `Snacks items` analysis. Analyze the price of snack items across various restaurants. 

### <div style="padding: 20px;color:white;margin:10;font-size:90%;text-align:left;display:fill;border-radius:10px;overflow:hidden;background-image: url(https://w0.peakpx.com/wallpaper/957/661/HD-wallpaper-white-marble-white-stone-texture-marble-stone-background-white-stone.jpg)"><b><span style='color:black'> Findings</span></b> </div>

![avg-price](images/avg_price.png)
![snacks](images/snacks_prices.png)
![prices](images/Items_prices.png)

### <div style="padding: 20px;color:white;margin:10;font-size:90%;text-align:left;display:fill;border-radius:10px;overflow:hidden;background-image: url(https://w0.peakpx.com/wallpaper/957/661/HD-wallpaper-white-marble-white-stone-texture-marble-stone-background-white-stone.jpg)"><b><span style='color:black'> Future steps</span></b> </div>

1. Investigate the correlation between location i.e `latitude` & `longitude` and `menu-prices`. 
2. Outsource data for `customer orders` and analyze `consumer purchasing trends`.

All the requirements to run this project are listed in the file [requirements-file](requirements.txt) together with the library versions. 
