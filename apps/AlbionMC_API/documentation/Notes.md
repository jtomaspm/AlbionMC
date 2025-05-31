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
    ISource.Nome as ITEM,
    CS.Qtd as QUANTITY,
    ISource.Preço as PRICE,
    ISource.Preço * CS.Qtd as TOTAL_PRICE
    
FROM
    Items I

JOIN 
    CraftingSlot CS
  ON 
    CS.ItemDestinoID = I.ID

JOIN
    Items ISource
  ON
    CS.ItemSourceID = ISource.ID

WHERE 
    I.Nome = 'Nome que o bot quer'
```

    
```python 
b: Car = Car()
class Car :
    a: int = 3 
```