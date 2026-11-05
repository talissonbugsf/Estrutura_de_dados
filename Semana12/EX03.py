def soma(n):
  if n <= 1:
    return 1
  return n + soma(n - 1)

resultado = soma(6)
print(f"soma(6) = {resultado}")
