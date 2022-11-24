-- This script lists the number of records with same dcore in second_table
SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
