SELECT subcategoria , date_format(fecha, "%m-%Y")as fecha, avg(precio_referencia) as average_price
                                            FROM productos
                                            INNER JOIN precios ON productos.idproductos = precios.productos_idproductos
                                            WHERE subcategoria in ("pan", "cereales", "aceites", "leche", "legumbres")
                                            GROUP BY subcategoria, year(fecha), month(fecha);