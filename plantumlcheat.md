
```plantuml
skinparam defaultTextAlignment center
start
if (Question 1) then (yes)
  if (Subquestion) then (yes)
    :Definitely yes!;
  else (no)
    :Maybe?;
  endif
else (no)
  :Obviously not...;
endif
end
stop
```
