-- Migration to add feedback column to guesses table

ALTER TABLE guesses
ADD COLUMN feedback VARCHAR(20);
