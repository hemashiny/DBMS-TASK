-- Create gold price table
DROP TABLE IF EXISTS gold_prices;
CREATE TABLE gold_prices (
    year INTEGER,
    month TEXT,
    price REAL
);

INSERT INTO gold_prices (year, month, price) VALUES
(2022, 'Jan', 4500), (2022, 'Feb', 4550), (2022, 'Mar', 4600),
(2023, 'Jan', 4700), (2023, 'Feb', 4720), (2023, 'Mar', 4750),
(2024, 'Jan', 4800), (2024, 'Feb', 4850), (2024, 'Mar', 4900);

-- Create ornament table
DROP TABLE IF EXISTS gold_ornaments;
CREATE TABLE gold_ornaments (
    name TEXT,
    price REAL,
    grams REAL
);

INSERT INTO gold_ornaments (name, price, grams) VALUES
('Necklace', 55000, 20),
('Ring', 10000, 4),
('Bangle', 30000, 10);
