
-- standarize date format

UPDATE housing
SET SaleDate = CONVERT(SaleDate, DATE)

SELECT SaleDate FROM housing

-- populate property address

SELECT *
FROM housing
-- WHERE PropertyAddress IS NULL
ORDER BY ParcelID

SELECT *
FROM housing a
JOIN housing b
ON a.ParcelID = b.ParcelID
AND a.UniqueID = b.UniqueID
