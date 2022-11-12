Получение магазинов 🏪
========================================




.. function:: Сделайте запрос методом `GET` по ссылке: api/v1/handbook/shops/


.. note::
   Данная запрос отправляет ответ список магазинов


**Успешный запрос:**

*Ответ*::
   
   - Status: 200 OK


*Дата данные*:

.. code-block:: json

    {
        "links": {
            "first": "http://127.0.0.1:8000/api/v1/handbook/shops/?page_number=1",
            "last": "http://127.0.0.1:8000/api/v1/handbook/shops/?page_number=1",
            "next": null,
            "prev": null
        },
        "data": [
            {
                "type": "Shop",
                "id": "1",
                "attributes": {
                    "name": "Склад Каскелен"
                }
            },
            {
                "type": "Shop",
                "id": "2",
                "attributes": {
                    "name": "Склад Карабулак"
                }
            },
            {
                "type": "Shop",
                "id": "3",
                "attributes": {
                    "name": "Склад Жаркент"
                }
            },
            {
                "type": "Shop",
                "id": "4",
                "attributes": {
                    "name": "Склад Аральск"
                }
            },
            {
                "type": "Shop",
                "id": "5",
                "attributes": {
                    "name": "Склад ВСЦ (неремонтопригодный товар)"
                }
            },
            {
                "type": "Shop",
                "id": "6",
                "attributes": {
                    "name": "Склад Тараз Mall"
                }
            },
            {
                "type": "Shop",
                "id": "7",
                "attributes": {
                    "name": "Склад Шу"
                }
            },
            {
                "type": "Shop",
                "id": "8",
                "attributes": {
                    "name": "Склад Сарыкемер"
                }
            },
            {
                "type": "Shop",
                "id": "9",
                "attributes": {
                    "name": "Склад Алматы ИМ Гранд"
                }
            },
            {
                "type": "Shop",
                "id": "10",
                "attributes": {
                    "name": "Склад Туркестан Rixos"
                }
            },
            {
                "type": "Shop",
                "id": "11",
                "attributes": {
                    "name": "Склад Узынагаш"
                }
            },
            {
                "type": "Shop",
                "id": "12",
                "attributes": {
                    "name": "Склад Торетам"
                }
            },
            {
                "type": "Shop",
                "id": "13",
                "attributes": {
                    "name": "Склад Алматы ИМ ТРЦ МАРТ"
                }
            },
            {
                "type": "Shop",
                "id": "14",
                "attributes": {
                    "name": "Склад Астана Грин Молл"
                }
            },
            {
                "type": "Shop",
                "id": "15",
                "attributes": {
                    "name": "Склад Шиели"
                }
            },
            {
                "type": "Shop",
                "id": "16",
                "attributes": {
                    "name": "Склад Отеген Батыр"
                }
            },
            {
                "type": "Shop",
                "id": "17",
                "attributes": {
                    "name": "Склад Айтеке Би "
                }
            },
            {
                "type": "Shop",
                "id": "18",
                "attributes": {
                    "name": "РЦШ Недостача"
                }
            },
            {
                "type": "Shop",
                "id": "19",
                "attributes": {
                    "name": "ПВЗ Астана ИМ Аружан"
                }
            },
            {
                "type": "Shop",
                "id": "20",
                "attributes": {
                    "name": "Склад Караганда"
                }
            },
            {
                "type": "Shop",
                "id": "21",
                "attributes": {
                    "name": "Склад Тараз-Алатау"
                }
            },
            {
                "type": "Shop",
                "id": "22",
                "attributes": {
                    "name": "ПВЗ Атакент Молл(Алматы)"
                }
            },
            {
                "type": "Shop",
                "id": "23",
                "attributes": {
                    "name": "Склад Тараз Сатпаева временный (недостача)"
                }
            },
            {
                "type": "Shop",
                "id": "24",
                "attributes": {
                    "name": "Склад Алматы ПВЗ Сабрина"
                }
            },
            {
                "type": "Shop",
                "id": "25",
                "attributes": {
                    "name": "Склад Арысь"
                }
            },
            {
                "type": "Shop",
                "id": "26",
                "attributes": {
                    "name": "Склад Ленгер"
                }
            },
            {
                "type": "Shop",
                "id": "27",
                "attributes": {
                    "name": "Склад Шымкент Янги-Шахар"
                }
            },
            {
                "type": "Shop",
                "id": "28",
                "attributes": {
                    "name": "Склад Алматы Ритц Палас"
                }
            },
            {
                "type": "Shop",
                "id": "29",
                "attributes": {
                    "name": "Склад Шымкент Акбар"
                }
            },
            {
                "type": "Shop",
                "id": "30",
                "attributes": {
                    "name": "Склад Кызылорда"
                }
            },
            {
                "type": "Shop",
                "id": "31",
                "attributes": {
                    "name": "Склад Рыскулова Торговый зал"
                }
            },
            {
                "type": "Shop",
                "id": "32",
                "attributes": {
                    "name": "Распределительный центр Алматы"
                }
            },
            {
                "type": "Shop",
                "id": "33",
                "attributes": {
                    "name": "Склад Астана ИМ"
                }
            },
            {
                "type": "Shop",
                "id": "34",
                "attributes": {
                    "name": "Склад Тулькубас"
                }
            },
            {
                "type": "Shop",
                "id": "35",
                "attributes": {
                    "name": "ул.Сейфуллина 510, выше Калинина"
                }
            },
            {
                "type": "Shop",
                "id": "36",
                "attributes": {
                    "name": "ул.Абая 139, уг.ул Жарокова"
                }
            },
            {
                "type": "Shop",
                "id": "37",
                "attributes": {
                    "name": "пр.Н.Абдирова, 19"
                }
            },
            {
                "type": "Shop",
                "id": "38",
                "attributes": {
                    "name": "пр. Шахтеров 82, ТЦ Магнум"
                }
            },
            {
                "type": "Shop",
                "id": "39",
                "attributes": {
                    "name": "Байтурсынова 64"
                }
            },
            {
                "type": "Shop",
                "id": "40",
                "attributes": {
                    "name": "ул.Токмаганбетова 1/77"
                }
            },
            {
                "type": "Shop",
                "id": "41",
                "attributes": {
                    "name": "ул. Толе би, дом № 27 (ТЦ Март)"
                }
            },
            {
                "type": "Shop",
                "id": "42",
                "attributes": {
                    "name": "ул.Рыскулова, б/н"
                }
            },
            {
                "type": "Shop",
                "id": "43",
                "attributes": {
                    "name": "ул.Жангельдина 5А"
                }
            },
            {
                "type": "Shop",
                "id": "44",
                "attributes": {
                    "name": "Тамерлановское шоссе, 30"
                }
            },
            {
                "type": "Shop",
                "id": "45",
                "attributes": {
                    "name": "ул.Аскарова 22"
                }
            },
            {
                "type": "Shop",
                "id": "46",
                "attributes": {
                    "name": "бульвар Кунаева, д.42, ВП-1"
                }
            },
            {
                "type": "Shop",
                "id": "47",
                "attributes": {
                    "name": "Мангилик Ел 19"
                }
            },
            {
                "type": "Shop",
                "id": "48",
                "attributes": {
                    "name": "просп. Тауке хана строение 200"
                }
            },
            {
                "type": "Shop",
                "id": "49",
                "attributes": {
                    "name": "Склад Казыгурт"
                }
            },
            {
                "type": "Shop",
                "id": "50",
                "attributes": {
                    "name": "Склад ВСЦ"
                }
            },
            {
                "type": "Shop",
                "id": "51",
                "attributes": {
                    "name": "Склад Тараз"
                }
            },
            {
                "type": "Shop",
                "id": "52",
                "attributes": {
                    "name": "Склад Сарыагаш"
                }
            },
            {
                "type": "Shop",
                "id": "53",
                "attributes": {
                    "name": "Склад Аксукент"
                }
            },
            {
                "type": "Shop",
                "id": "54",
                "attributes": {
                    "name": "Склад Жетысай"
                }
            },
            {
                "type": "Shop",
                "id": "55",
                "attributes": {
                    "name": "Склад Туркестан"
                }
            },
            {
                "type": "Shop",
                "id": "56",
                "attributes": {
                    "name": "Склад Жангельдина"
                }
            },
            {
                "type": "Shop",
                "id": "57",
                "attributes": {
                    "name": "Склад Рыскулова"
                }
            },
            {
                "type": "Shop",
                "id": "58",
                "attributes": {
                    "name": "Распределительный центр Шымкент"
                }
            },
            {
                "type": "Shop",
                "id": "59",
                "attributes": {
                    "name": "Склад Астана"
                }
            }
        ],
        "meta": {
            "pagination": {
                "page": 1,
                "pages": 1,
                "count": 59
            }
        }
    }