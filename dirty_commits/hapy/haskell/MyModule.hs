module MyModule where

-- Use Integer if you don't want to have arithmetic overflows
factorial :: Int -> Int
factorial n = if n == 0 then 1 else n * factorial (n-1)

-- Unexposed function
add :: Int -> Int -> Int
add x y = x + y
