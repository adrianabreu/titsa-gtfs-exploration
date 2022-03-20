# TITSA GTFS - Exploration


## Context

During my college I used a lot the bus service and it bothered me a lot how close were the two next bus stop, they were extremely close. After investigating a bit I discovered that [TITSA](https://titsa.com/index.php/tus-guaguas/38-titsa/titsa-open-data) post they google data on the open.

It took me a bit to understand the GTFS but [the official docs](https://developers.google.com/transit/gtfs/reference#field_definitions) are quite good.

## Requirements

The code attached is a notebook developed on top [docker stack](https://jupyter-docker-stacks.readthedocs.io/en/latest/) using Spark 3.2 (but most functions are retrocompat)

Also there is a *docker-composer* file containing the image and the volume mounted (the password for jupyter is _my-password_)

## Questions

### What are the closest bus stops in a single trip?

Both stops could be close to each other but some may be for specific lines, so using stop_times you can get the trip stop sequence and join it with the stop master data for the coords.

For calculating the distance I used the [harvesine distance](https://en.wikipedia.org/wiki/Haversine_formula) (kudos to [https://stackoverflow.com/questions/38994903/how-to-sum-distances-between-data-points-in-a-dataset-using-pyspark]) and compare each consecutive stop. 

There were some errores reporting the same stop for the same trip those were discarded... And well, I could found the same name in two similars id's  and they were a few degrees deviated one from another, as in the following img:

![](/imgs/same_name.png)

So I discarded also the same name as this is not really clear.
And well I ended up with two pretty similar bus stops that were both the same place but included the (T) from terminal.

So after discarded that error I found...

![](/imgs/palmar.png)

Which was hilarious, the difference between both is about 20 meters and it takes much more in the bus.

In case you're instered: the bus stops I was referring to were ranked as: 157.

More questions will be solved soon :) 