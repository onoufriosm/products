// SQL to retrieve shops in proximity (+ including tags if provided) -> products -> N most popular

"SELECT title, ( 3959 * acos( cos( radians(" + lat + ") ) * cos( radians( lat ) ) * cos( radians( lng ) - radians(" + lng + ") ) + sin( radians(" + lat +  ") ) * sin( radians( lat ) ) ) ) AS distance FROM shops HAVING distance < " + radius + " ORDER BY distance;");

// Cache results

// Write unit tests

