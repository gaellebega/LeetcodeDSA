def toLowerCase(s) -> str:
  for ch in s:
    if ch.islower():
      s=s.lower()
  return s
print(toLowerCase("MUKAmana"))