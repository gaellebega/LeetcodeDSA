s=input()
s=s.lower()
clean="".join(ch for ch in s if ch.isalnum())
reverse=clean[::-1]
if clean==reverse:
  print("True am a plaindrome")
else:
  print("False am not a plandrome")  