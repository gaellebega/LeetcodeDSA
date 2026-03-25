def toLowerCase(self, s: str) -> str:
  for ch in s:
    if ch.islower():
      s=s.lower()
  return s    