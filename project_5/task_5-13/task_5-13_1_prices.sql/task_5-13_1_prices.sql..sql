
UPDATE prices
SET price = price * 1.1
WHERE price < 1000;


SELECT * FROM prices WHERE price >= 1000 AND price < 1100 ORDER BY price DESC;