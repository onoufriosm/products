1. How would your design change if the data was not static (i.e updated frequently
during the day)?
- Reduce cache expiration time

2. Do you think your design can handle 1000 concurrent requests per second? If not, what
would you change?
- Check for bottlenecks - Most likely to be the database with this design
- Denormalise data / Use NoSQL
- Use PostGIS for faster spatial queries - R-tree algorithm
- Cache the queries in redis