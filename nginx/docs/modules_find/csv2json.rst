Csv в json продукты 🔍
========================================



API для поиска товара

.. function:: Сделайте запрос методом `POST` по ссылке: /api/v1/sale/product-excel/

.. note::
   При помощи запроса вы можете найти детальную информацию акции о продуках

   Так же в запросе добавлено поле для поиска акции типа {'chance'} где 
   показывает может ли учавствовать клиент в акции, а так же выводит 
   детальную информацию если клиент учавствует в этой акции



   *Заголовок*::
      
      - header 'Authorization: {Token}' 
      - header 'Content-Type: application/vnd.api+json' 

   *Тело запроса*:

.. note::
   При помощи запроса **form-data** вы можете конвертировать cvs(excel) файлы в json формат

   В запросе в **form-data** добавитье поле с названием **file** и загрузить значением 
   файл формата **.csv**



*Ответ*::
   
   - Status: 200 OK


*Дата данные*:

.. code-block:: json

    {
        "data": [
            {
                "id": 4000,
                "full_name": "Смарт-часы Huawei Watch Fit New Isle Blue TIA-B09 MCHN03",
                "price": 44950
            },
            {
                "id": 2,
                "full_name": "Чехол iPhone 12 mini Leather Case with MagSafe - Baltic Blue",
                "price": 14990
            },
            {
                "id": 3,
                "full_name": "Чехол iPhone 12 mini Leather Case with MagSafe - Black",
                "price": 39990
            }
        ]
    }



