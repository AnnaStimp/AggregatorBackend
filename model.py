host = '127.0.0.1'
user = 'postgres'
password = 'AnnaStimp13'
db_name = 'aggregator'
port = 5432
    

def get_new_product (cursor):
  cursor.execute(
    """SELECT product.id_product, product.name_product, product.about_product,
    MIN(price) AS price, picture_product
    FROM price_list INNER JOIN product
    ON product.ID_product = price_list.ID_product
    GROUP BY product.name_product, product.about_product, picture_product, product.id_product
    ORDER BY product.id_product DESC
    limit 4"""
  )

  return cursor.fetchall()

def get_category (cursor):
  cursor.execute(
    """SELECT *
    FROM category"""
  )

  return cursor.fetchall()

def get_product_of_category (cursor, id):
  cursor.execute(
    """SELECT product.id_category, product.id_product, product.name_product, product.about_product,
    MIN(price) AS price, picture_product
    FROM price_list INNER JOIN product
    ON product.ID_product = price_list.ID_product
    WHERE product.id_category = {}
    GROUP BY product.name_product, product.about_product, picture_product, product.id_product""".format(id)
  )

  return cursor.fetchall()

def get_product (cursor, id):
  cursor.execute(
    """SELECT product.id_product, product.name_product, store.name_store, product.about_product, price, link_product, picture_product
    FROM price_list INNER JOIN product 
    ON product.id_product = price_list.id_product INNER JOIN store
    ON store.id_store = price_list.id_store
    WHERE product.id_product = {}""".format(id)
  )

  return cursor.fetchall()

def get_products (cursor):
  cursor.execute(
    """SELECT id_product
    FROM product"""
  )

  return cursor.fetchall()

def get_users (cursor):
  cursor.execute(
    """SELECT *
    FROM users"""
  )

  return cursor.fetchall()