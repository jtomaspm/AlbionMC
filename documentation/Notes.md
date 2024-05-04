# Notes

## Tables

* Items 
    * ID
    * Nome
    * Preço

* CraftingSlot
    * CraftId
    * ItemDestinoID
    * Qtd
    * ItemSourceId

```sql
SELECT
    (SELECT Nome FROM Items WHERE ID = CS.ItemSourceId LIMIT 1) as Nome,
    CS.Qtd as QTD,
    Nome * QTD as Preço
FROM
    Items I

JOIN 
    CraftingSlot CS
  ON 
    CS.ItemDestinoId = I.ID

WHERE 
    I.Nome = 'Nome que o bot quer'
```

    
```python 
b: Car = Car()
class Car :
    a: int = 3 
```