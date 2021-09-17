SELECT cuenta, COUNT(cuenta)
FROM count_transaccion
GROUP BY cuenta
HAVING COUNT(cuenta)>1