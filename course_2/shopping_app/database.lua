       +------------------+       +-------------------+
       |      Users       |       |      Admins       |
       +------------------+       +-------------------+
       | user_id (PK)     |       | admin_id (PK)     |
       | username         |       | username          |
       | password         |       | password          |
       | email            |       | email             |
       | address          |       +-------------------+
       | phone_number     |
       | session_id       |
       +--------+---------+
                |
                |    +-------------------+
                +----|       Cart        |
                |    +-------------------+
                |    | cart_id (PK)      |
                |    | user_id (FK)      |
                |    | product_id (FK)   |
                |    | quantity          |
                |    +-------------------+
                |
                |    +-----------------------+
                +----|      Orders          |
                |   +-----------------------+
                |   | order_id (PK)         |
                |   | user_id (FK)          |
                |   | product_id (FK)       |
                |   | quantity              |
                |   | total_amount          |
                |   | payment_option_id (FK)|
                |   | order_date            |
                |   +-----------------------+
                |
                |
       +------------------+       +-------------------+
       |     Products     |       |     Categories    |
       +------------------+       +-------------------+
       | product_id (PK)  |       | category_id (PK)  |
       | name             |       | name              |
       | category_id (FK) +-------|                   |
       | price            |       +-------------------+
       +------------------+


                  +-----------------------+
                  |   Payment Options     |
                  +-----------------------+
                  | payment_option_id (PK)|
                  | name                  |
                  +-----------------------+
