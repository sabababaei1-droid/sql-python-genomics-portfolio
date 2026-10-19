-- Analysis 1: Filter variants by allele frequency and CADD score
SELECT gene, AF, CADD
FROM variants
WHERE AF <= 0.01
  AND CADD > 20
ORDER BY CADD DESC;
