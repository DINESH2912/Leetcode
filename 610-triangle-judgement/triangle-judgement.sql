select *,
case
when abs(z)+abs(x)>abs(y) and abs(x)+abs(y)>abs(z) and abs(y)+abs(z)>abs(x)   then "Yes"
else "No"
end as 'triangle'
from Triangle;
