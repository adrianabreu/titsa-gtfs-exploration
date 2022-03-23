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

### Which stops have the most lines?

Obviously there are some bus stations but they should share id or at least name. 

|stop_id|stop_name                |diff_routes|
|-------|-------------------------|-----------|
|9181   |INTERCAMBIADOR STA.CRUZ  |44         |
|2625   |INTERCAMBIADOR LAGUNA (T)|36         |
|9413   |MERIDIANO                |25         |
|9450   |INTERCAMBIADOR STA.CRUZ  |23         |
|2582   |COROMOTO (T)             |22         |
|2549   |LEOCADIO MACHADO         |22         |
|2692   |FRANCISCO SÁNCHEZ (T)    |21         |

Well I expected some magic output but there are the main bus stations and the previous / next stops. As we can see Santa Cruz station is splitted so I tried ot group also the stops by name.

And it yield some interesting results, a lot of bus stops share it's name even if they're not related the most common one is "Cementerio" (graveyard) and the second one is "Centro de salud" (health centre). 

I include here the top list and it's quite funny tough in such a small location to have so many collisions in names.

|stop_name       |stop_id                                                                                         |diff_stops|
|----------------|------------------------------------------------------------------------------------------------|----------|
|CEMENTERIO      |[1137, 1141, 1204, 1225, 1376, 4074, 4124, 4926, 5027, 5029, 7076, 7095, 7256, 7362, 9105, 9106]|16        |
|CENTRO DE SALUD |[1219, 1883, 1924, 1928, 2587, 2789, 7257, 7361, 7364, 7382, 7455, 9409]                        |12        |
|EL PINO         |[1636, 1647, 2130, 2145, 2314, 2704, 4957, 7577, 7603, 7735, 7782]                              |11        |
|EL CALVARIO     |[1203, 1226, 1258, 1259, 4016, 4035, 4217, 4356, 4359, 4739]                                    |10        |
|EL MOLINO       |[1519, 1571, 1971, 1977, 2573, 2574, 4301, 4308, 4642]                                          |9         |
|CAMPO DE FUTBOL |[1622, 1628, 2128, 2147, 4389, 4533, 9362, 9370]                                                |8         |
|LAS TOSCAS      |[1206, 1223, 1305, 1350, 1765, 2310, 4728, 4733]                                                |8         |


### What is the longest predicted route?

This question should be quite straightforward as we have for any trip all the stops and the predicted "arrival" and "departure" for each one. So we just need to group it and... What is this?

|trip_id|   start|     end|
|-------|--------|--------|
|3927806|24:10:00|24:34:19|
|3927807|25:30:00|25:54:19|
|3927809|24:50:00|25:08:38|
|3927810|26:20:00|26:38:38|
|3928436|25:10:00|25:20:20|
|3928763|24:05:00|24:21:39|
|3928766|24:15:00|24:44:20|
|3928769|24:45:00|25:01:39|
|3930761|28:40:00|29:37:11|
|3930762|25:00:00|25:51:52|
|3930763|27:30:00|28:21:52|
|3930764|24:00:00|24:50:36|
|3930765|26:25:00|27:15:36|
|3930767|24:00:00|24:51:52|
|3930768|26:25:00|27:16:52|
|3930769|25:20:00|26:10:36|
|3932368|24:05:00|24:31:00|
|3932373|24:40:00|25:01:17|
|3934883|24:05:00|24:55:17|
|3934886|25:00:00|25:50:17|

Seems that the people decided to put hour 24 and so on for representing the next day. 

Checking the standard from the gtfs reference is correct:

```
Service day - A service day is a time period used to indicate route scheduling. The exact definition of service day varies from agency to agency but service days often do not correspond with calendar days. A service day may exceed 24:00:00 if service begins on one day and ends on a following day. For example, service that runs from 08:00:00 on Friday to 02:00:00 on Saturday, could be denoted as running from 08:00:00 to 26:00:00 on a single service day.
``` 

So... Let's fix the time and convert it into a timestamp _doing this is awful in pyspark_. 

And after doing this, here are the top results:

|route_short_name|elapsed                            |rank|
|----------------|-----------------------------------|----|
|330             |INTERVAL '0 02:47:22' DAY TO SECOND|1   |
|330             |INTERVAL '0 02:44:55' DAY TO SECOND|2   |
|325             |INTERVAL '0 02:36:24' DAY TO SECOND|3   |
|343             |INTERVAL '0 02:28:52' DAY TO SECOND|4   |
|342             |INTERVAL '0 02:14:25' DAY TO SECOND|5   |
|108             |INTERVAL '0 02:13:36' DAY TO SECOND|6   |
|342             |INTERVAL '0 01:59:51' DAY TO SECOND|7   |
|343             |INTERVAL '0 01:56:35' DAY TO SECOND|8   |
|325             |INTERVAL '0 01:53:27' DAY TO SECOND|9   |
|34              |INTERVAL '0 01:52:27' DAY TO SECOND|10  |

The 330 is a "betlway", it starts and finishes on the same point, so it makes a lot of sense to have such a large estimate time.

And the 325, makes an amazing way. It only works 5 times on labour days and 3 times on weekends.

![](/imgs/325.png)
More questions will be solved soon :) 