--Calculadora con funcion de orden superior 
--Sergio Luis Huanca Cuellar
--INF -319 2do Parcial
--Pregunta 4

getnum::IO Integer
getnum = do
  s <- getLine
  return (read s)
--funciones
suma :: Integer -> Integer -> Integer
suma x y = x + y

res :: Integer -> Integer -> Integer
res x y = x - y

mul :: Integer -> Integer -> Integer
mul x y = x * y

divi :: Integer -> Integer -> Integer
divi x y = if y == 0 then -1 else x `div` y

--Funicon de orden superior que tiene como parametro una funcion(sum,res,mul,div) 
calcus x y fun = fun x y 
  
calcu = do
-- calculadora funciones
  putStrLn("****CALCULADORA EN HASKELL ORDEN SUPERIOR****")
--introduce dos numeros  
  putStr("Numero 1:\n")
  n1 <- getnum
  putStr("Numero 2:\n")
  n2 <- getnum
--suma llamamos a la funcion calcus de OS, entregamso como parametrola funcion suma
  putStr "La suma es: "
  print (calcus n1 n2 suma)
 --resta llamamosa a la funcion calcus de ORDEN SUPERIOR
  putStr "La resta es: "
  print (calcus n1 n2 res)
 --multiplicacion
  putStr "La multiplicacion es: "
  print (calcus n1 n2 mul)
 --division
  putStr "La divsion es: "
  print (calcus n1 n2 divi)