SELECT a.unique_id, b.name 
FROM EmployeeUNI a 
Right JOIN Employees b 
ON a.id = b.id;
