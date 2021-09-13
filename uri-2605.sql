SELECT products.name,providers.name 
FROM products,providers
WHERE id_categories=6 
AND products.id_providers=providers.id;