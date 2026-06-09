## структура проекта

### уровень 1

* папка level_1/task_1: задание 1. первая корутина и измерение времени
* папка level_1/task_2: задание 2. явные задачи: последовательно против конкурентно
* папка level_1/task_3: задание 3. сбор результатов через asyncio.gather
* папка level_1/task_4: задание 4. симулятор сетевых задержек
* папка level_1/task_5: задание 5. обработка ошибок в группе корутин

### уровень 2

* папка level_2/task_6: задание 6. тайм-ауты для долгих операций
* папка level_2/task_7: задание 7. отмена задач и cancellederror
* папка level_2/task_8: задание 8. управление объектами task
* папка level_2/task_9: задание 9. агрегатор данных из нескольких источников
* папка level_2/task_10: задание 10. ограничение одновременности через semaphore

## инструкции по запуску

для запуска любого задания перейдите в корень проекта и выполните соответствующую команду:

* python level_1/task_1/async_timer.py
* python level_1/task_2/pipeline.py
* python level_1/task_3/gather_aggregator.py
* python level_1/task_4/network_simulator.py
* python level_1/task_5/gather_errors.py
* python level_2/task_6/timeouts_demo.py
* python level_2/task_7/cancel_tasks.py
* python level_2/task_8/task_management.py
* python level_2/task_9/data_aggregator.py
* python level_2/task_10/semaphore_limit.py

для задания 10 также можно передать лимит через аргумент:
* python level_2/task_10/semaphore_limit.py --limit 5
