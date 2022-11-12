Получение списка активных акции 🔢
========================================



API для получения списка активных акций

.. function:: Сделайте запрос методом `GET` по ссылке: /api/v1/sale/?page[number]=2&page[size]=3

.. note::
   Данный запрос отправляет ответ со списками активных акций

   Значение **page[number]** указывает на **id** страницы, 
   
   Значение **page[size]** указывает на количество акций, 
   
   Значение **sale_type** фильтрирует по типу акции,

   Значение **author_id** фильтрирует по **id** автора,

   Значение **start_date** фильтрирует список акций, дата начала которых больше

   Значение **end_date** фильтрирует список акций, дата конец которых меньше

   Значение **is_early_deactivate** фильтрирует по активности акции
   

*Ответ*::
   
   - Status: 200 OK


*Дата данные*:

.. code-block:: json

    {
        "links": {
            "first": "http://127.0.0.1:8000/api/v1/sale/?page%5Bnumber%5D=1&page%5Bsize%5D=3",
            "last": "http://127.0.0.1:8000/api/v1/sale/?page%5Bnumber%5D=2&page%5Bsize%5D=3",
            "next": null,
            "prev": "http://127.0.0.1:8000/api/v1/sale/?page%5Bnumber%5D=1&page%5Bsize%5D=3"
        },
        "data": [
            {
                "type": "Sale",
                "id": "39",
                "attributes": {
                    "start_date": "2022-07-05T11:30:00+06:00",
                    "end_date": "2022-10-05T11:30:00+06:00",
                    "payment_method": "Картой",
                    "is_use_of_bonuses": true,
                    "is_manual_sale": true,
                    "is_compensated": true,
                    "prioritet": 7,
                    "sale_type": "cascadetype",
                    "is_active": true,
                    "author": {
                        "id": 2,
                        "full_name": "Auth Service",
                        "role_id": 4
                    }
                },
                "relationships": {
                    "is_intersects_models": {
                        "data": [
                            {
                                "id": 2,
                                "model": "percenttype"
                            }
                        ]
                    },
                    "content_object": {
                        "data": {
                            "cascade_positions": [
                                {
                                    "position": 1,
                                    "percent": 20
                                },
                                {
                                    "position": 2,
                                    "percent": 50
                                }
                            ]
                        }
                    }
                }
            },
            {
                "type": "Sale",
                "id": "43",
                "attributes": {
                    "start_date": "2022-07-07T11:30:00+06:00",
                    "end_date": "2022-07-20T11:30:00+06:00",
                    "payment_method": "Картой",
                    "is_use_of_bonuses": true,
                    "is_manual_sale": true,
                    "is_compensated": true,
                    "prioritet": 10,
                    "sale_type": "chancetype",
                    "is_active": true,
                    "author": {
                        "id": 2,
                        "full_name": "Auth Service",
                        "role_id": 4
                    }
                },
                "relationships": {
                    "is_intersects_models": {
                        "data": [
                            {
                                "id": 2,
                                "model": "percenttype"
                            },
                            {
                                "id": 3,
                                "model": "gifttype"
                            },
                            {
                                "id": 4,
                                "model": "specialpricetype"
                            }
                        ]
                    },
                    "content_object": {
                        "data": {
                            "id": 2,
                            "min_amount": 50000,
                            "multiplicity": 50000
                        }
                    }
                }
            },
            {
                "type": "Sale",
                "id": "46",
                "attributes": {
                    "start_date": "2022-07-07T11:30:00+06:00",
                    "end_date": "2022-10-11T11:30:00+06:00",
                    "payment_method": "Картой",
                    "is_use_of_bonuses": true,
                    "is_manual_sale": true,
                    "is_compensated": true,
                    "prioritet": 1001,
                    "sale_type": "promocodetype",
                    "is_active": true,
                    "author_id": null
                },
                "relationships": {
                    "is_intersects_models": {
                        "data": [
                            {
                                "id": 1,
                                "model": "cascadetype"
                            },
                            {
                                "id": 2,
                                "model": "percenttype"
                            }
                        ]
                    },
                    "content_object": {
                        "data": {
                            "id": 3,
                            "fixed_price": 10000,
                            "percent": 10000,
                            "promo_code": "dd",
                            "activation_period_start": "2022-07-06T11:30:00+06:00",
                            "activation_period_end": "2022-10-05T11:30:00+06:00",
                            "promocode_type": "fixed_price"
                        }
                    }
                }
            }
        ],
        "meta": {
            "pagination": {
                "page": 2,
                "pages": 2,
                "count": 6
            }
        }
    }