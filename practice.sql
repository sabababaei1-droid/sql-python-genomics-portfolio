
-- Analysis 1: Filter variants by allele frequency and CADD score

SELECT gene, AF, CADD
FROM variants
WHERE AF <= 0.01
  AND CADD > 20
ORDER BY CADD DESC;


-- Analysis 2: Count variants per gene

SELECT gene, COUNT(*) AS variant_count
FROM variants
GROUP BY gene
ORDER BY variant_count DESC;


-- Analysis 3: Summary statistics for CADD scores

SELECT
    COUNT(*) AS variant_count,
    ROUND(AVG(CADD), 2) AS mean_cadd,
    MAX(CADD) AS max_cadd
FROM variants;


-- Analysis 4: Complete CADD summary statistics

SELECT
    COUNT(*) AS variant_count,
    ROUND(AVG(CADD), 2) AS mean_cadd,
    MIN(CADD) AS min_cadd,
    MAX(CADD) AS max_cadd
FROM variants;
